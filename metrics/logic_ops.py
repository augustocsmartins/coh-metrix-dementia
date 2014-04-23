# -*- coding: utf-8 -*-
from coh import base


LOGIC_OPERATORS = [
    'e',
    'ou',
    'se',
    'não',
    'nem',
    'nenhum',
    'nenhuma',
    'nada',
    'nunca',
    'jamais',
    'caso',
    'desde que',
    'contanto que',
    'uma vez que',
    'a menos que',
    'sem que',
    'a não ser que',
    'salvo se',
    'exceto se',
    'então é porque',
    'fosse...fosse',  # TODO: check how to handle this.
    'vai que',
    'va que',
]

NEGATIONS = [
    'não',
    'nem',
    'nenhum',
    'nenhuma',
    'nada',
    'nunca',
    'jamais'
]


class LogicOperatorsIncidence(base.Metric):
    """"""
    def __init__(self, name='Logic operators incidence',
                 column_name='logic_operators'):
        super(LogicOperatorsIncidence, self).__init__(name, column_name)

    def value_for_text(self, t):
        lowercase_words = ' '.join(map(str.lower, t.all_words)) + ' '
        incidences = [lowercase_words.count(op + ' ')
                      for op in LOGIC_OPERATORS]
        return sum(incidences) / len(t.all_words)


class AndIncidence(base.Metric):
    """Docstring for AndIncidence. """
    def __init__(self, name='Incidence of ANDs.', column_name='and_incidence'):
        super(AndIncidence, self).__init__(name, column_name)

    def value_for_text(self, t):
        lowercase_words = ' '.join(map(str.lower, t.all_words)) + ' '
        incidences = [lowercase_words.count('e ')]
        return sum(incidences) / len(t.all_words)


class OrIncidence(base.Metric):
    """Docstring for OrIncidence. """
    def __init__(self, name='Incidence of ORs.', column_name='or_incidence'):
        super(OrIncidence, self).__init__(name, column_name)

    def value_for_text(self, t):
        lowercase_words = ' '.join(map(str.lower, t.all_words)) + ' '
        incidences = [lowercase_words.count('ou ')]
        return sum(incidences) / len(t.all_words)


class IfIncidence(base.Metric):
    """Docstring for IfIncidence. """
    def __init__(self, name='Incidence of IFs.', column_name='if_incidence'):
        super(IfIncidence, self).__init__(name, column_name)

    def value_for_text(self, t):
        lowercase_words = ' '.join(map(str.lower, t.all_words)) + ' '
        incidences = [lowercase_words.count('se ')]
        return sum(incidences) / len(t.all_words)


class NegationIncidence(base.Metric):
    """Docstring for NegationIncidence. """
    def __init__(self, name='Incidence of negations',
                 column_name='negation_incidence'):
        super(NegationIncidence, self).__init__(name, column_name)

    def value_for_text(self, t):
        lowercase_words = ' '.join(map(str.lower, t.all_words)) + ' '
        incidences = [lowercase_words.count(op + ' ') for op in NEGATIONS]
        return sum(incidences) / len(t.all_words)


class LogicOperators(base.Category):

    def __init__(self, name='Logic operators', table_name='logic_operators'):
        super(LogicOperators, self).__init__(name, table_name)
        self._set_metrics_from_module(__name__)
        self.metrics.sort(key=lambda m: m.name)

    def values_for_text(self, t):
        return super(LogicOperators, self).values_for_text(t)
