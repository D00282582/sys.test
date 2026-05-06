import pytest
from part1 import calculate_interest


def test_interest_tier1_boundary():
    assert calculate_interest(0) == "0.00"
    assert calculate_interest(1000) == f"{1000*0.03:.2f}"

def test_interest_tier2_boundary():
    # 1001 to 11000
    expected = (1000*0.03) + (10000*0.035)
    assert calculate_interest(11000) == f"{expected:.2f}"

def test_interest_tier3_boundary():
    # 11001 to 100000
    expected = (1000*0.03) + (10000*0.035) + (89000*0.04)
    assert calculate_interest(100000) == f"{expected:.2f}"

def test_interest_above_100k():
    deposit = 150000
    expected = (
        1000*0.03 +
        10000*0.035 +
        89000*0.04 +
        (deposit - 100000)*0.045
    )
    assert calculate_interest(deposit) == f"{expected:.2f}"

def test_string_input():
    with pytest.raises(ValueError, match="Deposit must not be a string."):
        calculate_interest("hello")

def test_boolean_input():
    with pytest.raises(ValueError, match="Deposit must not be a Boolean."):
        calculate_interest(True)

def test_negative_input():
    with pytest.raises(ValueError, match="Deposit cannot be negative."):
        calculate_interest(-50)
