import nltk
from nltk.data import load
from nltk.tag import OpenNLPPoSTagger
from os.path import dirname, abspath
from sys import modules


base_path = abspath(dirname(modules[__name__].__file__))

senter = load(base_path + '/../models/punkt/punkt-senter.pickle')

pos_tagger = OpenNLPPoSTagger(
    path=base_path + '/../vendor/apache-opennlp-1.5.3/bin/opennlp',
    model=base_path + '/../models/opennlp/pt-pos-maxent.bin',
    encoding='utf-8')

word_tokenize = nltk.word_tokenize
