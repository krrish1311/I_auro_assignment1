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

if 'a' or 'add' in operation:
    add(first_val,second_val)

elif 's' or 'sub' in operation :
    subtract(first_val,second_val)
elif 'm'or 'mul' in operation:
    multiplication(first_val,second_val)
    
elif 'd' or 'dev' in operation :
    division(first_val,second_val)
elif 'mod' in operation:
    module(first_val, second_val)
    
