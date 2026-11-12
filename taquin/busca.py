"""A varredura por largura, a partir da posicao resolvida.

Busca em largura de tras para frente: comeca na resolvida e anda. Toda posicao
visitada recebe a distancia em que foi vista pela primeira vez, e essa
distancia e a MINIMA -- e a propriedade que faz a busca em largura valer aqui
e que uma busca em profundidade nao daria.

O conjunto visitado no fim e exatamente o conjunto das posicoes alcancaveis.
Ninguem disse a ele que sao metade das permutacoes: isso e medido, e o
`juiz.py` preve o mesmo por um caminho que nao anda uma casa sequer.
"""

from collections import deque

from .nucleo import resolvida, vizinhos


def distancias(largura=3, altura=3):
    """Mapa posicao -> distancia ate a resolvida, para tudo que se alcanca."""
    inicio = resolvida(largura, altura)
    visto = {inicio: 0}
    fila = deque([inicio])
    while fila:
        atual = fila.popleft()
        d = visto[atual] + 1
        for v in vizinhos(atual, largura, altura):
            if v not in visto:
                visto[v] = d
                fila.append(v)
    return visto


def histograma(largura=3, altura=3):
    """Quantas posicoes existem a cada distancia.

    Devolve uma lista em que o indice e a distancia.
    """
    visto = distancias(largura, altura)
    maior = max(visto.values())
    saida = [0] * (maior + 1)
    for d in visto.values():
        saida[d] += 1
    return saida


def diametro(largura=3, altura=3):
    """A distancia da posicao mais longe: quantas jogadas o pior caso exige."""
    return max(distancias(largura, altura).values())


def mais_distantes(largura=3, altura=3):
    """As posicoes que realizam o diametro."""
    visto = distancias(largura, altura)
    d = max(visto.values())
    return sorted(e for e, k in visto.items() if k == d)
