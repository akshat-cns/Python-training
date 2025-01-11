import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    with pytest.raises(TypeError, match="Invalid input,expected a number."):
        add("a", 5)
    with pytest.raises(TypeError, match="Invalid input,expected a number."):
        add(None, 5)
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    with pytest.raises(TypeError, match="Invalid input,expected a number."):
        subtract(5, "test")
    assert subtract(0, 5) == -5
    assert subtract(-3, -7) == 4

def test_multiply():
    with pytest.raises(TypeError, match="Invalid input,expected a number."):
        multiply([1, 2], 3)
    assert multiply(-1, 5) == -5
    assert multiply(0, 5) == 0

def test_divide():
    with pytest.raises(TypeError, match="Invalid input,expected a number."):
        divide({}, 3)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
    assert divide(10, 2) == 5
    assert divide(-10, 2) == -5
    assert divide(5, 2) == 2.5
