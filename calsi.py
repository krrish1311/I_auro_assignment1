first_val=int(input())
second_val=int(input())
operation=input()

def add(first,second):
    return first+second

def subtract(first,second):
    return first-second

def multiplication(first,second):
    return first*second

def division(first,second):
    return first/second
def module(first,second):
    return first//second

if 'addition'or "+" in operation:
    add(first_val,second_val)

elif 'subtraction' or "-" in operation :
    subtract(first_val,second_val)
elif 'multiplication' or "*" in operation:
    multiplication(first_val,second_val)
    
elif 'division' or "/" in operation :
    division(first_val,second_val)
    
elif 'mod' in operation:
    module(first_val, second_val)
    
