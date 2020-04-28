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


def calculator(x,y,op):
    if (op== "+"):
        return add(x,y)
    if (op== "*"):
        return multiply(x,y)
    if (op== "-"):
        return subtract(x,y)
    if (op=="/"):
        return divide(x,y) 

print(calculator(6,8,'*'))
