import os
#suma de 200 primeros numeros impares
x=int(os.sys.argv[1])
i=1
suma=0
while(i<=200):
    suma +=i
    i +=2
#fin_while
print("la suma de los 200 primeros numeros es:",suma)
