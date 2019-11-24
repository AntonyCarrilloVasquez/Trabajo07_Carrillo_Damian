import os
#validar fiebre de una persona
fiebre=0.0
fiebre_invalida=True
while (fiebre_invalida):
    fiebre=float(input("ingrese fiebre:"))
    fiebre_invalida=(fiebre < float(os.sys.argv[1]) or fiebre > float(os.sys.argv[2]))
#fin del bucle
print("fin del bucle")

