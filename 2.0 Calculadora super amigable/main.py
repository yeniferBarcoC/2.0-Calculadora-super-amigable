""" Programa calculadora artimética super amigable#
    Realiza las 4 operaciones (+,-,* /)
    dada como entrada una cadena de caracteres 
    incorpora al modulo calculadora_aritmetica.py
    Yenifer Barco Castrillón
    Mayo 3-2021 """ 

#---------------- Zona librerias------------
import calculadora_aritmetica as calc

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------
def parser_cadena(cadena_entrada):
    operando=""

    #reemplazo los espacios
    cadena_sin_espacios = cadena_entrada.replace(" ", "")

    #Busco los simbolos find=-1 cuando no encuentra el simbolo
    multiplicacion=cadena_entrada.find("*")
    division=cadena_entrada.find("/")
    suma=cadena_entrada.find("+")
    resta=cadena_entrada[1:].find("-")

    #Si encuentra el simbolo del operador, separo la cadena
    if multiplicacion > 0:
        cadena_salida = cadena_sin_espacios.partition("*")
    elif division > 0:
        cadena_salida = cadena_sin_espacios.partition("/")
    elif suma > 0:
        cadena_salida = cadena_sin_espacios.partition("+")
    elif resta > 0: #verifica si el primer numero tiene un menos en la resta
        if (cadena_entrada.count("-"))>=2 and str(cadena_entrada[0])=="-" :
            cadena_salida = cadena_sin_espacios[1:].partition("-")
            nr1= True # El primer numero tiene un menos
            print(cadena_salida)
        else:
            cadena_salida = cadena_sin_espacios.partition("-")
            nr1= False
    else:
       print("Ingrese el operador",resta,cadena_salida)

    #comparo si la primera posicion de la palabra es "-"
    n1= str(cadena_salida[0][:1])=="-"
    n2= str(cadena_salida[2][:1])=="-"
    operando = cadena_salida[1]

    #Comprobamos si n1 y n2 tienen un "-"
    if n1 == True or nr1==True :
        if n2 == True :
            #Comprueba si  numero_1 y numero_2 son un numero
            if cadena_salida[0][1:].isdigit()==True and cadena_salida[2][1:].isdigit()==True:
                numero_uno = int(cadena_salida[0:][0])
                numero_dos = int(cadena_salida[2:][0])
            elif cadena_salida[0].isdigit()==True and cadena_salida[2][1:].isdigit:
                #Comprueba si es una resta y multiplica por -1 para darle el menos al primer numero
                numero_uno = int(cadena_salida[0])*(-1)
                numero_dos = int(cadena_salida[2:][0])
            else:
                print("ingrese valor valido suma1", numero_uno,numero_dos)
        else: # SI N2 NO ES TRUE
            if cadena_salida[0][1:].isdigit()==True and cadena_salida[2].isdigit()==True:
                numero_uno = int(cadena_salida[0:][0])
                numero_dos = int(cadena_salida[2:][0])
            #Comprueba si es una resta y multiplica por -1 para darle el menos al primer numero
            elif cadena_salida[0].isdigit()==True and cadena_salida[2].isdigit()==True:
                    numero_uno = int(cadena_salida[0])*(-1)
                    numero_dos = int(cadena_salida[2])
            else:
                print("ingrese valor valido suma2", numero_uno,numero_dos)
    if n1== False and nr1 == False:# Si n1 no es true
        if n2 == True :
            if cadena_salida[0].isdigit()==True and cadena_salida[2][1:].isdigit()==True:
                numero_uno = int(cadena_salida[0:][0])
                numero_dos = int(cadena_salida[2:][0])
            else:
                print("ingrese valor valido suma3", numero_uno,numero_dos)
        else: # Si n1 y n2 son false
            if cadena_salida[0].isdigit()==True and cadena_salida[2].isdigit()==True:
                numero_uno = int(cadena_salida[0:][0])
                numero_dos = int(cadena_salida[2:][0])
            else:
                print("ingrese valor valido suma4", cadena_salida)

    return numero_uno, numero_dos, operando
    

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

cadena = input("Ingrese la operacion: ")
numero_1,numero_2,operando=parser_cadena(cadena)

if operando=="+":
    suma = calc.sumar_numeros(numero_1,numero_2)
    print(numero_1,"+",numero_2,"=",suma)
elif operando=="-":
    resta = calc.restar_numeros(numero_1,numero_2)
    print(numero_1,"-",numero_2,"=",resta)
elif operando=="*":
    multiplicacion = calc.multiplicar_numeros(numero_1,numero_2)
    print(numero_1,"*",numero_2,"=",multiplicacion)
elif operando=="/":
    division = calc.dividir_numeros(numero_1,numero_2)
    print(numero_1,"/",numero_2,"=",division)
else:
    print("Por favor ingrese la operacion a realizar")


