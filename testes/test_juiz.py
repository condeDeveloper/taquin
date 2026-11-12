"""A paridade: ela preve a mesma coisa que a varredura descobre andando?

O teste grande aqui percorre as 362.880 permutacoes e compara os dois
caminhos. E a prova de que a regra de paridade nao e so uma frase bonita.
"""

import itertools

from taquin.busca import distancias
from taquin.juiz import (
    conta_alcancaveis_pela_formula,
    inversoes,
    linha_do_buraco_de_baixo,
    paridade_alcancavel,
)
from taquin.nucleo import resolvida, vizinhos


def test_inversoes_ignora_o_buraco():
    assert inversoes((1, 2, 3, 4, 5, 6, 7, 8, 0)) == 0
    assert inversoes((0, 1, 2, 3, 4, 5, 6, 7, 8)) == 0
    assert inversoes((2, 1, 3, 4, 5, 6, 7, 8, 0)) == 1
    assert inversoes((8, 7, 6, 5, 4, 3, 2, 1, 0)) == 28


def test_linha_do_buraco_contada_de_baixo():
    assert linha_do_buraco_de_baixo((1, 2, 3, 4, 5, 6, 7, 8, 0), 3) == 1
    assert linha_do_buraco_de_baixo((0, 1, 2, 3, 4, 5, 6, 7, 8), 3) == 3


def test_a_resolvida_e_alcancavel():
    assert paridade_alcancavel(resolvida(), 3)


def test_um_deslize_nao_muda_a_paridade():
    """Se mudasse, a regra nao seria invariante e nao serviria de juiz."""
    a = resolvida()
    for b in vizinhos(a):
        assert paridade_alcancavel(b, 3)
        for c in vizinhos(b):
            assert paridade_alcancavel(c, 3)


def test_a_paridade_reprova_alguma_coisa():
    """Um juiz que aprova tudo nao e juiz. Trocar duas pecas sai do alcance."""
    fora = (2, 1, 3, 4, 5, 6, 7, 8, 0)
    assert not paridade_alcancavel(fora, 3)


def test_formula_e_metade_do_fatorial():
    assert conta_alcancaveis_pela_formula(3, 3) == 181440
    assert conta_alcancaveis_pela_formula(2, 2) == 12


def test_paridade_contra_varredura_nas_362880():
    """Toda permutacao de 9 casas, pelos dois caminhos, zero divergencias."""
    alcancaveis = distancias(3, 3)
    total = 0
    for p in itertools.permutations(range(9)):
        total += 1
        assert paridade_alcancavel(p, 3) == (p in alcancaveis), p
    assert total == 362880
    assert len(alcancaveis) == total // 2
