#-*- coding: utf-8 -*-
# macmorpho.py - The tagset used to annotate the MacMorpho corpus.
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

from coh.tools.tag.api import TagSet


class MacMorphoTagSet(TagSet):
    article_tags = ['ART']
    verb_tags = ['V']
    auxiliary_verb_tags = ['VAUX']
    participle_tags = ['PCP']
    noun_tags = ['N',
                 'NPROP']
    adjective_tags = ['ADJ']
    adverb_tags = ['ADV',
                   'ADV-KS'
                   'ADV-KS-REL']
    pronoun_tags = ['PROPESS',
                    'PROSUB',
                    'PROADJ',
                    'PRO-KS',
                    'PRO-KS-REL',
                    ]
    numeral_tags = ['NUM']
    conjunction_tags = ['KS',
                        'KC']
    preposition_tags = ['PREP',
                        'PREP+PROPESS',
                        'PREP+ART']
    interjection_tags = ['IN']
    denotative_word_tags = ['PDEN']

    content_word_tags = verb_tags\
        + noun_tags\
        + adjective_tags\
        + adverb_tags

    function_word_tags = article_tags\
        + preposition_tags\
        + pronoun_tags\
        + conjunction_tags\
        + interjection_tags

    functions_as_noun_tags = ['N', 'NPROP', 'PROSUB']
    functions_as_adjective_tags = ['ADJ', 'PROADJ']

    punctuation_tags = ['PU']

    def is_denotative_word(self, token):
        """Check if a token represents a denotative word.

        Required parameters:
        token -- a tokenized word (a pair (string, string)).
        """
        return self._is_in(token, self.denotative_word_tags)
