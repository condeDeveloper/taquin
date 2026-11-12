"""O quebra-cabeca deslizante: estado, vizinhos e nada mais.

A posicao e uma tupla de l*a numeros, lida de cima para baixo e da esquerda
para a direita. O **0 e o buraco**, nao uma peca. Mover uma peca e, na verdade,
trocar o buraco com um vizinho dele -- e pensar assim deixa a geracao de
vizinhos com quatro casos em vez de oito.

A posicao resolvida e (1, 2, ..., n-1, 0): o buraco no canto de baixo a
direita. Essa escolha importa para as tabelas, porque a distancia de toda
posicao e medida ATE ela.
"""

LARGURA = 3
ALTURA = 3


def resolvida(largura=LARGURA, altura=ALTURA):
    n = largura * altura
    return tuple(list(range(1, n)) + [0])


def vizinhos(estado, largura=LARGURA, altura=ALTURA):
    """As posicoes alcancaveis com UM deslize.

    O buraco anda; a peca que estava no destino vem para o lugar dele.
    """
    buraco = estado.index(0)
    y, x = divmod(buraco, largura)
    saida = []
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ny, nx = y + dy, x + dx
        if not (0 <= ny < altura and 0 <= nx < largura):
            continue
        destino = ny * largura + nx
        novo = list(estado)
        novo[buraco], novo[destino] = novo[destino], novo[buraco]
        saida.append(tuple(novo))
    return saida


def aplica(estado, destino, largura=LARGURA):
    """Troca o buraco com a casa `destino`, se forem vizinhas."""
    buraco = estado.index(0)
    if destino not in [i for i in _indices_vizinhos(buraco, largura)]:
        raise ValueError('a casa %d nao e vizinha do buraco' % destino)
    novo = list(estado)
    novo[buraco], novo[destino] = novo[destino], novo[buraco]
    return tuple(novo)


def _indices_vizinhos(i, largura, altura=ALTURA):
    y, x = divmod(i, largura)
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < altura and 0 <= nx < largura:
            yield ny * largura + nx


def e_permutacao(estado, largura=LARGURA, altura=ALTURA):
    """O estado usa cada numero de 0 a n-1 exatamente uma vez?"""
    return sorted(estado) == list(range(largura * altura))
