from funciones1stnivel import sumaTodos 

doble= lambda x: x*2

print(sumaTodos(3, doble))
print(sumaTodos(3, lambda x: x**3))