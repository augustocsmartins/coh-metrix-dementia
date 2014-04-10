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
from nltk.tag.util import str2tuple
import codecs
import subprocess
import tempfile


class OpenNLPTagger(Tagger):
    """Represents an OpenNLP tagger trained on the MacMorpho corpus.
    """
    def __init__(self):
        self._path = base_path + '/vendor/apache-opennlp-1.5.3/bin/opennlp'
        self._model = base_path + '/models/opennlp/pt-pos-maxent.bin'
        self._encoding = 'utf-8'

        self.tagset = MacMorphoTagSet()

    def tag_sents(self, sentences):
        # Create a temporary input file.
        _, _input_file_path = tempfile.mkstemp(text=True)

        # Write the sentences to the temporary input file.
        with codecs.open(_input_file_path, mode='w', encoding=self._encoding)\
                as _input_file:
            _input = '\n'.join((' '.join(x) for x in sentences))
            _input_file.write(_input)

        with codecs.open(_input_file_path, mode='r', encoding=self._encoding)\
                as _input_file:
            # Run the tagger and get the output
            p = subprocess.Popen(self._cmd, stdin=_input_file,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)

            result = p.communicate()

        return self._process_output(result[0].decode(self._encoding))

    @property
    def _cmd(self):
        return [self._path, 'POSTagger', self._model]

    def _process_output(self, out):
        # Ignore the first line, containing:
        #       "Loading POS Tagger model ... done (x.xxxs)"
        # , the last three lines, containing:
        #       "Average: x sents/x
        #        Total: x sents
        #        Runtime: xs"
        # and empty lines
        lines = [line for line in out.split('\n') if line.strip()][1:-3]
        as_tuples = lambda line: [str2tuple(token, sep='_')
                                  for token in line.split(' ')]
        return [as_tuples(line) for line in lines]
