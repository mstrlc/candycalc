from math import log


def add(a,b):
    if type(a) == str or type(b) == str:
        raise TypeError
    return a+b

def subtract(a,b):
    if type(a) == str or type(b) == str:
        raise TypeError
    return a-b

def multiply(a,b):
    if type(a) == str or type(b) == str:
        raise TypeError
    return a*b

def divide(a,b):
    if type(a) == str or type(b) == str:
        raise TypeError
    if b!=0:
        return a/b
    else:
        raise ZeroDivisionError

def factorial(a):
    if type(a) == str:
        raise TypeError
    if a<0:
        raise ValueError("Factorial menej ako 0")
    b=1
    for i in range(a):
        b*=(i+1)
    return b

def power(a,b):
    if type(b) != int or b<0:
        raise ValueError("Exponent nie je prirodzene cislo")
    if type(a) == str or type(b) == str:
        raise TypeError
    return a**b

def sqrt(a,b):
    if type(a) == str or type(b) == str:
        raise TypeError
    if b<0:
        raise ValueError("Zaporna odmocnina")
    if a<0 and b%2==0:
        raise ValueError("Negativne cislo v parnej odmocnine")
    return a**(1/b)

def ln(a):
    if type(a) == str:
        raise TypeError
    return log(a)