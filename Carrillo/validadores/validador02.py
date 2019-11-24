import os
#validar el peso de una persona promedio
peso=0.0
peso_invalido=True
while (peso_invalido):
    peso=float(input("ingrese peso:"))
    peso_invalido=(peso < float(os.sys.argv[1]) or peso > float(os.sys.argv[2]))
#fin del bucle
print("fin del bucle")

