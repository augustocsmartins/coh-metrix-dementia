from coh import base
from coh.utils import ilen
from coh.resources import syllable_separator
from itertools import chain


class Flesch(base.Metric):
    """
    """
    def __init__(self, name='Flesch index', column_name='flesch'):
        super(Flesch, self).__init__(name, column_name)

    def value_for_text(self, t):
        mean_words_per_sentence = WordsPerSentence().value_for_text(t)

        syllables = chain(map(syllable_separator.separate, t.all_words))
        mean_syllables_per_word = ilen(t.all_words) / ilen(syllables)

        flesch = 164.835 - 1.015 * mean_words_per_sentence\
            - 84.6 * mean_syllables_per_word

        return flesch


class Words(base.Metric):
    """
    """
    def __init__(self, name='Number of Words', column_name='words'):
        super(Words, self).__init__(name, column_name)

    def value_for_text(self, t):
        return ilen(t.all_words)


class Sentences(base.Metric):
    """
    """
    def __init__(self, name='Number of Sentences', column_name='sentences'):
        super(Sentences, self).__init__(name, column_name)

    def value_for_text(self, t):
        return ilen(t.sentences)


class Paragraphs(base.Metric):
    """
    """
    def __init__(self, name='Number of Paragraphs', column_name='paragraphs'):
        super(Paragraphs, self).__init__(name, column_name)

    def value_for_text(self, t):
        return ilen(t.paragraphs)


class WordsPerSentence(base.Metric):
    """
    """
    def __init__(self, name='Mean words per sentence',
                 column_name='words_per_sentence'):
        super(WordsPerSentence, self).__init__(name, column_name)

    def value_for_text(self, t):
        nwords = map(len, t.words)
        return sum(nwords) / ilen(t.sentences)


class SentencesPerParagraph(base.Metric):
    """
    """
    def __init__(self, name='Mean sentences per paragraph',
                 column_name='sentences_per_paragraph'):
        super(SentencesPerParagraph, self).__init__(name, column_name)

    def value_for_text(self, t):
        return ilen(t.sentences) / ilen(t.paragraphs)


class SyllablesPerContentWord(base.Metric):
    """
    """
    def __init__(self, name='Mean syllables per content word',
                 column_name='syllables_per_content_word'):
        super(SyllablesPerContentWord, self).__init__(name, column_name)

    def value_for_text(self, t):
        content_words = filter(is_content_word, t.all_words)
        syllables = chain(map(syllable_separator.separate, content_words))

        return ilen(syllables) / ilen(content_words)


class VerbIncidence(base.Metric):
    """
    """
    def __init__(self, name='Verb incidence',
                 column_name='verbs'):
        super(VerbIncidence, self).__init__(name, column_name)

    def value_for_text(self, t):
        verbs = filter(is_verb, t.all_words)
        return ilen(verbs) / ilen(t.all_words)


class NounIncidence(base.Metric):
    """
    """
    def __init__(self, name='Noun incidence',
                 column_name='nouns'):
        super(NounIncidence, self).__init__(name, column_name)

    def value_for_text(self, t):
        nouns = filter(is_noun, t.all_words)
        return ilen(nouns) / ilen(t.all_words)


class AdjectiveIncidence(base.Metric):
    """
    """
    def __init__(self, name='Adjective incidence',
                 column_name='adjectives'):
        super(AdjectiveIncidence, self).__init__(name, column_name)

    def value_for_text(self, t):
        adjectives = filter(is_adjective, t.all_words)
        return ilen(adjectives) / ilen(t.all_words)


class AdverbIncidence(base.Metric):
    """
    """
    def __init__(self, name='Adverb incidence',
                 column_name='adverbs'):
        super(AdverbIncidence, self).__init__(name, column_name)

    def value_for_text(self, t):
        adverbs = filter(is_adverb, t.all_words)
        return ilen(adverbs) / ilen(t.all_words)


class PronounIncidence(base.Metric):
    """
    """
    def __init__(self, name='Pronoun incidence',
                 column_name='adverbs'):
        super(PronounIncidence, self).__init__(name, column_name)

    def value_for_text(self, t):
        pronouns = filter(is_pronoun, t.all_words)
        return ilen(pronouns) / ilen(t.all_words)


class ContentWordIncidence(base.Metric):
    """
    """
    def __init__(self, name='Content word incidence',
                 column_name='content_words'):
        super(ContentWordIncidence, self).__init__(name, column_name)

    def value_for_text(self, t):
        content_words = filter(is_content_word, t.all_words)
        return ilen(content_words) / ilen(t.all_words)


class FunctionWordIncidence(base.Metric):
    """
    """
    def __init__(self, name='Content word incidence',
                 column_name='content_words'):
        super(ContentWordIncidence, self).__init__(name, column_name)

    def value_for_text(self, t):
        return 1 - ContentWordIncidence().value_for_text(t)


class BasicCounts(base.Category):

    def __init__(self, name='Basic Counts', table_name='basic_counts'):
        super(BasicCounts, self).__init__(name, table_name)
        self._set_metrics_from_module(__name__, 'BasicCounts')

    def values_for_text(self, t):
        return super().values_for_text(t)
