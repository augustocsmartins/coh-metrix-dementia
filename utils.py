from os.path import dirname, abspath
from sys import modules


base_path = abspath(dirname(modules[__name__].__file__))


def ilen(it):
    """Calculate the number of elements in an iterable.
    """
    if isinstance(it, list) or isinstance(it, tuple):
        return len(it)

    count = 0
    for i in it:
        count = count + 1
    return count
