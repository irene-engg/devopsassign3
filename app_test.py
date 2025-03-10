import pytest
from app import area_of_square

# Basic functional tests
@pytest.mark.parametrize("side, expected", [
    (2, 4),
    (5, 25),
    (10, 100),
    (63, 63)  
])
def test_area(side, expected):
    assert area_of_square(side) == expected


# Test for invalid input types
def test_invalid_type():
    with pytest.raises(TypeError):
        area_of_square("hello")


# Test for negative numbers
def test_negative_input():
    with pytest.raises(ValueError):
        area_of_square(-5)
