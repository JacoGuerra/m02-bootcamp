def factorial(n):
    def recursividad(n):
        if n >= 1:
                return n * recursividad(n -1)
        if n == 0:
                return 1
    if n>0:
        return recursividad(n)
    else:
        n=-n
        return recursividad(n)
        
        
print(factorial(1))