# basic math operations 

def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Please Eneter correct value of second argument\ncan't divide by zero")
        