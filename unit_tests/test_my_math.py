import pytest
from my_math.arithmetic import sum, prod, div, sub

@pytest.mark.unit
class TestUnit():

  @pytest.mark.parametrize('x, y, expected', [(1, 1, 2), (1, 2, 3), (2, 1, 3)])
  def test_sum(self, x, y, expected):
    assert sum(x, y) == expected

  @pytest.mark.parametrize('x, y, expected', [(1, 1, 1), (2, 3, 6), (-1, -5, 5)])
  def test_prod(self, x, y, expected):
    assert prod(x, y) == expected

  @pytest.mark.parametrize('x, y, expected', [(1, 1, 1), (2, 0.2, 10), (-5, -2, 2.5)])
  def test_div(self, x, y, expected):
    assert div(x, y) == expected

  @pytest.mark.parametrize('x, y, expected', [(1, 1, 0), (2, 3, -1), (5, -10, 15)])
  def test_sub(self, x, y, expected):
    assert sub(x, y) == expected