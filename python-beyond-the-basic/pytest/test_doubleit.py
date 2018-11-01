import pytest
from doubleit import doubleit

def test_doubleit():
    with pytest.raises(TypeError):
        doubleit('a')