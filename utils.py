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


def is_valid_id(string):
    """Check whether a string is a valid id.

    :string: The string to be checked
    :returns: True if the string represents a valid id; false otherwise.

    """
    import re

    return re.match("^[_A-Za-z][_a-zA-Z0-9]*$", string) is not None
