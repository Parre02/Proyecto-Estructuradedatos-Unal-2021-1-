import random
from collections import deque

print('''                                                                ..',,;;;;;,,'..
                                                             ..',;;;;;;;;;;;;;;;;;;;,;;;:::,.
                                                        ..';;;;;;;;;;;;;;;;;;;;;;oOOxoooooooodkx;
                                                     .,;;;;;;;;;;;;;;;;;;;;;;;cO0lcoOXXKKKKKX0dccOd
                                                 ..,;;;;;;;;;;;;;;;;;;coxo;;lKk,lKKKKKKKKKKKKKKKKo;0l
                                               .,;;;;;;;;;;;;;;;;cdkOkol,Nd00..KKKKKX0dc;;cdKKKKKKK:dO
                                            .';;;;;;;;;;;;;;;;;l0k,clkKXO'Wc .XKKKKO'       .;0KKKKXcoO
                                          .,;;;;;;;;;;:ld:;;;:0k'.',XKKKXl.  OKKKK0 ;ll:. .,;,.OKKKKX,0,
                                        .,;;;;;;;:oxOkxolx0x:cN.';;.oKKKKX.  NKKKX:x0c:lk0,.,.  KKKKK0,X
                                       ,;;;;:oxOkd:,ld0XXkcck0KK ,.  0KKKKK  NKKKXcxk;;;;:K: .' oKKKKN.M
                                     .;;;:kOolllx0. 0KKKKKKXkcckd .' .XKKKKk KKKKKK.Nc;;;;:W..  oKKKKN.N
                                  ..,;;:k0;..KKKKKK .XKKKKKKKKXkc.    :XKKKX:;XKKKKk,Kd;;;;K:  .XKKKKk::
                             .:dxxlOx;;00 ,;'.XKKKKx :XKKKKXKKKKKXk:   xKKKKX.oXKKKK0:lkOO0O. cKKKKKX.O
                          'OxllloOK.Xl;:W,',. cXKKKX; kKKKKNdkXKKKKKXx;.KKKKK0 cXKKKKKKxlllokXKKKKKK'x 
                        .Ox. .XKKKKk'N:;oN. .' kKKKKX. KKKKK0 .cOXKKKKKXKXKKKKd .dXKKKKKKKKKKKKKKKl'c
                        ol    :XKKKXco0;;OO..   XKKKK0 'XKKKKd   .cOXKKKKKKKKKX,   :xKXKKKKKXX0d; o
                         K.    xKKKKX.0d;;Nc    'XKKKKo oXKKKX,     .l0XKKKKKKKX.     .';;;,.   l
                          0     KKKKK0.Nc;cW.    oKKKKX. 0KKKKX        .l0XKKKKKO           .c.
                          ;o   .'XKKKKd;X;;xX     KKKKKO .XKKKKO.d'       .o0Kko:.OOxdoodxk.
                           k' ,;.lKKKKX,xk;;Kx    dKKKKN  ;XKKKXllM0d.          cKd;;:::;'
                            N.,;. OKKKKX.Ok;:W'   KKKKKN   xKKKKX,0kck0o.  .,lx0d;;;;;;;
                            .k  .'.KKKKKXc:ddO. ;0KKKKKd    KXOdc.:W:;;lkOOkdc;;;;;;;;
                             c:..  .0KKKKKXOxxOXKKKKKXd.        'OOc;;;;;;;;;;;;;;;;
                              x.     oXKKKKKKKKKKKKKd;xW'   'cxOOc;;;;;;;;;;;;;;;'
                               l,     .ckKXXXXX0xl,.oKolXxkOxl;;;;;;;;;;;;;;;;;
                                 x.        ...   .oKo;;;;;;;;;;;;;;;;;;;;;;;
                                   c;.       .,oOOl;;;;;;;;;;;;;;;;;;;;;
                                        lxxkOkoc;;;;;;;;;;;;;;;;;;;.
                                             ';;;;;;;;;;;;;;, 






                                         ''')


