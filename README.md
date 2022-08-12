# Arrays

> Este programa foi realizado como exercício de programação para a disciplina de Princípios de Desenvolvimentos de Algoritmos (MAC0122) oferecida pela Universidade de São Paulo em 2021, ministrada pelos professores José Coelho de Pina Junior e Carlos Hitoshi Morimoto.

## Descrição do projeto

No arquivo array2d.py foi implementada como exercício a classe Array2d, a fim de representar e manipular matrizes de duas dimensões, além de demonstrar brevemente o uso da biblioteca Numpy.

## Demonstração

Testes da classe Array2d, com o código à esquerda e a saída correspondente à direita.
[img EI09]
<br>

[img EG09]
Testes do método resize().
<br>

[img EI10]
Testes do método reshape(), que trabalha com o conceito de "vista". Quando trabalhamos com estruturas com muitos dados, devemos tomar o cuidado de não “desperdiçar” a memória do computador criando várias cópias da mesma estrutura, e o conceito de vista nos ajuda a mitigar esse problema.

O método copy() retorna uma cópia completa do objeto do tipo Array2d, ou seja, incluindo uma cópia da lista data do objeto. Já o método reshape() recebe uma tupla com uma dimensão (nlin, ncol) e retorna uma vista do objeto do tipo Array2d. A vista se comporta como um objeto Array2d com a nova dimensão, ou seja, com valores diferentes do atributo shape, mas compartilha a mesma lista data.
<br>

[img EG10_1]
Testes do método carregue(), que carrega os dados do Array a partir de uma lista externa.

<br>
[img EG10_2]
Testes do método carregue2(), que diferentemente do anterior, se algum número específico é alterado no Array através do método _setitem_(), a lista de dados em si não se altera.

<br>
[img EI11_1]
Testes dos métodos getlin(), getcol() e dot() da classe Array2d.

<br>
[img EI11_2]
Testes da função matmul(), que retorna o produto matricial entre dois objetos Array2d, e em seguida a mesma operação realizada a partir da biblioteca Numpy.