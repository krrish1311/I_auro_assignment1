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

if 'a' in operation:
    add(first_val,second_val)

elif 's' in operation :
    subtract(first_val,second_val)
elif 'm' in operation:
    multiplication(first_val,second_val)
    
elif 'd' in operation :
    division(first_val,second_val)
    
