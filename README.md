# Arrays

> Este programa foi realizado como exercício de programação para a disciplina de Princípios de Desenvolvimentos de Algoritmos (MAC0122) oferecida pela Universidade de São Paulo em 2021, ministrada pelos professores José Coelho de Pina Junior e Carlos Hitoshi Morimoto.

## Descrição do projeto

No arquivo array2d.py foi implementada como exercício a classe Array2d, a fim de representar e manipular matrizes de duas dimensões, além de demonstrar brevemente o uso da biblioteca Numpy.

## Demonstração

<div id="EI09" align="center"> <img src="https://user-images.githubusercontent.com/101532054/184396523-448e9380-8d8c-47f2-aab0-ec525ebd082a.png" width="500px"> <img src="https://user-images.githubusercontent.com/101532054/184396565-383dfc74-2379-445a-9ce4-0acfddc18d20.png" width="500px"> </div>
Testes da classe Array2d, com o código à esquerda e a saída correspondente à direita.
<br>

<br>
<div id="EG09" align="center"> <img src="https://user-images.githubusercontent.com/101532054/184396593-7b8cf215-7550-4867-9711-911470afb939.png" width="500px"> <img src="https://user-images.githubusercontent.com/101532054/184396609-acab9ae8-19a5-47cf-b1a9-a96963d76f51.png" width="500px"> </div>
Testes do método resize().
<br>

<br>
<div id="EI10" align="center"> <img src="https://user-images.githubusercontent.com/101532054/184396639-6aec72e3-d671-488f-b707-a29dd7231038.png" width="500px"> <img src="https://user-images.githubusercontent.com/101532054/184396683-51862694-74be-45d8-aa6d-245b2b020781.png" width="500px"> </div>
Testes do método reshape(), que trabalha com o conceito de "vista". Quando trabalhamos com estruturas com muitos dados, devemos tomar o cuidado de não “desperdiçar” a memória do computador criando várias cópias da mesma estrutura, e o conceito de vista nos ajuda a mitigar esse problema.

O método copy() retorna uma cópia completa do objeto do tipo Array2d, ou seja, incluindo uma cópia da lista data do objeto. Já o método reshape() recebe uma tupla com uma dimensão (nlin, ncol) e retorna uma vista do objeto do tipo Array2d. A vista se comporta como um objeto Array2d com a nova dimensão, ou seja, com valores diferentes do atributo shape, mas compartilha a mesma lista data.
<br>

<br>
<div id="EG10pt1" align="center"> <img src="https://user-images.githubusercontent.com/101532054/184396750-7108cedc-d152-4147-ba15-d4d3efbfd338.png" width="500px"> <img src="https://user-images.githubusercontent.com/101532054/184396784-c20f0144-1efa-4911-8710-20a665ac54fb.png" width="500px"> </div>
Testes do método carregue(), que carrega os dados do Array a partir de uma lista externa.
<br>

<br>
<div id="EG10pt2" align="center"> <img src="https://user-images.githubusercontent.com/101532054/184396808-ff5e6cba-7146-45dc-be86-a5827a7132fc.png" width="500px"> <img src="https://user-images.githubusercontent.com/101532054/184396817-d635b394-1e86-484b-a9f0-ac1870564b20.png" width="500px"> </div>
Testes do método carregue2(), que diferentemente do anterior, se algum número específico é alterado no Array através do método _setitem_(), a lista de dados em si não se altera.
<br>

<br>
<div id="EI11pt1" align="center"> <img src="https://user-images.githubusercontent.com/101532054/184396907-4aa239fd-797e-4f42-8627-0baef516c757.png" width="500px"> <img src="https://user-images.githubusercontent.com/101532054/184396944-273d1385-acfe-4798-9104-c665d520dacd.png" width="500px"> </div>
Testes dos métodos getlin(), getcol() e dot() da classe Array2d.
<br>

<br>
<div id="EI11pt2" align="center"> <img src="https://user-images.githubusercontent.com/101532054/184396965-b3172aa3-8f1d-4174-895a-28748c1e13d0.png" width="500px"> <img src="https://user-images.githubusercontent.com/101532054/184396998-69f8382d-c784-450b-a147-b1671a30b1b7.png" width="500px"> </div>
Testes da função matmul(), que retorna o produto matricial entre dois objetos Array2d, e em seguida a mesma operação realizada a partir da biblioteca Numpy.
