import os
#suma de 600 primeros numeros impares
x=int(os.sys.argv[1])
i=1
suma=0
while(i<=600):
    suma +=i
    i += 2
#fin_while
print("la suma de los 600 primeros numeros es:",suma)
