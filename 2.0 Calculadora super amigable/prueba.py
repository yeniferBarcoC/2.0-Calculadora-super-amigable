 #Si encuentra el simbolo de +
    if suma > 0:
        cadena_suma = cadena_sin_espacios.partition("+")
        #comparo si la primera posicion de la palabra es "-"
        n1= str(cadena_suma[0][:1])=="-"
        n2= str(cadena_suma[2][:1])=="-"
        operando = cadena_suma[1]

        #Comprobamos si n1 y n2 tienen un "-"
        if n1 == True :
            if n2 == True :
                #Comprueba si  numero_1 y numero_2 son un numero
                if cadena_suma[0][1:].isdigit()==True and cadena_suma[2][1:].isdigit()==True:
                    numero_uno = int(cadena_suma[0:][0])
                    numero_dos = int(cadena_suma[2:][0])
                else:
                    print("ingrese valor valido suma1")
            else: # SI N2 NO ES TRUE
                if cadena_suma[0][1:].isdigit()==True and cadena_suma[2].isdigit()==True:
                    numero_uno = int(cadena_suma[0:][0])
                    numero_dos = int(cadena_suma[2:][0])
                else:
                    print("ingrese valor valido suma2")
        if n1== False:# Si n1 no es true
            if n2 == True :
                if cadena_suma[0].isdigit()==True and cadena_suma[2][1:].isdigit()==True:
                    numero_uno = int(cadena_suma[0:][0])
                    numero_dos = int(cadena_suma[2:][0])
                else:
                    print("ingrese valor valido suma3")
            else: # Si n1 y n2 son false
                if cadena_suma[0].isdigit()==True and cadena_suma[2].isdigit()==True:
                    numero_uno = int(cadena_suma[0:][0])
                    numero_dos = int(cadena_suma[2:][0])
                else:
                    print("ingrese valor valido suma4")
    else:
        print("Error")
    return numero_uno, numero_dos, operando