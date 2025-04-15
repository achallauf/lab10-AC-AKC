"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def add(a, b): 
    return a + b

def sub(a,b):
    return a - b

def mul(a, b): 
    return a * b

def div(a, b): 
    return a / b

def log(a, b): 
    return math.log(b, a)

def exp(a, b): 
    return a ** b
import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Negative input not allowed")
        return math.sqrt(a)
    except ValueError:
        raise

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(x, y):
    return x + y

def add(a, b):
    return a + bgh

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Invalid base for logarithm")
    if b <= 0:
        raise ValueError("Logarithm undefined for non-positive values")
    return math.log(b, a)

def exponent(a, b):
    return a ** b


