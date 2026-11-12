"""Medidor: as tabelas do README em markdown, prontas para colar.

    python ferramentas/medidor.py
"""

import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from taquin.medidas import (  # noqa: E402
    extremas,
    fracao_a_partir_de,
    mediana,
    pico,
    resumo,
    tabela_histograma,
    vales,
)


def main():
    t0 = time.time()
    r = resumo()

    print('## Cabeceira')
    print()
    print('| medida | valor |')
    print('|---|---|')
    print('| posicoes alcancaveis (varredura) | %d |' % r['alcancaveis'])
    print('| metade de 9! (paridade) | %d |' % r['formula'])
    print('| diametro | %d |' % r['diametro'])
    print('| posicoes no diametro | %d |' % r['no_diametro'])

    d, q = pico()
    print()
    print('## Histograma')
    print()
    print('| distancia | posicoes |')
    print('|---|---|')
    for distancia, quantas in tabela_histograma():
        print('| %d | %d |' % (distancia, quantas))

    print()
    print('pico: distancia %d, com %d posicoes' % (d, q))
    print('vales locais: %s' % (', '.join(str(v) for v in vales()) or 'nenhum'))
    print('mediana: %d' % mediana())
    print('a %d ou mais: %.1f%%' % (mediana(), 100 * fracao_a_partir_de(mediana())))
    print('posicoes extremas: %s' % (extremas(),))
    print()
    print('medido em %.1f s' % (time.time() - t0))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
