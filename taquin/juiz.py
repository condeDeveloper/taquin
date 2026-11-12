"""O juiz: decidir se da para resolver SEM mexer em nenhuma peca.

A busca descobre quais posicoes sao alcancaveis andando de verdade, uma
jogada por vez, a partir da resolvida. Este arquivo responde a mesma pergunta
olhando a posicao parada.

O argumento: cada deslize horizontal nao muda nada na leitura linear das
pecas, e cada deslize vertical move uma peca por cima de exatamente
`largura - 1` outras, trocando a paridade do numero de inversoes esse tanto de
vezes. Com largura IMPAR, `largura - 1` e par, entao a paridade das inversoes
nunca muda. Logo so as posicoes com paridade igual a da resolvida sao
alcancaveis -- e a resolvida tem zero inversoes, que e par.

Isso vale para largura impar. Para largura par a conta precisa somar a linha
do buraco, e por isso `paridade_alcancavel` cobra a largura e trata os dois
casos em vez de fingir que a regra e uma so.
"""


def inversoes(estado):
    """Pares fora de ordem na leitura linear, ignorando o buraco."""
    pecas = [v for v in estado if v != 0]
    total = 0
    for i in range(len(pecas)):
        for j in range(i + 1, len(pecas)):
            if pecas[i] > pecas[j]:
                total += 1
    return total


def linha_do_buraco_de_baixo(estado, largura):
    """Quantas linhas o buraco esta acima da ultima, contando de baixo."""
    altura = len(estado) // largura
    y = estado.index(0) // largura
    return altura - y


def paridade_alcancavel(estado, largura):
    """Da para resolver, decidido so pela paridade?

    Largura impar: as inversoes tem que ser pares.
    Largura par: inversoes + linha do buraco contada de baixo tem que ser impar.
    """
    inv = inversoes(estado)
    if largura % 2 == 1:
        return inv % 2 == 0
    return (inv + linha_do_buraco_de_baixo(estado, largura)) % 2 == 1


def conta_alcancaveis_pela_formula(largura, altura):
    """Quantas posicoes a paridade deixa passar: metade do fatorial.

    Calculado, nao digitado: a metade de (l*a)! sai de um produto aqui dentro.
    """
    n = largura * altura
    fat = 1
    for k in range(2, n + 1):
        fat *= k
    return fat // 2
