# -*- coding: utf-8 -*-


class ResourcePool(object):
    """A resource pool is a repository of methods for extracting data from
    texts. It centralizes tasks like PoS-tagging and sentence splitting,
    allowing synchronization among threads and use of multiple tools for
    the same task (e.g., taggers).
    """
    def __init__(self, debug=False):
        """Form a new resource pool."""
        self._res = {}  # The resources, in the form {<suffix> : <hook>}.
        self._cache = {}  # Resources already asked for, in the form
# {(<text>, <suffix>) : <data>}.
        self._debug = debug

    def register(self, suffix, hook):
        """Register a new resource.

        :suffix: @todo
        :hook: @todo
        :returns: @todo

        """
        self._res[suffix] = hook

    def get(self, text, suffix):
        """Get a resource.

        :text: @todo
        :id: @todo
        :returns: @todo

        """
        if (text, suffix) not in self._cache:
            self._cache[(text, suffix)] = self._res[suffix](text)

            if self._debug:
                print('Resource', suffix, 'calculated for text', text)

        return self._cache[(text, suffix)]