cartas = {"RC":("+_________+", "|     Rojo|", "|         |", "|     />  |", "|  </     |", "|         |", "|         |", "+---------+"),  

"ZC":("+_________+", "|     Azul|", "|         |", "|     />  |", "|  </     |", "|         |", "|         |", "+---------+"), 

"AC":("+_________+", "| Amarillo|", "|         |", "|     />  |", "|  </     |", "|         |", "|         |", "+---------+"), 

"VC":("+_________+", "|    Verde|", "|         |", "|     />  |", "|  </     |", "|         |", "|         |", "+---------+"), 

"RB":("+_________+", "|x    Rojo|", "|         |", "|         |", "|    X    |", "|         |", "|        x|", "+---------+"), 

"ZB":("+_________+", "|x    Azul|", "|         |", "|         |", "|    X    |", "|         |", "|        x|", "+---------+"), 

"AB":("+_________+", "|xAmarillo|", "|         |", "|         |", "|    X    |", "|         |", "|        x|", "+---------+"),

"VB":("+_________+", "|x   Verde|", "|         |", "|         |", "|    X    |", "|         |", "|        x|", "+---------+"), 

"R2+":("+_________+", "|+2   Rojo|", "|         |", "|         |", "|    +2   |", "|         |", "|       +2|", "+---------+"), 

"Z2+":("+_________+", "|+2   Azul|", "|         |", "|         |", "|    +2   |", "|         |", "|       +2|", "+---------+"), 

"A2+":("+_________+", "| Amarillo|", "|         |", "|         |", "|    +2   |", "|         |", "|       2+|", "+---------+"), 

"V2+":("+_________+", "|+2  Verde|", "|         |", "|         |", "|    +2   |", "|         |", "|       2+|", "+---------+"), 

"R1":("+_________+", "|1    Rojo|", "|         |", "|         |", "|    1    |", "|         |", "|        1|", "+---------+"), 

"Z1":("+_________+", "|1    Azul|", "|         |", "|         |", "|    1    |", "|         |", "|        1|", "+---------+"), 

"A1":("+_________+", "|1Amarillo|", "|         |", "|         |", "|    1    |", "|         |", "|        1|", "+---------+"), 

"V1":("+_________+", "|1   Verde|", "|         |", "|         |", "|    1    |", "|         |", "|        1|", "+---------+"), 

"R2":("+_________+", "|2    Rojo|", "|         |", "|         |", "|    2    |", "|         |", "|        2|", "+---------+"), 

"Z2":("+_________+", "|2    Azul|", "|         |", "|         |", "|    2    |", "|         |", "|        2|", "+---------+"), 

"A2":("+_________+", "|2Amarillo|", "|         |", "|         |", "|    2    |", "|         |", "|        2|", "+---------+"), 

"V2":("+_________+", "|2   Verde|", "|         |", "|         |", "|    2    |","|         |", "|        2|", "+---------+"), 

"R3":("+_________+", "|3    Rojo|", "|         |", "|         |", "|    3    |", "|         |", "|        3|", "+---------+"), 

"Z3":("+_________+", "|3    Azul|", "|         |", "|         |", "|    3    |", "|         |", "|        3|", "+---------+"), 

"A3":("+_________+", "|3Amarillo|", "|         |", "|         |", "|    3    |", "|         |", "|        3|", "+---------+"), 

"V3":("+_________+", "|3   Verde|", "|         |", "|         |", "|    3    |", "|         |", "|        3|", "+---------+"), 

"R4":("+_________+", "|4    Rojo|", "|         |", "|         |", "|    4    |", "|         |", "|        4|", "+---------+"), 

"Z4":("+_________+", "|4    Azul|", "|         |", "|         |", "|    4    |", "|         |", "|        4|", "+---------+"), 

"A4":("+_________+", "|4Amarillo|", "|         |", "|         |", "|    4    |", "|         |", "|        4|", "+---------+"), 

"V4":("+_________+", "|4   Verde|", "|         |", "|         |", "|    4    |", "|         |", "|        4|", "+---------+"), 

"R5":("+_________+", "|5    Rojo|", "|         |", "|         |", "|    5    |", "|         |", "|        5|", "+---------+"), 

"Z5":("+_________+", "|5    Azul|", "|         |", "|         |", "|    5    |", "|         |", "|        5|", "+---------+"), 

"A5":("+_________+", "|5Amarillo|", "|         |", "|         |", "|    5    |", "|         |", "|        5|", "+---------+"), 

"V5":("+_________+", "|5   Verde|", "|         |", "|         |", "|    5    |", "|         |", "|        5|", "+---------+"), 

"R6":("+_________+", "|6    Rojo|", "|         |", "|         |", "|    6    |", "|         |", "|        6|", "+---------+"), 

"Z6":("+_________+", "|6    Azul|", "|         |", "|         |", "|    6    |", "|         |", "|        6|", "+---------+"), 

"A6":("+_________+", "|6Amarillo|", "|         |", "|         |", "|    6    |", "|         |", "|        6|", "+---------+"), 

"V6":("+_________+", "|6   Verde|", "|         |", "|         |", "|    6    |", "|         |", "|        6|", "+---------+"), 

"R7":("+_________+", "|7    Rojo|", "|         |", "|         |", "|    7    |", "|         |", "|        7|", "+---------+"), 

"Z7":("+_________+", "|7    Azul|", "|         |", "|         |", "|    7    |", "|         |", "|        7|", "+---------+"), 

"A7":("+_________+", "|7Amarillo|", "|         |", "|         |", "|    7    |", "|         |", "|        7|", "+---------+"), 

"Z7":("+_________+", "|7   Verde|", "|         |", "|         |", "|    7    |", "|         |", "|        7|", "+---------+"), 

"R8":("+_________+", "|8    Rojo|", "|         |", "|         |", "|    8    |", "|         |", "|        8|", "+---------+"), 

"Z8":("+_________+", "|8    Azul|", "|         |", "|         |", "|    8    |", "|         |", "|        8|", "+---------+"), 

"A8":("+_________+", "|8Amarillo|", "|         |", "|         |", "|    8    |", "|         |", "|        8|", "+---------+"), 

"V8":("+_________+", "|8   Verde|", "|         |", "|         |", "|    8    |", "|         |", "|        8|", "+---------+"), 

"R9":("+_________+", "|9    Rojo|", "|         |", "|         |", "|    9    |", "|         |", "|        9|", "+---------+"), 

"Z9":("+_________+", "|9    Azul|", "|         |", "|         |", "|    9    |", "|         |", "|        9|", "+---------+"), 

"A9":("+_________+", "|9Amarillo|", "|         |", "|         |", "|    9    |", "|         |", "|        9|", "+---------+"), 

"V9":("+_________+", "|9   Verde|", "|         |","|         |", "|    9    |", "|         |", "|        9|", "+---------+")}


