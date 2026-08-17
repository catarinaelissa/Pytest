import pytest

def num_par (num: float):
    return num % 2 == 0

@pytest.mark.parametrize("entrada, esperado",
                        [
                            (2, True),
                            (3, False),
                            (0, True),
                            (-2, True),
                            (-3, False)
                        ])
def test_num_par (entrada, esperado):
    assert num_par(entrada) == esperado

