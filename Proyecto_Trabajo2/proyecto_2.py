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

"V7":("+_________+", "|7   Verde|", "|         |", "|         |", "|    7    |", "|         |", "|        7|", "+---------+"), 

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

random.shuffle(turnos) #O(n*n)


# maso agrega una carta aleatoria que es con la que se va a comenzar el juego
maso.append(lista_cartas.pop()) 
sentido = True


########################################################################################################################



# Busqueda de carta que pueda servir por turno.
def BusquedaDeCarta(turno, cartaCentro, masoRestante): ## Esta funcion tiene eficiencia segun notacionBigOh O(n)
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
    
    elif cartaCentro[-1][-1] == '+':
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
            print("De las cartas restantes se ha tomado una carta automaticamente y como esta carta es valida se puso en el centro.")
            return 1
        else:
            print("Se ha tomado una carta automaticamente de las cartas restantes y se te agrego a tu maso.")
            turno.append(masoRestante.pop())
            return -1

#funcion de cambio de sentido
def CambioDeSentido(cartaCentro): ## Esta funcion tiene eficiencia segun notacionBigOh O(n)
    global sentido
    # B en este caso es para identificar si la carta es especial osea si contiene (C, B, 2)
    # Cambio de sentido
    B = cartaCentro[-1]
    if B[1] == 'C' and sentido == True: #Sentido horario
        sentido = False
    elif B[1] == 'C' and sentido == False: #Sentido Antihorario
        sentido = True

        
def VerificarListaDeArrastre(): ##Esta funcion es O(1)
    global lista_cartas
    global maso
    global Centro
    if len(lista_cartas) == 0:
        Centro = maso.pop()
        lista_cartas = list(maso)
        maso = []
        maso.append(Centro)


while True: ## BigOh indefinida ya que tiene en cuenta la probablidad de cartas 
    # Si el maso de cartas restantes se queda en 0 este se reemplaza por el maso de cartas que no estas en posesion de ningun jugador
    if len(lista_cartas) == 0:
        Centro = maso.pop()
        lista_cartas = list(maso)
        maso = []
        maso.append(Centro)
    
    verificarSiSeArrastro = False
    verificarPosibleJugada = False


    ##Impresion de la carta del centro
    print("Turno de la maquina \n")
    for i in cartas[maso[-1]]:
        print("             ", i)


    while True:
        if turnos[0] == turno_1:
            print("Menu del jugador")
            print("Opciones:")
            print("  1.Ver cartas en mi maso")
            print("  2.Ver la carta del centro")
            print("  3.Tirar carta")
            print(" ")

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
                print(' CARTAS DEL CENTRO ')
                print(" ")
                print(" ")
                for i in cartas[maso[-1]]:
                    print(i)
                print(" ")
                print(" ")
            elif entrada == 3:
                print("Para escoger una carta cuando imprime el maso de cartas que le corresponde a cada\ncarta se le asigna un indice, debe escribir el indice de la carta que desea escoger.\n Si no encuentra un indice coloque cualquier numero")
                print("\nQue carta desea tirar?")
                varCartaTirar = int(input())
                if maso[-1][0] == turnos[0][varCartaTirar-1][0] or maso[-1][-1] == turnos[0][varCartaTirar-1][-1]:
                    maso.append(turnos[0].pop(varCartaTirar-1))
                    break
                else:
                    print("Movimiento invalido")
                    print("Se ha movido una carta valida automaticamente")
                    BusquedaDeCarta(turnos[0], maso, lista_cartas)
                    break
        else:
            break

    acumulacion  = 0 #acumulador para las cartas de +2

    BusquedaDeCarta(turnos[0], maso, lista_cartas)
    CambioDeSentido(maso)

    #Impresion de la carta del centro


    if len(turnos[0]) == 0:
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
