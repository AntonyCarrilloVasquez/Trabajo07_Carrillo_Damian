import os
#suma de 45 primeros numeros pares
x=int(os.sys.argv[1])
i=0
suma=0
while(i<=45):
    suma +=i
    i += 2
#fin_while
print("la suma de los 45 primeros numeros es:",suma)
