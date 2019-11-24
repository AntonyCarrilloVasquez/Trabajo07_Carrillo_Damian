import os
#validar la edad de un puber
edad=0.0
edad_invalida=True
while (edad_invalida):
    edad=float(input("ingrese edad:"))
    edad_invalida=(edad < float(os.sys.argv[1]) or edad > float(os.sys.argv[2]))
#fin del bucle
print("fin del bucle")

