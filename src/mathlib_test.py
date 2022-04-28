##
#   @file mathlib_test.py
#   @brief Tests for implementation of library 'mathlib'

import mathlib
import pytest


##
# @brief Tests for 'add' function

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
        mathlib.add("a", 10)
        mathlib.add("a", "a")
        mathlib.add(10, -10, -10)
        mathlib.add(10)
        mathlib.add()


##
# @brief Tests for 'subtract' function

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
        mathlib.subtract("a", 10)
        mathlib.subtract("a", "a")
        mathlib.subtract(10, -10, -10)
        mathlib.subtract(10)
        mathlib.subtract()


##
# @brief Tests for 'multiply' function

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
    assert mathlib.multiply(
        10.0123456789, -10.0123456789) == -100.24706599378749
    with pytest.raises(TypeError):
        mathlib.multiply(10, "a")
        mathlib.multiply("a", 10)
        mathlib.multiply("a", "a")
        mathlib.multiply(10, -10, -10)
        mathlib.multiply(10)
        mathlib.multiply()


##
# @brief Tests for 'divide' function

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
        mathlib.divide(0, 0)
    with pytest.raises(TypeError):
        mathlib.divide(10, "a")
        mathlib.divide("a", 10)
        mathlib.divide("a", "a")
        mathlib.divide(10, -10, -10)
        mathlib.divide(10)
        mathlib.divide()


##
# @brief Tests for 'factorial' function

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
        mathlib.factorial()
    with pytest.raises(ValueError):
        mathlib.factorial(-10)


##
# @brief Tests for 'power' function with natural exponent

def test_power():
    assert mathlib.power(10, 0) == 1
    assert mathlib.power(3, 2) == 9
    assert mathlib.power(-5, 2) == 25
    assert mathlib.power(0, 2) == 0
    assert mathlib.power(6, 14) == 78364164096
    with pytest.raises(ValueError):
        mathlib.power(10, 10.532)
        mathlib.power(10, -10)
    with pytest.raises(TypeError):
        mathlib.power(10, -10, -10)
        mathlib.power()


##
# @brief Tests for 'nroot' function

def test_nroot():
    assert mathlib.nroot(0, 4) == 0
    assert mathlib.nroot(5, 2) == 2.23606797749979
    assert mathlib.nroot(25, 2) == 5
    assert mathlib.nroot(0, 40) == 0
    assert mathlib.nroot(10, 10.532) == 1.2443676944633455
    assert mathlib.nroot(-8, 3) == -2
    with pytest.raises(ValueError):
        mathlib.nroot(10, -10)
        mathlib.nroot(-10, 10)
        mathlib.nroot(-10, -10)
    with pytest.raises(TypeError):
        mathlib.nroot(10, 10, 10)
        mathlib.nroot()


##
# @brief Tests for 'ln' function

def test_ln():
    assert mathlib.ln(4) == 1.3862943611198906
    assert mathlib.ln(10.24135) == 2.3264334468592685
    assert mathlib.ln(1432.47618103) == 7.267159820897427
    assert mathlib.ln(100) == 4.605170185988092
    with pytest.raises(ValueError):
        mathlib.ln(-4)
        mathlib.ln(0)
    with pytest.raises(TypeError):
        mathlib.ln(3, 5)
        mathlib.ln()
