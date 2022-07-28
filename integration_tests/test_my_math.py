import pytest
from my_math.arithmetic import sum, prod, sub, div

@pytest.mark.integration
def test_combo():
    assert prod(sum(1, 2), 3) == 9
    assert div(6, sub(5, 3)) == 3