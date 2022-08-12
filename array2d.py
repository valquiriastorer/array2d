# -*- coding: utf-8 -*-

## ==================================================================

def main():

    #EI09
    print("Testes da classe Array2d\n")
    
    a = Array2d( (2,3), 3) # cria Array2d com valor inicial 3
    print('teste 1: Criação do Array2d a:')
    print(a)
    print(f'shape: {a.shape}')
    print(f'size : {a.size}')
    print(f'data : {a.data}')
    print()

    b = Array2d( (2,3), 1.7)   # criar Array2d com valor inicial 1.7
    print('teste 2: Criação do Array2d b:')
    print(b)
    print(f'shape: {b.shape}')
    print(f'size : {b.size}')
    print(f'data : {b.data}')
    print()

    print(f'teste 3: a[0,1] + 100 é: {a[0,1] + 100}') # acesso direto usando tupla: use o método __getitem__
    print()

    a[1,1] = -1    # atribuição usando tupla: use o método __setitem__
    print('teste 4: Array2d a:')
    print(a)

    #EG09: resize()     
    c = Array2d( (2,3), 3) # cria Array2d com valor inicial 3
    print(f'\nteste 5: Criação do Array2d c:')
    c[0,0] = 1
    c[0,1] = 2
    c[1,1] = 4
    c[1,2] = 5
    print(c)
    print(f'shape: {c.shape}')
    print(f'size : {c.size}')
    print(f'data : {c.data}')
    print()
    
    c.resize( (3,2) )
    print(f'teste 6: Novo c depois de resize:')
    print(c)
    print(f'shape: {c.shape}')
    print(f'size : {c.size}')
    print(f'data : {c.data}')
    
    #EI10: reshape() e copy()
    print('\n======= Teste dos métodos reshape() e copy():')
    a = Array2d( (1,6), 3) # cria Array2d com valor inicial 3
    print(f'teste 7: Criação do Array2d a:')
    print(a)
    print()

    b = a.reshape( (2,3) )   
    print(f'teste 8: reshape cria uma vista de a:')
    print(b)
    print()
    
    print(f'teste 9: mudanças em b devem resultar em mudanças em a:')
    b[1, 2] = 100
    print(a)
    print(b)
    print()

    print(f'teste 10: e vice-versa - mudanças em a devem resultar em mudanças em b:')
    a[0, 2] = -1 
    print(a)
    print(b)
    print()

    print(f'teste 11: copy cria um clone')
    a = Array2d( (1,6), 3) # cria Array2d com valor inicial 3
    c = a.copy()
    print(f'a: {a}')
    print(f'c: {c}')
    print()

    print(f'teste 12: mudanças em objeto um não devem refletir no outro')
    a[0,1] = 99
    c[0,5] = -1
    print(f'a: {a}')
    print(f'c: {c}')
    print()
    
    #EG10
    print("\n=========== Teste dos métodos carregue() e carregue2():")
    lista = [1,2,3,4,5,6]
    a = Array2d( (2,3), 0)
    print(f'teste 13: carregue() \na:\n{a}\n')
    
    a.carregue( lista )
    print(f'a:\n{a}\n')
    
    a[1,1] = -1
    print(f'a:\n{a}\n')
    print(f'lista: {lista}')
    
    lista = [1,2,3,4,5,6]
    a = Array2d( (2,3), 0)
    print(f'teste 14: carregue2() \na:\n{a}\n')
    
    a.carregue2( lista )
    print(f'a:\n{a}\n')
    
    a[1,1] = -1
    print(f'a:\n{a}\n')
    print(f'lista: {lista}')
    
    #EI11 getlin(), getcol(), dot()
    
    print("\n========= Testes dos métodos getlin, getcol e dot da classe Array2d\n")

    lista_a = [1, 2, 3, 4, 5, 6]
    lista_b = [0, 1, 1, 0, 0, 1]
    tam_a = len(lista_a)
    tam_b = len(lista_b)

    a = Array2d( (1, tam_a), 0) # cria Array2d com valor inicial 0
    print(f'Criação do Array2d a:')
    print(a)
    print()
    a.data = lista_a   ## ou a.carregue(lista_a)
    a.resize( (2,3) )
    print(f'a:\n{a}\n')

    b = Array2d( (1, tam_b), 0)
    b.data = lista_b   # ou b.carregue(lista_b)
    b.resize( (3,2) )
    print(f'b:\n{b}\n')

    linha = a.getlin(0)
    print(f'teste 15: linha a.getlin(0)\n{linha}\n')

    coluna = b.getcol(1)
    print(f'teste 16: coluna b.getcol(1)\n{coluna}\n')

    print(f'teste 17: linha.dot(coluna)\n{linha.dot(coluna)}\n')

    print(f'============ Teste para comparação: função matmul() e Numpy:\n')    

    print(f'teste 18: matmul(a,b)\n{matmul(a,b)}\n')

    ### agora com Numpy
    import numpy as np
    npa = np.array( lista_a ).reshape((2,3))
    print(f'teste 19: Numpy')
    print(f'npa:\n{npa}\n')

    npb = np.array( lista_b ).reshape((3,2))
    print(f'npb:\n{npb}\n')

    print(f'np.matmul(npa, npb):\n{np.matmul(npa, npb)}\n')
    print('ao invés de np.matmul podemos usar @:')
    print(f'npa @ npb:\n{npa @ npb}\n')


