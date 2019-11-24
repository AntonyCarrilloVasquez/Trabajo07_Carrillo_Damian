import os
#validar la temperatura normal de un ser humano
temperatura=0.0
temperatura_invalida=True
while (temperatura_invalida):
    temperatura=float(input("ingrese temperatura:"))
    temperatura_invalida=(temperatura < float(os.sys.argv[1]) or temperatura > float(os.sys.argv[2]))
#fin del bucle
print("fin del bucle")
