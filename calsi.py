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

if operation=='a':
    add(first_val,second_val)

elif operation=='s':
    subtract(first_val,second_val)
elif operation == 'm':
    multiplication(first_val,second_val)
    
elif operation == 'd':
    division(first_val,second_val)
    
