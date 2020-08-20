def factorial(x):
    a=0
    if x>0:
        return x
    if x<0:
        return -x
        a=1
    
    fact = lambda x: 1 if x == 0 else x * fact(x-1)

    if a==1:
        fact=-fact
        
        
print(factorial(3))