##############################################################################################################

# Inicializacion del programa, se reparten todas las cartas 

lista_cartas = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "RB", "RC", "R2+",
"R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "RB", "RC", "R2+",
 "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "AB", "AC", "A2+",
  "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "AB", "AC", "A2+",
   "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "VB", "VC", "V2+",
    "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "VB", "VC", "V2+",
     "Z1", "Z2", "Z3", "Z4", "Z5", "Z6", "Z7", "Z8", "Z9", "ZB", "ZC", "Z2+",
      "Z1", "Z2", "Z3", "Z4", "Z5", "Z6", "Z7", "Z8", "Z9", "ZB", "ZC", "Z2+"]


# Maso de de cartas donde esta la carta del centro
maso = []

# Cartas aleatorias
random.shuffle(lista_cartas) # O(n*n)

# Turnos
turnos = deque()
turno_1 = []
turno_2 = []
turno_3 = []
turno_4 = []


for AddCards in range(8):
    turno_1.append(lista_cartas.pop())
    turno_2.append(lista_cartas.pop())
    turno_3.append(lista_cartas.pop())
    turno_4.append(lista_cartas.pop())

#Se ramdomizan los turnos para comenzar 

turnos.append(turno_1)
turnos.append(turno_2)
turnos.append(turno_3)
turnos.append(turno_4)

