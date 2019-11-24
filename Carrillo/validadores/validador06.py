import os
#validar la mensualidad de un profesor
mensualidad=0.0
mensualidad_invalida=True
while (mensualidad_invalida):
    mensualidad=float(input("ingrese mensualidad:"))
    mensualidad_invalida=(mensualidad < float(os.sys.argv[1]) or mensualidad > float(os.sys.argv[2]))
#fin del bucle
print("fin del bucle")
