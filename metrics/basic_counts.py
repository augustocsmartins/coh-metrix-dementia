from .. import base


class Flesch(base.Metric):
    def __init__(self, name='Flesch index', column_name='flesch'):
        super(Flesch, self).__init__(name, column_name)

    def value_for_text(self, t):
        return super().value_for_text(t)


class Words(base.Metric):
    def __init__(self, name='Number of Words', column_name='words'):
        super(Words, self).__init__(name, column_name)

    def value_for_text(self, t):
        return super().value_for_text(t)


#class Sentences(base.Metric):
#    def value_for_text(self, t):
#        return super().value_for_text(t)
#
#
#class Paragraphs(base.Metric):
#    def value_for_text(self, t):
#        return super().value_for_text(t)
#
#
#class WordsPerSentence(base.Metric):
#    def value_for_text(self, t):
#        return super().value_for_text(t)
#
#
#class SentencesPerParagraph(base.Metric):
#    def value_for_text(self, t):
#        return super().value_for_text(t)
#
#
#class SyllablesPerContentWord(base.Metric):
#    def value_for_text(self, t):
#        return super().value_for_text(t)
#
#
#class Verbs(base.Metric):
#    def value_for_text(self, t):
#        return super().value_for_text(t)
#
#
#class Nouns(base.Metric):
#    def value_for_text(self, t):
#        return super().value_for_text(t)
#
#
#class Adjectives(base.Metric):
#    def value_for_text(self, t):
#        return super().value_for_text(t)
#
#
#class Adverbs(base.Metric):
#    def value_for_text(self, t):
#        return super().value_for_text(t)
#
#
#class Pronouns(base.Metric):
#    def value_for_text(self, t):
#        return super().value_for_text(t)
#
#
#class ContentWords(base.Metric):
#    def value_for_text(self, t):
#        return super().value_for_text(t)
#
#
#class FunctionWords(base.Metric):
#    def value_for_text(self, t):
#        return super().value_for_text(t)


class BasicCounts(base.Category):

    def __init__(self, name='Basic Counts', table_name='basic_counts'):
        super(BasicCounts, self).__init__(name, table_name)
        metrics = self._set_metrics_from_module(__name__, 'BasicCounts')

    def values_for_text(self, t):
        return super().values_for_text(t)
