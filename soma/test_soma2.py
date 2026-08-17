import pytest
from soma import*

'''A parametrização de testes no pytest permite que você execute o mesmo teste múltiplas vezes com diferentes
conjuntos de dados. Em vez de escrever vários testes semelhantes, você pode usar a parametrização para
testar uma função com diversas entradas, aumentando a cobertura de testes e reduzindo a repetição de
código.'''
@pytest.mark.parametrize("val1, val2, sum", [ (1,2,3),(1,5,9),(10,20,30) ] )

@pytest.mark.skip(reason= "Não testar agora")
def test_soma (val1, val2, sum):

    assert soma (val1, val2) == sum