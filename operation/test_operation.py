import pytest
def operation (a, b, operador):
    if operador == "soma":
        return a + b
    elif operador == "subtracao":
        return a - b
    elif operador == "multiplicacao":
        return a * b
    elif operador == "divisao":
        return a / b
    else:
     raise ValueError("Operador Inválido")

@pytest.mark.parametrize("a, b, operador, esperado",
                         [
                            (2, 4, "soma", 6),
                            (2, 4, "subtracao", -2),
                            (2, 4, "multiplicacao", 8),
                            (8, 2, "divisao", 4),
                            (5, 0, "divisao", ZeroDivisionError)
                         ])
def test_operation (a, b, operador, esperado):
    if esperado == ZeroDivisionError:
        with pytest.raises(ZeroDivisionError):
            operation(a, b, operador)
    else:
        assert operation(a, b, operador) == esperado