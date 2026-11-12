"""Estado e vizinhos: o basico, antes de qualquer tabela."""

import pytest

from taquin.nucleo import aplica, e_permutacao, resolvida, vizinhos


def test_resolvida_poe_o_buraco_no_fim():
    assert resolvida(3, 3) == (1, 2, 3, 4, 5, 6, 7, 8, 0)
    assert resolvida(2, 2) == (1, 2, 3, 0)


def test_quantos_vizinhos_por_posicao_do_buraco():
    """Canto tem 2, borda tem 3, centro tem 4."""
    canto = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    assert len(vizinhos(canto)) == 2
    borda = (1, 2, 3, 4, 5, 6, 7, 0, 8)
    assert len(vizinhos(borda)) == 3
    centro = (1, 2, 3, 4, 0, 6, 7, 8, 5)
    assert len(vizinhos(centro)) == 4


def test_vizinho_e_reciproco():
    """Se B esta a um passo de A, A esta a um passo de B."""
    a = (1, 2, 3, 4, 0, 6, 7, 8, 5)
    for b in vizinhos(a):
        assert a in vizinhos(b)


def test_vizinhos_continuam_permutacao():
    a = resolvida()
    for b in vizinhos(a):
        assert e_permutacao(b)
        assert sorted(b) == list(range(9))


def test_vizinhos_mexem_uma_casa_so():
    a = resolvida()
    for b in vizinhos(a):
        diferentes = [i for i in range(9) if a[i] != b[i]]
        assert len(diferentes) == 2
        assert 0 in (a[diferentes[0]], a[diferentes[1]])


def test_aplica_recusa_casa_que_nao_e_vizinha():
    a = resolvida()
    with pytest.raises(ValueError):
        aplica(a, 0)


def test_e_permutacao():
    assert e_permutacao(resolvida())
    assert not e_permutacao((1, 1, 2, 3, 4, 5, 6, 7, 8))