random.shuffle(turnos)


# maso agrega una carta aleatoria que es con la que se va a comenzar el juego
maso.append(lista_cartas.pop())
sentido = True


########################################################################################################################



# Busqueda de carta que pueda servir por turno.
def BusquedaDeCarta(turno, cartaCentro, masoRestante):
    global acumulacion
    encontrada = False
    #se priorisan bloqueos y +2
    if cartaCentro[-1][-1] == 'B': 
        for carta in turno:
            if carta[-1] == cartaCentro[-1][-1]:
                cartaCentro.append(carta)
                turno.remove(carta)
                encontrada = True
                return 1
        if encontrada == False:
            return 1
    
    if cartaCentro[-1][-1] == '+':
        acumulacion += 2
        for carta in turno:
            if carta[-1] == cartaCentro[-1][-1]:
                cartaCentro.append(carta)
                turno.remove(carta)
                encontrada = True
                return 1
        if encontrada == False:
            for i in range(acumulacion):
                VerificarListaDeArrastre()
                turno.append(masoRestante.pop())
            acumulacion = 0
            return 1
    else:
        for carta in turno:
            if carta[0] == cartaCentro[-1][0] or carta[-1] == cartaCentro[-1][-1]:
                cartaCentro.append(carta)
                turno.remove(carta)
                encontrada = True
                return 1
        if encontrada == False and masoRestante[-1][0] == cartaCentro[-1][0] or masoRestante[-1][-1] == cartaCentro[-1][-1]:
            cartaCentro.append(masoRestante.pop())
            return 1
        else:
            turno.append(masoRestante.pop())
            return -1

#funcion de cambio de sentido
def CambioDeSentido(cartaCentro):
    global sentido
    # B en este caso es para identificar si la carta es especial osea si contiene (C, B, 2)
    # Cambio de sentido
    B = cartaCentro[-1]
    if B[1] == 'C' and sentido == True: #Sentido horario
        sentido = False
    elif B[1] == 'C' and sentido == False: #Sentido Antihorario
        sentido = True


##En esta funcion se verifica si el jugador puede arrastrar
def verificarArrastre (masoCartasJugador, MasoCentro):
    posiblejugadas = []

    for i in range(len(masoCartasJugador)):
        if MasoCentro[-1][0] == masoCartasJugador[i][0]:
            posiblejugadas.append(masoCartasJugador[i])
        elif MasoCentro[-1][1] == masoCartasJugador[i][1]:
            posiblejugadas.append(masoCartasJugador[i])
    if len(posiblejugadas) != 0:
        return False
    else:
        return True

def verificarCartaTirar (masoCartasJugador, masoCentro,cartaTirar):
    ##Se verifica si existe la carta que deseo tirar en el maso y se realizan las comparaciones para tirar
    posiblejugadas = []

    if cartaTirar in masoCartasJugador:
        print("La carta esta en el maso")
        
        for i in range(len(masoCartasJugador)):
            if masoCentro[-1][0] == masoCartasJugador[i][0]:
                posiblejugadas.append(masoCartasJugador(i))
            elif masoCentro[-1][1] == masoCartasJugador[i][1]:
                posiblejugadas.append(masoCartasJugador(i))
        return posiblejugadas
    else:
        print("La carta no esta en el maso, favor coloque bien el dato -.-")
        return
        
