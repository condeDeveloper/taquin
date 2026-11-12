"""A varredura em largura: ela mede distancia MINIMA e alcanca tudo."""

from taquin.busca import diametro, distancias, histograma, mais_distantes
from taquin.nucleo import resolvida, vizinhos


def test_a_resolvida_esta_a_zero():
    d = distancias(3, 3)
    assert d[resolvida()] == 0


def test_distancia_de_vizinho_difere_de_um():
    """Propriedade da busca em largura: vizinhos nunca pulam dois degraus."""
    d = distancias(3, 3)
    for estado, k in list(d.items())[:2000]:
        for v in vizinhos(estado):
            assert abs(d[v] - k) <= 1


def test_toda_distancia_tem_caminho_descendo():
    """De qualquer posicao da para chegar em zero sempre descendo um degrau."""
    d = distancias(3, 3)
    for estado in list(d)[:500]:
        atual, passos = estado, 0
        while d[atual] > 0:
            atual = min(vizinhos(atual), key=lambda v: d[v])
            passos += 1
            assert passos <= 31
        assert passos == d[estado]


def test_tamanho_do_alcance():
    assert len(distancias(3, 3)) == 181440


def test_diametro_e_31():
    assert diametro(3, 3) == 31


def test_so_duas_posicoes_no_diametro():
    extremas = mais_distantes(3, 3)
    assert len(extremas) == 2
    d = distancias(3, 3)
    assert all(d[e] == 31 for e in extremas)


def test_histograma_soma_o_alcance():
    h = histograma(3, 3)
    assert sum(h) == 181440
    assert len(h) == 32
    assert h[0] == 1
    assert h[1] == 2
    assert h[-1] == 2


def test_quadrado_2x2():
    """O 2x2 tambem fecha, e serve de caso pequeno conferivel a mao."""
    d = distancias(2, 2)
    assert len(d) == 12
    assert diametro(2, 2) == 6
