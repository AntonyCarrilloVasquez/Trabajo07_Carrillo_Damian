# sumar los numeros que se encuentra entre "a" y "b"
importar os
# input
a =  int (os.sys.argv [ 1 ])
b =  int (os.sys.argv [ 2 ])
i = a
suma =  0
mientras que (i <= b):
    suma + = i
    i + =   5
# fin_while
print ( " la suma de los numeros que se diferencia en 5 unidades es: " , suma)
