import os
#validar nota de un estudiante
nota=0.0
nota_invalida=True
while (nota_invalida):
    nota=float(input("ingrese nota:"))
    nota_invalida=(nota < float(os.sys.argv[1]) or nota > float(os.sys.argv[2]))
#fin del bucle
print("fin del bucle")

