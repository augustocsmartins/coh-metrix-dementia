#-*- coding: utf-8 -*-
# opennlp.py - An OpenNLP tagger trained using the MacMorpho corpus.
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

from coh.tools.tag.api import Tagger
from coh.tools.tag.macmorpho import MacMorphoTagSet
from coh.utils import base_path
from nltk.tag import OpenNLPPoSTagger


class OpenNLPTagger(Tagger):
    """Represents an OpenNLP tagger trained on the MacMorpho corpus.
    """
    def __init__(self):
        self._pos_tagger = OpenNLPPoSTagger(
            path=base_path + '/vendor/apache-opennlp-1.5.3/bin/opennlp',
            model=base_path + '/models/opennlp/pt-pos-maxent.bin',
            encoding='utf-8')

        self.tagset = MacMorphoTagSet()

    def tag(self, tokens):
        return self._pos_tagger.tag(tokens)

    def batch_tag(self, sentences):
        return self._pos_tagger.batch_tag(sentences)
