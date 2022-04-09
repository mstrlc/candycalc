import mathlib
import pytest


# test for add function
def test_add():
    assert mathlib.add(10, 5) == 15
    assert mathlib.add(10, -5) == 5
    assert mathlib.add(-10, -5) == -15
    assert mathlib.add(-10, 5) == -5
    assert mathlib.add(10, 0) == 10
    assert mathlib.add(0, 0) == 0
    assert mathlib.add(0, 10) == 10
    assert mathlib.add(9999999, 9999999) == 19999998
    assert mathlib.add(9999999, -9999999) == 0
    assert mathlib.add(10.0123456789, 10.0123456789) == 20.0246913578
    assert mathlib.add(10.0123456789, -10.0123456789) == 0
    with pytest.raises(TypeError):
        mathlib.add(10, "a")
    with pytest.raises(TypeError):
        mathlib.add("a", 10)
    with pytest.raises(TypeError):
        mathlib.add("a", "a")
    with pytest.raises(TypeError):
        mathlib.add(10, -10, -10)
    with pytest.raises(ValueError):
        mathlib.add(10)
    with pytest.raises(ValueError):
        mathlib.add()


# test for subtract function with errors
def test_subtract():
    assert mathlib.subtract(10, 5) == 5
    assert mathlib.subtract(10, -5) == 15
    assert mathlib.subtract(-10, -5) == -5
    assert mathlib.subtract(-10, 5) == -15
    assert mathlib.subtract(10, 0) == 10
    assert mathlib.subtract(0, 0) == 0
    assert mathlib.subtract(0, 10) == -10
    assert mathlib.subtract(10, 10) == 0
    assert mathlib.subtract(9999999, 9999999) == 0
    assert mathlib.subtract(9999999, -9999999) == 19999998
    assert mathlib.subtract(10.0123456789, 10.0123456789) == 0
    assert mathlib.subtract(10.0123456789, -10.0123456789) == 20.0246913578
    with pytest.raises(TypeError):
        mathlib.subtract(10, "a")
    with pytest.raises(TypeError):
        mathlib.subtract("a", 10)
    with pytest.raises(TypeError):
        mathlib.subtract("a", "a")
    with pytest.raises(TypeError):
        mathlib.subtract(10, -10, -10)
    with pytest.raises(TypeError):
        mathlib.subtract(10)
    with pytest.raises(TypeError):
        mathlib.subtract()


# test for multiply function
def test_multiply():
    assert mathlib.multiply(10, 5) == 50
    assert mathlib.multiply(10, -5) == -50
    assert mathlib.multiply(-10, -5) == 50
    assert mathlib.multiply(-10, 5) == -50
    assert mathlib.multiply(10, 0) == 0
    assert mathlib.multiply(0, 0) == 0
    assert mathlib.multiply(0, 10) == 0
    assert mathlib.multiply(9999999, 9999999) == 99999980000001
    assert mathlib.multiply(9999999, -9999999) == -99999980000001
    assert mathlib.multiply(10.0123456789, 10.0123456789) == 100.24706599378749
    assert mathlib.multiply(10.0123456789, -10.0123456789) == -100.24706599378749
    with pytest.raises(TypeError):
        mathlib.multiply(10, "a")
    with pytest.raises(TypeError):
        mathlib.multiply("a", 10)
    with pytest.raises(TypeError):
        mathlib.multiply("a", "a")
    with pytest.raises(TypeError):
        mathlib.multiply(10, -10, -10)
    with pytest.raises(ValueError):
        mathlib.multiply(10)
    with pytest.raises(TypeError):
        mathlib.multiply()


# test for divide function
def test_divide():
    assert mathlib.divide(10, 5) == 2
    assert mathlib.divide(10, -5) == -2
    assert mathlib.divide(-10, -5) == 2
    assert mathlib.divide(-10, 5) == -2
    assert mathlib.divide(0, 10) == 0
    assert mathlib.divide(9999999, 9999999) == 1
    assert mathlib.divide(9999999, -9999999) == -1
    assert mathlib.divide(10.0123456789, 10.0123456789) == 1
    assert mathlib.divide(10.0123456789, -10.0123456789) == -1
    with pytest.raises(ZeroDivisionError):
        mathlib.divide(10, 0)
    with pytest.raises(ZeroDivisionError):
        mathlib.divide(0, 0)
    with pytest.raises(TypeError):
        mathlib.divide(10, "a")
    with pytest.raises(TypeError):
        mathlib.divide("a", 10)
    with pytest.raises(TypeError):
        mathlib.divide("a", "a")
    with pytest.raises(TypeError):
        mathlib.divide(10, -10, -10)
    with pytest.raises(TypeError):
        mathlib.divide(10)
    with pytest.raises(TypeError):
        mathlib.divide()


# test for factorial function
def test_factorial():
    assert mathlib.factorial(0) == 1
    assert mathlib.factorial(1) == 1
    assert mathlib.factorial(2) == 2
    assert mathlib.factorial(3) == 6
    assert mathlib.factorial(4) == 24
    assert mathlib.factorial(5) == 120
    assert mathlib.factorial(10) == 3628800
    assert mathlib.factorial(20) == 2432902008176640000
    with pytest.raises(TypeError):
        mathlib.factorial(10, 10)
    with pytest.raises(ValueError):
        mathlib.factorial(-10)
    with pytest.raises(TypeError):
        mathlib.factorial()


# test for power function with natural exponent
def test_power():
    assert mathlib.power(10, 0) == 1
    assert mathlib.power(3, 2) == 9
    assert mathlib.power(-5, 2) == 25
    assert mathlib.power(0, 2) == 0
    assert mathlib.power(6, 14) == 78364164096
    with pytest.raises(ValueError):
        mathlib.power(10, 10.532)
    with pytest.raises(ValueError):
        mathlib.power(10, -10)
    with pytest.raises(TypeError):
        mathlib.power(10, -10, -10)
    with pytest.raises(TypeError):
        mathlib.power()


# test for square root function
def test_sqrt():
    assert mathlib.sqrt(0, 4) == 0
    assert mathlib.sqrt(5, 2) == 2.23606797749979
    assert mathlib.sqrt(25, 2) == 5
    assert mathlib.sqrt(0, 40) == 0
    assert mathlib.sqrt(10, 10.532) == 1.2443676944633455
    with pytest.raises(ValueError):
        mathlib.sqrt(10, -10)
    with pytest.raises(ValueError):
        mathlib.sqrt(-10, 10)
    with pytest.raises(ValueError):
        mathlib.sqrt(-10, -10)
    with pytest.raises(TypeError):
        mathlib.sqrt(10, 10, 10)
    with pytest.raises(TypeError):
        mathlib.sqrt()


# test for natural logarithm function
def test_ln():
    assert mathlib.ln(4) == 1.3862943611198906
    assert mathlib.ln(10.24135) == 2.3264334468592685
    assert mathlib.ln(1432.47618103) == 7.267159820897427
    assert mathlib.ln(100) == 4.605170185988092
    with pytest.raises(ValueError):
        mathlib.ln(-4)
    with pytest.raises(ValueError):
        mathlib.ln(0)
    with pytest.raises(TypeError):
        mathlib.ln()
