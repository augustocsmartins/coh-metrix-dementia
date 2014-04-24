# -*- coding: utf-8 -*-
# resource_pool.py - Classes for storing and retrieving data from texts.
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

from itertools import chain
from coh.tools import senter, word_tokenize,\
    pos_tagger


class ResourcePool(object):
    """A resource pool is a repository of methods for extracting data from
    texts. It centralizes tasks like PoS-tagging and sentence splitting,
    allowing synchronization among threads and use of multiple tools for
    the same task (e.g., taggers).
    """
    def __init__(self, debug=False):
        """Form a new resource pool."""
        # The resources, in the form {<suffix> : <hook>}.
        self._res = {}
        # Resources already asked for, in the form
        # {(<text>, <suffix>) : <data>}.
        self._cache = {}
        self._debug = debug

    def register(self, suffix, hook):
        """Register a new resource.

        :suffix: A string identifying the resource type.
        :hook: The method that, when called, generates the resource data.
        :returns: None.

        """
        self._res[suffix] = hook
        setattr(self, suffix, lambda t: self.get(t, suffix))

    def get(self, text, suffix):
        """Get a resource.

        :text: The text to be analyzed.
        :suffix: The type of the resource to be extracted.
        :returns: The resource data (as returned by the resource's hook.)

        """
        if (text, suffix) not in self._cache:
            self._cache[(text, suffix)] = self._res[suffix](text)

            if self._debug:
                print('Resource', suffix, 'calculated for text', text)

        return self._cache[(text, suffix)]


class DefaultResourcePool(ResourcePool):
    """A resource pool that uses the standard tools.
    """
    def __init__(self, debug=False):
        """Registers the default resources."""
        super(DefaultResourcePool, self).__init__(debug)

        self.register('paragraphs', lambda t: t.paragraphs)
        self.register('sentences', self._sentences)
        self.register('words', self._words)
        self.register('all_words', self._all_words)
        self.register('tagged_sentences', self._tagged_sentences)
        self.register('tagged_words', self._tagged_words)

    def _sentences(self, text):
        """Return a list of strings, each one being a sentence of the text.
        """
        paragraphs = self.get(text, 'paragraphs')
        sentences = chain.from_iterable(
            [senter.tokenize(p) for p in paragraphs])
        return list(sentences)

    def _words(self, text):
        """Return a list of lists of strings, where each list of strings
            corresponds to a sentence, and each string in the list is a word.
        """
        sentences = self.get(text, 'sentences')
        return list([word_tokenize(sent) for sent in sentences])

    def _all_words(self, text):
        """Return all words of the text in a single list.
        """
        words = self.get(text, 'words')
        return list(chain.from_iterable(words))

    def _tagged_sentences(self, text):
        """Return a list of lists of pairs (string, string), representing
            the sentences with tagged words.
        """
        words = self.get(text, 'words')
        return pos_tagger.tag_sents(words)

    def _tagged_words(self, text):
        """Return a list of pair (string, string), representing the tokens
            not separated in sentences.
        """
        tagged_sentences = self.get(text, 'tagged_sentences')
        return list(chain.from_iterable(tagged_sentences))

rp = DefaultResourcePool()
