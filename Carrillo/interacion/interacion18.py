import os
#suma de 10 primeros numeros impares
x=int(os.sys.argv[1])
i=1
suma=0
while(i<=10):
    suma +=i
    i += 2
#fin_while
print("la suma de los 10 primeros numeros es:",suma)
