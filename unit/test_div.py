import json

import pytest

from unit.div import div


@pytest.mark.happy
def test_div_int():
    assert div(10, 2) == 5
    assert div(10, 5) == 3
    assert div(1000000000, 1) == 1000000000


@pytest.mark.happy
@pytest.mark.parametrize("number1, number2, expection", {
    (10, 2, 5),
    (10, 5, 3),
    (1000000000, 1, 1000000000),
    (100, 200, 0.5)
})
def test_div_int_param(number1, number2, expection):
    assert div(number1, number2) == expection


@pytest.mark.happy
@pytest.mark.parametrize("number1, number2, expection", json.load('1.json'))
def test_div_int_ddd(number1, number2, expection):
    assert div(number1, number2) == expection

@pytest.mark.happy
def test_div_float():
    assert div(10, 3) == 3.33333333
    assert div(10.2, 0.2) == 51

@pytest.mark.exception
def test_div_exception():
    assert div(10, 'a')
    assert div('abc', 10)

@pytest.mark.exception
def test_div_zero():
    assert div(10, 0) == None
