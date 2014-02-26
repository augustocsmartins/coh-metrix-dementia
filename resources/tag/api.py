#-*- coding: utf-8 -*-
# api.py - Basic classes for tagging functionalities.
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

import warnings


class Tagger(object):
    """Represents an interface for classes that perform part-of-speech tagging.

    There are two basic methods:
        tag: takes as input a list of tokens and return a list of tuples
        (string, string), containing the token and its PoS tag.

        batch_tag: takes as input a list of tokenized sentences and analyze
        them all at once.

    Derived classes must override at least one these methods. This class is
    based on nltk.tag.api.TaggerI
    (see http://www.nltk.org/api/nltk.tag.html#nltk.tag.api.TaggerI).
    """

    def tag(self, tokens):
        """Assign a part-of-speech tag to a tokenized sentence.

        Required parameters:
        tokens -- a list of strings, containing the tokens to be analyzed.

        Returns:
        A list of pairs (string, string), where the first string is the token
            and the second one is the corresponding PoS tag.
        """
        return self.batch_tag([tokens])[0]

    def batch_tag(self, sentences):
        """Assign part-of-speech tags to multiple sentences at once.

        Required parameters:
        sentences -- A list of lists of strings, containing the tokens to
            be analyzed, separated by sentences.

        Returns:
        A list of lists of pairs (string, string), one list of each sentence.
        """
        return [self.tag(sent) for sent in sentences]


class TagSet(object):
    """Represents a set of tags used by a tagger. This class is entended to
    facilitate the use of multiple taggers with different tagsets.

    Subclasses must, at least, define the *_tags lists.
    """
    article_tags = []
    verb_tags = []
    auxiliary_verb_tags = []
    participle_tags = []
    noun_tags = []
    adjective_tags = []
    adverb_tags = []
    pronoun_tags = []
    numeral_tags = []
    conjuntion_tags = []
    preposition_tags = []
    interjection_tags = []
    currency_tags = []

    content_word_tags = []
    function_word_tags = []

    functions_as_noun_tags = []
    functions_as_adjective_tags = []

    punctuation_tags = []

    def _is_in(self, token, _list):
        """Return true if the token's tag is in the list, and false otherwise.
        """
        if not _list:
            warnings.warn('Empty list')
        return token[1] in _list

    def is_article(self, token):
        """Check if a token represents an article.

        Required parameters:
        token -- a tokenized word (a pair (string, string)).
        """
        return self._is_in(token, self.article_tags)

    def is_verb(self, token):
        """Check if a token represents a verb.

        Required parameters:
        token -- a tokenized word (a pair (string, string)).
        """
        return self._is_in(token, self.verb_tags)

    def is_auxiliary_verb(self, token):
        """Check if a token represents an auxiliary verb.

        Required parameters:
        token -- a tokenized word (a pair (string, string)).
        """
        return self._is_in(token, self.auxiliary_verb_tags)

    def is_participle(self, token):
        """Check if a token represents a verb in the participle.

        Required parameters:
        token -- a tokenized word (a pair (string, string)).
        """
        return self._is_in(token, self.participle_tags)

    def is_noun(self, token):
        """Check if a token represents a noun.

        Required parameters:
        token -- a tokenized word (a pair (string, string)).
        """
        return self._is_in(token, self.noun_tags)

    def is_adjective(self, token):
        """Check if a token represents an adjective.

        Required parameters:
        token -- a tokenized word (a pair (string, string)).
        """
        return self._is_in(token, self.adjective_tags)

    def is_adverb(self, token):
        """Check if a token represents an adverb.

        Required parameters:
        token -- a tokenized word (a pair (string, string)).
        """
        return self._is_in(token, self.adverb_tags)

    def is_pronoun(self, token):
        """Check if a token represents a pronoun.

        Required parameters:
        token -- a tokenized word (a pair (string, string)).
        """
        return self._is_in(token, self.pronoun_tags)

    def is_numeral(self, token):
        """Check if a token represents a numeral.

        Required parameters:
        token -- a tokenized word (a pair (string, string)).
        """
        return self._is_in(token, self.numeral_tags)

    def is_conjunction(self, token):
        """Check if a token represents a conjunction.

        Required parameters:
        token -- a tokenized word (a pair (string, string)).
        """
        return self._is_in(token, self.conjunction_tags)

    def is_preposition(self, token):
        """Check if a token represents a preposition.

        Required parameters:
        token -- a tokenized word (a pair (string, string)).
        """
        return self._is_in(token, self.preposition_tags)

    def is_interjection(self, token):
        """Check if a token represents an interjection.

        Required parameters:
        token -- a tokenized word (a pair (string, string)).
        """
        return self._is_in(token, self.interjection_tags)

    def is_currency(self, token):
        """Check if a token represents a currency value.

        Required parameters:
        token -- a tokenized word (a pair (string, string)).
        """
        return self._is_in(token, self.currency_tags)

    def is_content_word(self, token):
        """Check if a token represents a content word.

        Required parameters:
        token -- a tokenized word (a pair (string, string)).
        """
        return self._is_in(token, self.content_word_tags)

    def is_function_word(self, token):
        """Check if a token represents a function word.

        Required parameters:
        token -- a tokenized word (a pair (string, string)).
        """
        return self._is_in(token, self.function_word_tags)

    def functions_as_noun(self, token):
        """Check if a token represents a word that functions as a noun.

        Required parameters:
        token -- a tokenized word (a pair (string, string)).
        """
        return self._is_in(token, self.functions_as_noun_tags)

    def functions_as_adjective(self, token):
        """Check if a token represents a word that functions as an adjective.

        Required parameters:
        token -- a tokenized word (a pair (string, string)).
        """
        return self._is_in(token, self.functions_as_adjective_tags)

    def is_punctuation(self, token):
        """Check if a token represents a punctuation mark.

        Required parameters:
        token -- a tokenized word (a pair (string, string)).
        """
        return self._is_in(token, self.punctuation_tags)
