"""Linha de comando.

    python -m taquin              tudo
    python -m taquin histograma   so o histograma
"""

import sys

from .medidas import (
    extremas,
    fracao_a_partir_de,
    mediana,
    pico,
    resumo,
    tabela_histograma,
    vales,
)


def cabecalho():
    r = resumo()
    print('posicoes alcancadas pela varredura: %d' % r['alcancaveis'])
    print('a paridade preve (metade do fatorial): %d  %s'
          % (r['formula'], 'bate' if r['formula'] == r['alcancaveis'] else 'DIVERGE'))
    print('diametro: %d jogadas, realizado por %d posicoes'
          % (r['diametro'], r['no_diametro']))
    print()


def histo():
    d, q = pico()
    print('histograma de distancias (pico em %d, com %d posicoes)' % (d, q))
    for distancia, quantas in tabela_histograma():
        barra = '#' * max(1, quantas * 50 // q) if quantas else ''
        print('   %2d  %6d  %s' % (distancia, quantas, barra))
    print()
    print('vales locais (menos que as duas vizinhas): %s'
          % (', '.join(str(v) for v in vales()) or 'nenhum'))
    print('mediana: %d jogadas' % mediana())
    print('a %d jogadas ou mais: %.1f%%' % (mediana(), 100 * fracao_a_partir_de(mediana())))
    print()


def extremos():
    print('as posicoes mais longe de todas (0 e o buraco):')
    for e in extremas():
        for y in range(3):
            print('   ' + ' '.join(str(v) for v in e[y * 3:y * 3 + 3]))
        print()


def main():
    alvo = sys.argv[1] if len(sys.argv) > 1 else 'tudo'
    if alvo in ('tudo', 'resumo'):
        cabecalho()
    if alvo in ('tudo', 'histograma'):
        histo()
    if alvo in ('tudo', 'extremos'):
        extremos()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
