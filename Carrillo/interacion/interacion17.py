import os
#suma de 500 primeros numeros pares
x=int(os.sys.argv[1])
i=0
suma=0
while(i<=500):
    suma +=i
    i += 2
#fin_while
print("la suma de los 500 primeros numeros es:",suma)
