import pytest
from soma import*

@pytest.mark.parametrize("val1, val2, sum", [ (1,2,3),(1,5,9),(10,20,30) ] )


def test_soma (val1, val2, sum):

    assert soma (val1, val2) == sum