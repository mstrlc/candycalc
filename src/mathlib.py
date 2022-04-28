##
#  @file mathlib.py
#  @package mathlib
#  @brief Mathematical library


from math import log


##
# @brief Adds two numbers
#
# @param a First number
# @param b Second number
#
# @return Addition of two numbers a and b
def add(a,b):
    if type(a) == str or type(b) == str:
        raise TypeError
    return a+b


##
# @brief Subtracts two numbers
#
# @param a First number
# @param b Second number
#
# @return Substraction of two numbers a and b
def subtract(a,b):
    if type(a) == str or type(b) == str:
        raise TypeError
    return a-b



##
# @brief Multiplies two numbers
#
# @param a First number
# @param b Second number
#
# @return Multiplication of two numbers a and b
def multiply(a,b):
    if type(a) == str or type(b) == str:
        raise TypeError
    return a*b


##
# @brief Divides two numbers
#
# @param a First number, dividend
# @param b Second number, divisor
#
# @return Division of two numbers a and b
def divide(a,b):
    if type(a) == str or type(b) == str:
        raise TypeError
    if b!=0:
        return a/b
    else:
        raise ZeroDivisionError


##
# @brief Factorial
#
# @param a size of the factorial
#
# @return Factorial of number a
def factorial(a): 
    if type(a) == str:
        raise TypeError
    if a<0:
        raise ValueError("Math Err")
    b=1
    for i in range(a):
        if(abs(b) > (2 ** 128 - 1)):
            raise OverflowError() 
        b*=(i+1)
    return b


##
# @brief Power of a number
#
# @param a Number to be powered
# @param b The power of a
#
# @return Number a to the power of b
def power(a,b): 
    if type(b) != int or b<0:
        raise ValueError("Math Err")
    if type(a) == str or type(b) == str:
        raise TypeError
    return a**b


##
# @brief Root of a number
#
# @param a Number to be rooted
# @param b The root of b
#
# @return B-th root of number a
def nroot(a,b): 
    if type(a) == str or type(b) == str:
        raise TypeError
    if b<0:
        raise ValueError("Math Err")
    if a<0 and b%2==0:
        raise ValueError("Math Err")
    elif a<0:
        return -((-a)**(1/b))
    else:
        return a**(1/b)


##
# @brief Natural logarithm of a number
#
# @param a Number for which we want the logarithm
#
# @return Natural logarithm of number a
def ln(a):
    if type(a) == str:
        raise TypeError
    if a <=0:
        raise ValueError("Math Err")
    return log(a)