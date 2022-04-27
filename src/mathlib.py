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
        raise ValueError("Math Err")
    b=1
    for i in range(a):
        b*=(i+1)
    return b

def power(a,b): 
    if type(b) != int or b<0:
        raise ValueError("Math Err")
    if type(a) == str or type(b) == str:
        raise TypeError
    return a**b

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

def ln(a):
    if type(a) == str:
        raise TypeError
    return log(a)