# -*- coding: utf-8 -*-
# base.py - Basic classes for accessing Coh-Metrix-Port's functionality.
# Copyright (C) 2014  Andre Luiz Verucci da Cunha
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.

from coh.utils import is_valid_id
from coh.resource_pool import ResourcePool,\
    DefaultResourcePool, rp as default_rp
import codecs
import collections


class Text(object):
    """Represents a text: its content and metadata.

    A text has several (optional) attributes: title, author,
    source, publication data and genre.
    """
    def __init__(self, filepath, encoding='utf-8', title='', author='',
                 source='', publication_date='', genre=''):
        """Form a text.

        Required arguments:
        filepath -- a path to the file containing the text. The text is
            supposed to be formatted as one paragraph per line, with
            multiple sentences per paragraph. Blank lines are ignored.

        Keyword arguments:
        encoding -- The encoding of the input file (default "utf-8")
        title -- The title of the text (default "").
        author -- The author of the text (default "").
        source -- Where the text came from, usually a URL (default "").
        publication_date -- When the text was released (default "").
        genre -- The textual genre that better fits the text (default "").
        """
        self.title = title
        self.author = author
        self.source = source
        self.publication_date = publication_date
        self.genre = genre

        with codecs.open(filepath, mode='r', encoding=encoding)\
                as input_file:
            content = input_file.readlines()

            self.paragraphs = [line.strip() for line in content
                               if not line.isspace()]

    def __str__(self):
        return '<Text: "%s...">' % (self.paragraphs[0][:70])


class Category(object):
    """Represents a set of taxonomically related metrics.
    """
    def __init__(self, name=None, table_name=None, desc=None):
        """Form a category.

        Keyword arguments:
        name -- A succint name of the category (e.g., 'Basic Counts'). If
            no name is provided, the class name is used. (default None).
        table_name -- The name of the table in coh_user_data that contains
            the values of this category on the users's texts. If no value is
            specified, Coh-Metrix-Port will check whether 'name' is a valid
            table name; if so, 'name' is used as the table name. (default None)
        desc -- A longer description of the category. Used for UI purposes.
            If no value is passed, the docstring of the class is used.
            (default None)
        """
        if name is None:
            name = self.__class__.__name__
        self.name = name

        if table_name is None:
            if is_valid_id(name):
                table_name = name
            else:
                raise ValueError('No valid table name provided.')
        self.table_name = table_name

        if desc is None:
            desc = self.__doc__

        self.desc = desc

    def _set_metrics_from_module(self, module):
        """Set self.metrics as the list of Metric subclasses declared in
            a module.

        Required arguments:
        module -- the name of module that will be scanned for metrics.
        """
        import sys
        import inspect

        self.metrics = [obj() for _, obj
                        in inspect.getmembers(sys.modules[module])
                        if inspect.isclass(obj) and issubclass(obj, Metric)]

    def values_for_text(self, text, rp=default_rp):
        """Calculate the value of each metric in a text and return it in a
            ResultSet.

        Required arguments:
        text -- the text whose metrics will be extracted.

        Returns: a ResultSet containing the calculated metrics.
        """
        #metrics_values = ResultSet([m.value_for_text(text).items()[0]
        #                            for m in self.metrics])
        metrics_values = ResultSet([(m, m.value_for_text(text))
                                    for m in self.metrics])
        #return ResultSet([(self, metrics_values)])
        return metrics_values

    def __str__(self):
        return '<Category: %s: %s>' % \
            (self.name, str([m.name for m in self.metrics]))

    def __getattr__(self, attr):
        # A metric's column name can be used as an attribute to access its
        # object in self.metrics.
        for m in self.metrics:
            if m.column_name == attr:
                return m
        raise AttributeError('%s: no such metric.' % attr)

    def __getitem__(self, key):
        # A metric's column name and its name can be used as an index
        # to access its object in self.metrics.
        for m in self.metrics:
            if m.column_name == key or m.name == key:
                return m
        raise KeyError('%s: no such metric.' % key)


class Metric(object):
    """A metric is a textual characteristic.
    """

    def __init__(self, name=None, column_name=None, desc=None):
        """Form a metric.

        Keyword arguments:
        name -- A succint name of the metric (e.g., 'Flesch index'). If
            no name is provided, the class name is used. (default None)
        table_name -- The name of the column in the table corresponding to
            the category of this metric in coh_user_data. If no value is
            specified, Coh-Metrix-Port will check whether 'name' is a valid
            table name; if so, 'name' is used as the table name. (default None)
        desc -- A longer description of the metric. Used for UI purposes.
            (default None)
        """
        if name is None:
            name = self.__class__.__name__
        self.name = name

        if column_name is None:
            if is_valid_id(name):
                column_name = name
            else:
                raise ValueError('No valid column name provided.')
        self.column_name = column_name

        self.desc = desc

    def value_for_text(self, text, rp=default_rp):
        """Calculate the value of the metric in the text.

        Required arguments:
        text -- The text to be analyzed.

        Returns: an integer value, corresponding to the metric.
        """
        raise NotImplementedError('Subclasses should implement this method!')

    def __str__(self):
        return '<Metric: %s> ' % (self.name)


class MetricsSet(object):
    def __init__(self, categories):
        self.categories = categories

    def _set_categories_from_module(self, module):
        """Set self.categories as the list of Category subclasses
            declared in a module.

        Required arguments:
        module -- the name of module that will be scanned for categories.
        """
        import sys
        import inspect

        self.categories = [obj() for _, obj
                           in inspect.getmembers(sys.modules[module])
                           if inspect.isclass(obj)
                           and issubclass(obj, Category)]

    def values_for_text(self, t):
        return ResultSet([(c, c.values_for_text(t)) for c in self.categories])


class ResultSet(object):
    """A dictionary-like structure that represents the values of
        a set of metrics extracted from a text.
    """
    def __init__(self, *args, **kwargs):
        #TODO: To improve performance, replace OrderedDict by namedtuple.
        self._store = collections.OrderedDict(*args, **kwargs)

    def items(self):
        return self._store.items()

    def __getitem__(self, key):
        if isinstance(key, int):
            key = list(self._store.items())[key][0]
        return self._store[key]

    def __setitem__(self, key, value):
        self._store[key] = value

    def __delitem__(self, key):
        del self._store[key]

    def __iter__(self):
        return iter(self._store)

    def __len__(self):
        return len(self._store)

    def __getattr__(self, attr):
        for key in self._store.keys():
            if (isinstance(key, Category) and key.table_name == attr) or \
               (isinstance(key, Metric) and key.column_name == attr):
                return self._store[key]

    def __str__(self):
        from prettytable import PrettyTable

        table = PrettyTable(['Metric', 'Value'])
        table.align['Metric'] = 'r'
        table.align['Value'] = 'r'
        table.padding_width = 1

        string = ''
        for key, value in self._store.items():
            if isinstance(key, Category):
                string = string + '%s:\n%s\n' % (key.name, value)
                is_table = False
            elif isinstance(key, Metric):
                table.add_row([key.name, str(value)])
                is_table = True

        if is_table:
            string = table.get_string()

        return string.rstrip()


