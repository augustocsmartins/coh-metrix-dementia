from nltk.data import load
from os.path import dirname, abspath
from sys import modules


base_path = abspath(dirname(modules[__name__].__file__))

senter = load(base_path + '/../models/punkt/punkt-senter.pickle')
