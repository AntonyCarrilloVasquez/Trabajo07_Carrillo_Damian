import os
#validar velocidad de un ferrari
velocidad=0.0
velocidad_invalida=True
while (velocidad_invalida):
    velocidad=float(input("ingrese velocidad:"))
    velocidad_invalida=(velocidad < float(os.sys.argv[1]) or velocidad > float(os.sys.argv[2]))
#fin del bucle
print("fin del bucle")
