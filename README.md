# taquin

O quebra-cabeça deslizante 3×3 varrido **inteiro** em Python 3.10+, sem dependência
nenhuma: busca em largura a partir da posição resolvida, e a paridade da permutação como
juiz independente que decide a mesma coisa sem mover uma peça.

## O que é

Oito peças numeradas e um buraco numa grade 3×3. Uma jogada desliza uma peça para o
buraco. A posição resolvida é `1 2 3 / 4 5 6 / 7 8 0`, com o buraco no canto de baixo à
direita, e a **distância** de uma posição é o menor número de jogadas até ela.

Metade das permutações não é alcançável. A varredura descobre isso andando; o juiz prevê
pela contagem de inversões.

## Os quatro achados

- **A varredura alcança 181.440 posições, e a paridade acerta as 362.880.** Para toda
  permutação das nove casas, a regra de inversões e a busca concordam: **zero divergências**
  em 362.880 conferências. Metade exata do fatorial, medida e prevista pelos dois caminhos.
- **O diâmetro é 31 jogadas, e só duas posições o realizam.** Duas em 181.440 — uma em
  noventa mil. O pior caso do quebra-cabeça é quase um acidente.
- **O histograma tem exatamente um vale, e o pico vem logo depois dele.** A contagem sobe
  até 23.952 na distância 22, **cai para 20.224 na 23**, e volta ao máximo de 24.047 na 24.
  Varrendo as 31 distâncias, a 23 é a **única** que tem menos posições que as duas vizinhas.
- **O embaralhamento típico já é quase o pior caso.** A mediana é 22 jogadas e **60,4%**
  das posições (109.528 de 181.440) estão a 22 ou mais. A dificuldade não mora na cauda.

## Cabeceira

| medida | valor |
|---|---|
| posições alcançáveis (varredura) | 181.440 |
| metade de 9! (paridade) | 181.440 |
| diâmetro | 31 |
| posições no diâmetro | 2 |

## O histograma inteiro

| distância | posições | | distância | posições |
|---|---|---|---|---|
| 0 | 1 | | 16 | 4.485 |
| 1 | 2 | | 17 | 5.638 |
| 2 | 4 | | 18 | 9.529 |
| 3 | 8 | | 19 | 10.878 |
| 4 | 16 | | 20 | 16.993 |
| 5 | 20 | | 21 | 17.110 |
| 6 | 39 | | 22 | 23.952 |
| 7 | 62 | | 23 | **20.224** |
| 8 | 116 | | 24 | **24.047** |
| 9 | 152 | | 25 | 15.578 |
| 10 | 286 | | 26 | 14.560 |
| 11 | 396 | | 27 | 6.274 |
| 12 | 748 | | 28 | 3.910 |
| 13 | 1.024 | | 29 | 760 |
| 14 | 1.893 | | 30 | 221 |
| 15 | 2.512 | | 31 | 2 |

As quatro primeiras linhas dobram (1, 2, 4, 8, 16) porque nos primeiros passos quase todo
vizinho é novo. O dobro morre na distância 5, onde 16 viram 20 e não 32: a partir dali a
busca começa a reencontrar posições que já viu.

## O juiz

A busca descobre o alcance **andando**. O juiz decide olhando a posição parada, pelo
número de inversões na leitura linear das peças.

O argumento: um deslize horizontal não muda nada na leitura linear; um deslize vertical
passa uma peça por cima de exatamente `largura - 1` outras. Com largura ímpar, `largura - 1`
é par, então a paridade das inversões **nunca muda**. A resolvida tem zero inversões, que é
par, logo só as posições com inversões pares são alcançáveis.

A função cobra a largura e trata os dois casos em vez de fingir que a regra é uma só: para
largura par é a soma das inversões com a linha do buraco contada de baixo que precisa ser
ímpar.

A bateria também tem um caso que o juiz **tem que reprovar** — trocar duas peças de lugar
sai do alcance. Sem ele, "concordam em 362.880 casos" não significaria nada.

## Os tabuleiros menores

Conferíveis quase à mão, e servem de piso de sanidade para a varredura grande.

| tabuleiro | alcançáveis | diâmetro |
|---|---|---|
| 2×2 | 12 | 6 |
| 3×2 | 360 | 21 |
| 3×3 | 181.440 | 31 |

O histograma do 2×2 é `1, 2, 2, 2, 2, 2, 1` — um ciclo, que é exatamente o que o 2×2 é: as
três peças só giram.

## O que as medidas me corrigiram

- **Eu esperava um histograma que sobe e desce, e só.** Ele tem um vale: a distância 23 tem
  3.728 posições a menos que a 22 e 3.823 a menos que a 24. Varri as 31 distâncias
  procurando outros vales e **não há nenhum** — é um buraco único, não ruído de uma curva
  acidentada. Virou o terceiro achado.
- **Eu esperava o pico na mediana.** A mediana é 22 e o pico é 24. São medidas diferentes e
  eu as tratei como se fossem a mesma.
- **Eu escrevi `diametro(2, 2) == 6` no teste antes de medir.** O valor estava certo, mas
  isso foi sorte: era um número derivado entrando no arquivo que existe justamente para
  impedir chute. Medi depois, e passou a valer por medida.
- **O caminho do script quebrou a varredura duas vezes.** `/c/Projetos/...` é caminho do
  Git Bash e o Python do Windows não o resolve. O erro foi `ModuleNotFoundError` num
  módulo que existia o tempo todo.

## Rodar

```bash
pip install -e ".[dev]"
pytest                          # a bateria inteira
python -m taquin                # tudo
python -m taquin histograma     # só o histograma, com barras
python -m taquin extremos       # as duas posições mais distantes
python ferramentas/medidor.py   # as tabelas em markdown
```

## Mapa

| arquivo | o que faz |
|---|---|
| `taquin/nucleo.py` | estado, vizinhos, nada mais |
| `taquin/juiz.py` | a paridade, que decide sem mover peça |
| `taquin/busca.py` | a busca em largura, que mede distância mínima |
| `taquin/medidas.py` | as tabelas do README |
| `testes/test_juiz.py` | as 362.880 conferências |
| `testes/test_medidas.py` | os números acima, presos |

30 testes. MIT.