def VerificarListaDeArrastre():
    global lista_cartas
    global maso
    global Centro
    if len(lista_cartas) == 0:
        Centro = maso.pop()
        lista_cartas = list(maso)
        maso = []
        maso.append(Centro)



while True:
    # Si el maso de cartas restantes se queda en 0 este se reemplaza por el maso de cartas que no estas en posesion de ningun jugador
    if len(lista_cartas) == 0:
        Centro = maso.pop()
        lista_cartas = list(maso)
        maso = []
        maso.append(Centro)
    
    verificarSiSeArrastro = False
    verificarPosibleJugada = False

    while True:
        if turnos[0] == turno_1:
            print("Menu del jugador")
            print("Opciones:")
            print(" 1.Ver cartas en mi maso")
            print(" 2.Arrastrar")
            print(" 3.Ver la carta del centro")
            print(" 4.Tirar carta")

            entrada = int(input("Elija la opcion con un entero: "))


            if entrada == 1:
                listaImpresionCartas = turnos[0]
                print(" ")
                for i in range(len(cartas[maso[-1]])):
                    a = ""
                    for j in listaImpresionCartas:
                        a += cartas[j][i] + "       "
                    print(a)
                    a = ""
                indices = list(map(str, range(1, len(listaImpresionCartas) + 1)))
                print("    ", "                 ".join(indices))
                print(" ")
            elif entrada == 2:
                verificarPosibleArrastre = False
                verificarPosibleArrastre = verificarArrastre(turnos[0],maso)
                if verificarPosibleArrastre == True and verificarSiSeArrastro == False:
                    print("Se ha arrastrado una carta")
                    turnos[0].add(lista_cartas.pop(-1))
                    verificarSiSeArrastro = True
                else:
                    print("Aun no se puede arrastrar tienes movimiento posibles o ya arrastraste")
            elif entrada == 3:
                print(' CARTAS DEL CENTRO ')
                print(" ")
                print(" ")
                for i in cartas[maso[-1]]:
                    print(i)
                print(" ")
                print(" ")
            elif entrada == 4:

                ##Aqui da errores revisar aun falta hacer el filtro mejor
                print("\nImportante las Cartas que empiezan con Z al comienzo son las azules")
                print("Las cartas que por ejemplo son RB, RC, R2+ corresponden a la primera letra el color R = Rojo y en la segunda letra \n B = Cancelar el proximo jugador \n C = Cambio de Sentido \n 2+ es igual a +2")
                print("\nQue carta desea tirar?")
                varCartaTirar = str(input())
                masoCartasJugador = turnos[0]
                ##Para poder tirar elegir el indice
                
                varPosibleJugadas = verificarCartaTirar(masoCartasJugador,maso,varCartaTirar)

                if len(varPosibleJugadas) != 0:
                    verificarPosibleJugada = True

                if verificarPosibleJugada == False:
                    print("Movimiento Invalido")
                else:
                    print("Se ha tirado la carta al centro")

                    for i in range(turnos[0]):
                        if varCartaTirar == turnos[0][i]:
                            del(turnos[0][i])
                            break
                    break
        else:
            break



    acumulacion  = 0 #acumulador para las cartas de +2
    print("Turno de la maquina \n")
    for i in cartas[maso[-1]]:
        print("             ", i)
    BusquedaDeCarta(turnos[0], maso, lista_cartas)
    CambioDeSentido(maso)





   



    

    if len(turnos[0]) == 1:
        break


    print(" ")

    if sentido == True:
        turnos.append(turnos.popleft())
    if sentido == False:
        turnos.appendleft(turnos.pop())

    ##Modificar esto ya que estoy haciendo la comparacion para acceder al indice por medio de del indice 0 y se puede generar error cuando se hace un cambio de sentido ya que la comparacion para pasar si es turno del jugador es con la poscion 0 de el deque turnos

# Faltante
# JOSE
# - Cartas especiales: +2, bloqueo
# SIMON
# - Automatizar turnos y randomizar
