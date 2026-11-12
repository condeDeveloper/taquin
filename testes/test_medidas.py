"""Os numeros do README, presos.

Todos sairam do programa antes de entrar aqui -- inclusive os que "so"
continuam um padrao, como o diametro do 2x2.
"""

from taquin.busca import diametro, distancias, histograma
from taquin.medidas import (
    extremas,
    fracao_a_partir_de,
    mediana,
    pico,
    resumo,
    tabela_histograma,
    vales,
)

HISTOGRAMA = [1, 2, 4, 8, 16, 20, 39, 62, 116, 152, 286, 396, 748, 1024,
              1893, 2512, 4485, 5638, 9529, 10878, 16993, 17110, 23952,
              20224, 24047, 15578, 14560, 6274, 3910, 760, 221, 2]

EXTREMAS = [(6, 4, 7, 8, 5, 0, 3, 2, 1), (8, 6, 7, 2, 5, 4, 3, 0, 1)]


def test_resumo():
    r = resumo()
    assert r['alcancaveis'] == 181440
    assert r['formula'] == 181440
    assert r['diametro'] == 31
    assert r['no_diametro'] == 2


def test_a_varredura_e_a_formula_dao_o_mesmo():
    r = resumo()
    assert r['alcancaveis'] == r['formula']


def test_histograma_inteiro():
    assert [q for _, q in tabela_histograma()] == HISTOGRAMA
    assert sum(HISTOGRAMA) == 181440


def test_pico_vem_depois_do_vale():
    """O maximo do histograma nao e no meio: e em 24, logo apos a queda."""
    d, q = pico()
    assert (d, q) == (24, 24047)
    assert vales() == (23,)
    assert d > vales()[0]


def test_o_vale_e_unico_em_todo_o_histograma():
    h = histograma(3, 3)
    encontrados = [i for i in range(1, len(h) - 1) if h[i] < h[i - 1] and h[i] < h[i + 1]]
    assert encontrados == [23]
    assert h[23] == 20224
    assert h[22] == 23952
    assert h[24] == 24047


def test_mediana_e_a_fracao_dificil():
    assert mediana() == 22
    f = fracao_a_partir_de(22)
    assert 0.603 < f < 0.604
    # Em numero redondo: 109.528 das 181.440.
    assert sum(HISTOGRAMA[22:]) == 109528


def test_extremas():
    assert extremas() == EXTREMAS
    d = distancias(3, 3)
    for e in EXTREMAS:
        assert d[e] == 31


def test_os_tabuleiros_menores_fecham_tambem():
    assert (len(distancias(2, 2)), diametro(2, 2)) == (12, 6)
    assert histograma(2, 2) == [1, 2, 2, 2, 2, 2, 1]
    assert (len(distancias(3, 2)), diametro(3, 2)) == (360, 21)