## ==================================================================
#   A classe Array2d permite a manipulação de 'matrizes' de duas 
#   dimensões. O exercício é utilizar uma lista linear, ao invés
#   de uma lista aninhada, para armazenar os dados da matriz 
#   internamente.
#   A lista linear deve ser um atributo de nome 'data'.

class Array2d:

    # ---------------------------------------------------------------
    def __init__(self, shape, val):
        ''' (Array2d, tuple, obj) -> None
        Constrói um objeto do tipo Array2d com os atributos:
        data : lista onde os valores são armazenados
        shape: tupla que armazena as dimensões da matriz
        size : número total de elementos da matriz
        '''
        self.data = shape[1]*shape[0]*[val]
        self.size = shape[1]*shape[0]
        self.shape = shape

    # ---------------------------------------------------------------
    def __getitem__(self, key):
        ''' (Array2d, tupla) -> obj
        recebe uma tupla key contendo a posição (lin, col)
        e retorna o item nessa posição do Array2d self.

        Esse método é usado quando o objeto é chamado com 
        uma tupla entre colchetes, como self[0,0]. 
        Exemplo:
        >>> a = Array2d( (2,3), -1)
        >>> a[1,1] + 100
        99
        >>> print( a[1,1] )
        -1
        '''
        lin = key[0]
        col = key[1]
        posição = self.data[self.shape[1] * lin + col]
        return posição

    # ---------------------------------------------------------------
    def __setitem__(self, key, valor):
        ''' (Array2d, tupla, obj) -> None
        recebe uma tupla key contendo a posição (lin, col)
        e um objeto valor e armazena o valor nessa posição
        do Array2d self.

        Esse método é usado para atribuir 'valor' na posição
        indicada pela tupla `key`, como self[0,0] = 0. 
        Exemplo:
        >>> a = Array2d( (2,3), -1)
        >>> print( a[1,1] )
        -1
        >>> a[1,1] = 100
        >>> print( a[1,1] )
        100
        '''
        lin = key[0]
        col = key[1]
        self.data[self.shape[1] * lin + col] = valor

    # ---------------------------------------------------------------
    def __str__(self):
        ''' (Array2d) -> None
        ao ser usada pela função print, deve exibir cada linha
        do Array2d em uma linha separada, separando seus elementos por um espaço.

        Exemplo: para self.data = [1, 2, 3, 4, 5, 6] e self.shape = (2,3)
        o método deve retornar a string 
        "1 2 3\n4 5 6" 
        e, caso self.shape = (3,2) o método deve retornar a string
        "1 2\n3 4\n5 6" 
        '''
        lin = self.shape[0]
        col = self.shape[1]
        data = self.data
        ini = 0
        fim = col
        s = ''
        linha = []
        
        for x in range(0, lin):
            for i in range(ini, fim):
                linha += [data[i]]
            
            for j in range(len(linha)):
                s += f'{linha[j]} '
            s = s.strip() + '\n'
            if x == 0:
                ini = j+1
            else:
                ini += col
            fim += col
            linha = []

        return s.strip()
    # ---------------------------------------------------------------
    def resize(self, reshape):
        '''(Array2d, tuple) -> None
        Recebe uma tupla e altera a dimensão do Array2d.
        '''

        self.shape = reshape
    # ---------------------------------------------------------------
    def copy(self):
        ''' (Array2d)-> Array2d
        Recebe um objeto do tipo Array2d e retorna uma cópia do mesmo.
        '''
        copy = Array2d(self.shape, 0)
        copy.data = self.data[:]
        return copy
    # ---------------------------------------------------------------
    def reshape(self,  dimensões):
        '''(Array2d, tuple)-> Array2d
        Recebe uma tupla com o número de linhas e de colunas, respectivamente,
        e retorna uma vista do objeto do tipo Array2d.
        
        Ou seja, uma nova configuração do objeto Array2d recebido
        com as dimensões definidas pela tupla.
        '''
        reshape = Array2d(dimensões, 0)
        reshape.data = self.data
        return reshape
    # ---------------------------------------------------------------
    def carregue(self, nova_lista):
        '''
        recebe uma lista do mesmo tamanho de self.size e carrega a lista 
        self.data com o conteúdo de nova_lista
        '''
        
        self.data = nova_lista
    # ---------------------------------------------------------------        
    def carregue2(self, nova_lista):
        '''
        recebe uma lista do mesmo tamanho de self.size e carrega a lista 
        self.data com o conteúdo de nova_lista
        '''
        self.data = nova_lista [:]
    # ---------------------------------------------------------------        
    def getlin(self, lin):
        '''(Array2d, int)-> Array2d
        Recebe um Array2d self e um inteiro lin,
        retorna um Array2d formado pela a linha de índice lin de self.
        '''
        ncols = self.shape[1]
        linha = Array2d((1, ncols), None)
        dados = []
        for i in range(0, ncols):
            dados += [self.data[ncols*lin + i]]
        linha.data = dados
        return linha
        
    # ---------------------------------------------------------------
    def getcol(self, col):
        '''(Array2d, int)-> Array2d
        Recebe um Array2d self e um inteiro col,
        retorna um Array2d formado pela coluna de índice col de self.
        '''
        nlins = self.shape[0]
        coluna = Array2d((nlins, 1), None)
        dados = []
        for i in range(0, nlins):
            dados += [self[i, col]]
        coluna.data = dados
        return coluna
    # ---------------------------------------------------------------
    def dot(self, other):
        '''(Array2d, Array2d)-> int
        Recebe um Array2d self e outro Array2d other com o mesmo número de elementos,
        e retorna um número (escalar) resultante do produto termo a termo
        entre self e other.
        '''
        dot = 0
        for i in range(0, self.size):
            mul = self.data[i] * other.data[i]
            dot += mul
        return dot
# ---------------------------------------------------------------
def matmul( esq, dir ):
    '''(Array2d, Array2d) -> Array2d
    Recebe um Array2d esq de dimensão (m, n) e outro Array2d dir de dimensão (n, p)
    e retorna o produto matricial entre esq e dir, que deve ser outro Array2d
    de dimensão (m, p).
    '''
    m = esq.shape[0]
    p = dir.shape[1]
    mul = Array2d((m, p), None)
    for i in range(0, m): #linhas da esq
        for j in range(0,p): #coluna da dir
            mul[i, j] =  esq.getlin(i).dot(dir.getcol(j))

    return mul
        
## ==================================================================

if __name__ == '__main__':
    main()