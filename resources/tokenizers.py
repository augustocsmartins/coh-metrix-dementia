import nltk
from nltk.data import load
from nltk.tag import OpenNLPPoSTagger
from coh.utils import base_path

senter = load(base_path + '/models/punkt/punkt-senter.pickle')

word_tokenize = nltk.word_tokenize
