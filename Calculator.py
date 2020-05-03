import math

def add(x,y):
    z=x+y
    return z

def multiply(x,y):
    z=x*y
    return z

def subtract(x,y):
    z=x-y
    return z

def divide(x,y):
    z=x/y
    return z


def square_root(x,y):
    z=math.sqrt(x**2 + y**2)
    return z
    

def calculator(x,y,op):
    if (op== "+"):
        return add(x,y)
    if (op== "*"):
        return multiply(x,y)
    if (op== "-"):
        return subtract(x,y)
    if (op=="/"):
        return divide(x,y)
    if  (op=="**"):
        return square_root(x,y)

print(calculator(5,10,'**'))
