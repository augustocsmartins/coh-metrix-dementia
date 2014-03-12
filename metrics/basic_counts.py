from coh import base
from coh.utils import ilen
from coh.tools import syllable_separator, pos_tagger
from itertools import chain, filterfalse


class Flesch(base.Metric):
    """
    """
    def __init__(self, name='Flesch index', column_name='flesch'):
        super(Flesch, self).__init__(name, column_name)

    def value_for_text(self, t):
        mean_words_per_sentence = WordsPerSentence().value_for_text(t)

        syllables = chain.from_iterable(
            map(syllable_separator.separate, t.all_words))
        mean_syllables_per_word = ilen(syllables) / ilen(t.all_words)

        flesch = 164.835 - 1.015 * mean_words_per_sentence\
            - 84.6 * mean_syllables_per_word

        return flesch


class Words(base.Metric):
    """
    """
    def __init__(self, name='Number of Words', column_name='words'):
        super(Words, self).__init__(name, column_name)

    def value_for_text(self, t):
        return ilen(filterfalse(pos_tagger.tagset.is_punctuation,
                                t.tagged_words))


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
        return Words().value_for_text(t) / Sentences().value_for_text(t)


class SentencesPerParagraph(base.Metric):
    """
    """
    def __init__(self, name='Mean sentences per paragraph',
                 column_name='sentences_per_paragraph'):
        super(SentencesPerParagraph, self).__init__(name, column_name)

    def value_for_text(self, t):
        return Sentences().value_for_text(t) / Paragraphs().value_for_text(t)


class SyllablesPerContentWord(base.Metric):
    """
    """
    def __init__(self, name='Mean syllables per content word',
                 column_name='syllables_per_content_word'):
        super(SyllablesPerContentWord, self).__init__(name, column_name)

    def value_for_text(self, t):
        content_tokens = filter(pos_tagger.tagset.is_content_word,
                                t.tagged_words)
        content_words = map(lambda t: t[0], content_tokens)

        syllables = map(syllable_separator.separate, content_words)

        nwords = 0
        nsyllables = 0
        for w in syllables:
            nwords += 1
            nsyllables += len(w)

        return nsyllables / nwords


class VerbIncidence(base.Metric):
    """
    """
    def __init__(self, name='Verb incidence',
                 column_name='verbs'):
        super(VerbIncidence, self).__init__(name, column_name)

    def value_for_text(self, t):
        verbs = filter(pos_tagger.tagset.is_verb, t.tagged_words)
        return ilen(verbs) / ilen(t.all_words)


class NounIncidence(base.Metric):
    """
    """
    def __init__(self, name='Noun incidence',
                 column_name='nouns'):
        super(NounIncidence, self).__init__(name, column_name)

    def value_for_text(self, t):
        nouns = filter(pos_tagger.tagset.is_noun, t.tagged_words)
        return ilen(nouns) / ilen(t.all_words)


class AdjectiveIncidence(base.Metric):
    """
    """
    def __init__(self, name='Adjective incidence',
                 column_name='adjectives'):
        super(AdjectiveIncidence, self).__init__(name, column_name)

    def value_for_text(self, t):
        adjectives = filter(pos_tagger.tagset.is_adjective, t.tagged_words)
        return ilen(adjectives) / ilen(t.all_words)


class AdverbIncidence(base.Metric):
    """
    """
    def __init__(self, name='Adverb incidence',
                 column_name='adverbs'):
        super(AdverbIncidence, self).__init__(name, column_name)

    def value_for_text(self, t):
        adverbs = filter(pos_tagger.tagset.is_adverb, t.tagged_words)
        return ilen(adverbs) / ilen(t.all_words)


class PronounIncidence(base.Metric):
    """
    """
    def __init__(self, name='Pronoun incidence',
                 column_name='pronouns'):
        super(PronounIncidence, self).__init__(name, column_name)

    def value_for_text(self, t):
        pronouns = filter(pos_tagger.tagset.is_pronoun, t.tagged_words)
        return ilen(pronouns) / ilen(t.all_words)


class ContentWordIncidence(base.Metric):
    """
    """
    def __init__(self, name='Content word incidence',
                 column_name='content_words'):
        super(ContentWordIncidence, self).__init__(name, column_name)

    def value_for_text(self, t):
        content_words = filter(pos_tagger.tagset.is_content_word,
                               t.tagged_words)
        return ilen(content_words) / ilen(t.all_words)


class FunctionWordIncidence(base.Metric):
    """
    """
    def __init__(self, name='Function word incidence',
                 column_name='function_words'):
        super(FunctionWordIncidence, self).__init__(name, column_name)

    def value_for_text(self, t):
        function_words = filter(pos_tagger.tagset.is_function_word,
                                t.tagged_words)
        return ilen(function_words) / ilen(t.all_words)


class BasicCounts(base.Category):

    def __init__(self, name='Basic Counts', table_name='basic_counts'):
        super(BasicCounts, self).__init__(name, table_name)
        self._set_metrics_from_module(__name__)
        self.metrics.sort(key=lambda m: m.name)

    def values_for_text(self, t):
        return super(BasicCounts, self).values_for_text(t)
