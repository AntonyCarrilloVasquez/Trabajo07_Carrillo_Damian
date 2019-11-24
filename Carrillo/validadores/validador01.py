import os
#validar altura de un deportista
altura=0.0
altura_invalida=True
while (altura_invalida):
    altura=float(input("ingrese altura:"))
    altura_invalida=(altura < float(os.sys.argv[1]) or altura > float(os.sys.argv[2]))
#fin del bucle
print("fin del bucle")
