"""O quebra-cabeca deslizante varrido inteiro por largura."""

from .nucleo import resolvida, vizinhos, e_permutacao
from .juiz import inversoes, paridade_alcancavel, conta_alcancaveis_pela_formula
from .busca import distancias, histograma, diametro, mais_distantes

__all__ = ['resolvida', 'vizinhos', 'e_permutacao', 'inversoes',
           'paridade_alcancavel', 'conta_alcancaveis_pela_formula',
           'distancias', 'histograma', 'diametro', 'mais_distantes']
