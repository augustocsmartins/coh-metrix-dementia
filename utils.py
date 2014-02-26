from os.path import dirname, abspath
from sys import modules


base_path = abspath(dirname(modules[__name__].__file__))


def ilen(it):
    count = 0
    for i in it:
        count = count + 1
    return count
