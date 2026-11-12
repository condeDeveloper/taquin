"""As tabelas do README. Nenhum numero do texto nasce fora daqui.

A varredura inteira leva meio segundo, entao nao ha tabela cortada neste
projeto: tudo que o README afirma foi medido no dominio completo.
"""

from functools import lru_cache

from .busca import histograma, mais_distantes
from .juiz import conta_alcancaveis_pela_formula

LARGURA = 3
ALTURA = 3


@lru_cache(maxsize=None)
def resumo(largura=LARGURA, altura=ALTURA):
    """Os numeros de cabeceira: alcancaveis, formula, diametro, quantos nele."""
    h = histograma(largura, altura)
    return {
        'alcancaveis': sum(h),
        'formula': conta_alcancaveis_pela_formula(largura, altura),
        'diametro': len(h) - 1,
        'no_diametro': h[-1],
    }


@lru_cache(maxsize=None)
def tabela_histograma(largura=LARGURA, altura=ALTURA):
    """(distancia, quantas) para toda distancia."""
    return tuple(enumerate(histograma(largura, altura)))


@lru_cache(maxsize=None)
def pico(largura=LARGURA, altura=ALTURA):
    """A distancia com mais posicoes, e quantas sao."""
    h = histograma(largura, altura)
    i = max(range(len(h)), key=lambda k: h[k])
    return i, h[i]


@lru_cache(maxsize=None)
def vales(largura=LARGURA, altura=ALTURA):
    """As distancias que tem MENOS posicoes que as duas vizinhas.

    Um histograma que so sobe e desce nao tem nenhuma. Este tem.
    """
    h = histograma(largura, altura)
    return tuple(i for i in range(1, len(h) - 1) if h[i] < h[i - 1] and h[i] < h[i + 1])


@lru_cache(maxsize=None)
def mediana(largura=LARGURA, altura=ALTURA):
    """A distancia em que se acumula metade das posicoes."""
    h = histograma(largura, altura)
    total = sum(h)
    acumulado = 0
    for i, q in enumerate(h):
        acumulado += q
        if acumulado >= total / 2:
            return i
    raise AssertionError('histograma vazio')


@lru_cache(maxsize=None)
def fracao_a_partir_de(corte, largura=LARGURA, altura=ALTURA):
    """Que fracao das posicoes fica a `corte` jogadas ou mais."""
    h = histograma(largura, altura)
    return sum(h[corte:]) / sum(h)


@lru_cache(maxsize=None)
def extremas(largura=LARGURA, altura=ALTURA):
    """As posicoes que realizam o diametro."""
    return mais_distantes(largura, altura)
