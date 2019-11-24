import os
#validar la profundidad de una piscina para que un niño pueda entrar
profundidad=0.0
profundidad_invalida=True
while (profundidad_invalida):
    profundidad=float(input("ingrese profundidad:"))
    profundidad_invalida=(profundidad < float(os.sys.argv[1]) or profundidad > float(os.sys.argv[2]))
#fin del bucle
print("fin del bucle")
