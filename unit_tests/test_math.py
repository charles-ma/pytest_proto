import pytest
from my_math.arithmetic import sum, prod, div, sub

@pytest.mark.unit
class TestUnit():

  def test_sum(self):
    assert sum(1, 1) == 2

  def test_prod(self):
    assert prod(2, 3) == 6

  def test_div(self):
    assert div(1, 2) == 0.5

  def test_sub(self):
    assert sub(2, 1) == 1