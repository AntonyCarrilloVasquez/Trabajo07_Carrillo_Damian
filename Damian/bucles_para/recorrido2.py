# sumar los numeros que se encuentra entre "x" y "z"
importar os
# input
x =  int (os.sys.argv [ 1 ])
z =  int (os.sys.argv [ 2 ])
i = x
suma =  0
mientras que (i <= z):
    suma + = i
    i + =   1
# fin_while
print ( " la suma de los numeros que estan entre dichos numeros es: " , suma)
