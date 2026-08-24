import pytest
from calculadora import somar, subtracao

@pytest.fixture
def dados_basicos():
    lista_num = [1, 2, 3, 4, 5, 6]
    return lista_num

def test_soma(dados_basicos):
    assert sum(dados_basicos) == 21

def test_maximo(dados_basicos):
    assert max(dados_basicos) == 6

def test_par(dados_basicos):
    for numero in dados_basicos:
        if numero % 2 == 0:
            assert numero % 2 == 0 
        else:
            assert numero % 2 != 0 
@pytest.mark.skip(reason="Não quero buscar o número na lista")

def test_busca (dados_basicos):
    assert 4 in dados_basicos

@pytest.mark.parametrize("a, b, operador, esperado", [
    (2, 4, "soma", 6),
    (2, 4, "subtracao", -2),
    (4, 4, "soma", 8),
    (4, 2, "subtracao", 2),

])
def test_operacoes_calculadora(a, b, operador, esperado):
    if operador == "soma":
        assert somar(a, b) == esperado
    elif operador == "subtracao":
        assert subtracao(a, b) == esperado
