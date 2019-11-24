import os
#validar el numero de personas permitidas en una discoteca
personas=0.0
personas_extras=True
while (personas_extras):
    personas=float(input("ingrese personas:"))
    personas_extras=(personas < float(os.sys.argv[1]) or personas > float(os.sys.argv[2]))
#fin del bucle
print("fin del bucle")

