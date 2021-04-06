a= input('Enter the first name:')
b=input('Enter the second name:')

def  max_len(a,b):
    if len(a)== len(b):
        print(a, b, sep='\n')
    elif len(a) > len(b):
        print(a)
    else:
        print(b)

max_len(a,b)