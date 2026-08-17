import pytest

def soma (val1: float, val2: float):
    return val1+val2

def test_soma ():

    val1 = 2
    val2 = 4
    sum = 6
    resultado = soma(val1, val2)

    assert resultado == sum