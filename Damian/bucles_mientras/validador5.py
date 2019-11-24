importar os
# error mientras el numero de dias no sea 7
numero_dias =  int (os.sys.argv [ 1 ])
invalido =  verdadero

mientras (invalido):
    print ( " ################################## " )
    print ( " Ingrese el numero dias: " , numero_dias)
    print ( " ################################## " )
    invalido = (numero_dias ! =  7 )
    if (invalido ==   verdadero ):
        print ( " error " )
    más :
        print ( " todo correcto   " )

# fin_bucle
print ( " fin del bucle " )
