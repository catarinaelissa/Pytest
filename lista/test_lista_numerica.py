import pytest

@pytest.fixture
def lista_num ():

    return [1, 2, 3, 4, 5, 6]
def test_soma (lista_num):
    assert sum(lista_num) == 21

def test_maximo (lista_num):
    assert max(lista_num) == 6