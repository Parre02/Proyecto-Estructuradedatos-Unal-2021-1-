from collections import deque
from random import randint

print("Bienvenido a solitario spider \n Desea jugar un nuevo juego? \n  1 para si \n  2 para no " )


entradan1 = int(input())

if(entradan1 == 1):
    cartas = ('A-P','2-P', '3-P', '4-P', '5-P', '6-P', '7-P', '8-P', '9-P', '10-P', 'J-P', 'Q-P', 'K-P', 
            'A-T', '2-T', '3-T', '4-T', '5-T', '6-T', '7-T', '8-T', '9-T', '10-T', 'J-T', 'Q-T', 'K-T',
            'A-D', '2-D', '3-D', '4-D', '5-D', '6-D', '7-D', '8-D', '9-D', '10-D', 'J-D', 'Q-D', 'K-D', 
            'A-C', '2-C', '3-C', '4-C', '5-C', '6-C', '7-C', '8-C', '9-C', '10-C', 'J-C', 'Q-C', 'K-C')

    a = deque()
    while True:
        ran = randint(0, 51)
        if cartas[ran] not in a:
            a.append(cartas[ran])
        if len(a) == 52:
            break

    ##Columnas 1-7 del juego, son filas    
    b = deque()
    c = deque()
    d = deque()
    e = deque()
    f = deque()
    g = deque()
    h = deque()

    ## Columnas 1-7 del juego, filas cartas descubiertas, 
    b2 = deque()
    c2 = deque()
    d2 = deque()
    e2 = deque()
    f2 = deque()
    g2 = deque()
    h2 = deque()


    variable_con = False

    while len(a) != 24:
        if variable_con == False:
            b.append(a.pop())
            variable_con = True
        elif len(c) != 2:
            c.append(a.pop())
        elif len(d) != 3:
            d.append(a.pop())
        elif len(e) != 4:
            e.append(a.pop())
        elif len(f) != 5:
            f.append(a.pop())
        elif len(g) != 6:
            g.append(a.pop())
        elif len(h) != 7:
            h.append(a.pop())

    Cola_de_arraste_1 = a ## Fila de arraste!! 
    Cola_de_arrastre_2 = deque() ##SACAR DE AQUI!!!
    Cola_de_arrastre_2.append(Cola_de_arraste_1.pop())
    # Inicializacion torres de figuras
    tupla = (b, c, d, e, f, g, h)
    tupla2 = (b2, c2, d2, e2, f2, g2, h2)

    ## Columnas fantasmas, cartas boca arriba
    b2.append(b[-1])
    c2.append(c[-1])
    d2.append(d[-1])
    e2.append(e[-1])
    f2.append(f[-1])
    g2.append(g[-1])
    h2.append(h[-1])

    Torre_P = deque()
    Torre_C = deque()
    Torre_T = deque()
    Torre_D = deque()



    def reiniciar_cola_ararste(): ## Funcion 2 reiniciar cola
        longitud_cola_arraste_2 = len(Cola_de_arrastre_2)
        longitud_cola_arraste = len(Cola_de_arraste_1)
        if(longitud_cola_arraste == 0):
            iterador_cola_arraste_2 = longitud_cola_arraste_2
            print("La cola de arraste se reincia")
            while (iterador_cola_arraste_2 != 0):
                Cola_de_arraste_1.append(Cola_de_arrastre_2.pop())
                iterador_cola_arraste_2 -= 1
            print(Cola_de_arraste_1)
        else:
            print("Aun no se puede ejecutar esta funcionalidad")

    def destapar_cola_arraste(): ##Funcion 1 destapar cola
        longitud_cola_arraste = len(Cola_de_arraste_1)
        if(longitud_cola_arraste>0):
            Carta_del_arraste = Cola_de_arraste_1.pop()
            print(f"La carta que salio es {Carta_del_arraste} ")
            Cola_de_arrastre_2.append(Carta_del_arraste)
        elif(longitud_cola_arraste == 0):
            print("Desea reinciar la cola de arraste? \n 1 para si, 2 para no ")
            Reinicio = int(input())
            if(Reinicio == 1):
                reiniciar_cola_ararste()

    def MoverCartas(tupla, tupla2): ## Funcion N6 Llevar Z cartas de la Columna X a la columna Y Joelle
        desde = int(input("Desde que columna desea mover las cartas? ")) - 1
        hasta = int(input("A que columna desea moverlas? ")) - 1
        N = str(input("Desde que elemento de la columna? "))
        b_t = tuple(tupla[desde])
        if len(tupla[desde]) == 0:
            print("Movimiento invalido")

        cont = 0
        for i in b_t:
            entero = i.split('-')[0]
            if i == N:
                cont += 1                
                if entero == 'A':
                    entero = 1
                elif entero == 'J':
                    entero = 11
                elif entero == 'Q':
                    entero = 12
                elif entero == 'K':
                    entero = 13

                if len(tupla[hasta]) != 0:
                    entero_1 = tupla[hasta][-1].split('-')[0]
                else:
                    entero_1 = 0


                if entero_1 == 'A':
                    entero_1 = 1
                elif entero_1 == 'J':
                    entero_1 = 11
                elif entero_1 == 'Q':
                    entero_1 = 12
                elif entero_1 == 'K':
                    entero_1 = 13 

                if len(tupla[hasta]) != 0:
                    if ('P' in i and 'P' in tupla[hasta][-1]) or ('C' in i and 'C' in tupla[hasta][-1]) or ('D' in i and 'D' in tupla[hasta][-1]) or ('T' in i and 'T' in tupla[hasta][-1]) or ('P' in i and 'T' in tupla[hasta][-1]) or ('T' in i and 'P' in tupla[hasta][-1]) or ('C' in i and 'D' in tupla[hasta][-1]) or ('D' in i and 'C' in tupla[hasta][-1]):
                        print("Movimiento invalido")
                        break

                if int(entero) != int(entero_1) - 1 and entero != 13:
                    print("Movimiento invalido")
                    break
            
            if len(tupla[hasta]) == 0 and entero == 13 and cont == 1:
                tupla[hasta].append(i)
                tupla2[hasta].append(i)
                tupla[desde].pop()
                tupla2[desde].pop()
            elif len(tupla[desde]) != 0 and entero != 13 and cont == 1:
                tupla[hasta].append(i)
                tupla2[hasta].append(i)
                tupla[desde].pop()
                tupla2[desde].pop()
        


        if cont == 0:
            print("Movimiento invalido")

        if len(tupla2[desde]) == 0 and len(tupla[desde]) != 0:
                tupla2[desde].append(tupla[desde][-1])

    def arrastre_a_torre(x): ## Funcionalidad n 3 arrastre de 
        carta = Cola_de_arrastre_2[-1]
        torres = {'P':Torre_P, 'C':Torre_C, 'T':Torre_T, 'D':Torre_D}

        if carta[-1] == x:
            if len(torres[x]) == 0:
                if carta[0] == 'A':
                    torres[x].append(Cola_de_arrastre_2.pop())
                else:
                    print('jugada invalida')
            elif len(torres[x]) != 0:
                carta_2 = torres[x][-1]
                if carta[0] == 'A':
                    print('jugada invalida')
                elif carta[0] == '2' and carta_2[0] == 'A':
                    torres[x].append(Cola_de_arrastre_2.pop())
                elif carta[:2] == '10' and carta_2[0] == '9':
                    torres[x].append(Cola_de_arrastre_2.pop())
                elif carta[0] == 'J' and carta_2[:2] == '10':
                    torres[x].append(Cola_de_arrastre_2.pop())
                elif carta[0] == 'Q' and carta_2[0] == 'J':
                    torres[x].append(Cola_de_arrastre_2.pop())
                elif carta[0] == 'K' and carta_2[0] == 'Q':
                    torres[x].append(Cola_de_arrastre_2.pop())
                elif 2 < int(carta[0]) < 10 and carta_2[0] != 'K' and carta_2[0] != 'Q' and carta_2[0] != 'J' and carta_2[0] != 'A' and carta_2[:2] != '10':
                    if int(carta_2[0]) == int(carta[0]) - 1:
                        torres[x].append(Cola_de_arrastre_2.pop())
                    else:
                        print('jugada invalida')
            else:
                print('jugada invalida')
        else:
            print('jugada invalida')

    def DTYaX(tupla, tupla2, P, C, T, D): ## Funcionalidad N 7
        Torre = str(input("Desde que torre de figuras? "))

        columna = int(input("Hacia que columna? ")) - 1

        if Torre == "P":
            Torre = P
        elif Torre == "C":
            Torre = C
        elif Torre == "T":
            Torre = T
        elif Torre == "D":
            Torre = D
        else:
            return "Movimiento invalido"
        
        entero = Torre[-1].split('-')[0]
        entero_1 = tupla[columna][-1].split('-')[0]

        if entero == 'A':
            entero = 1
        elif entero == 'J':
            entero = 11
        elif entero == 'Q':
            entero = 12
        elif entero == 'K':
            entero = 13 

        if entero_1 == 'A':
            entero_1 = 1
        elif entero_1 == 'J':
            entero_1 = 11
        elif entero_1 == 'Q':
            entero_1 = 12
        elif entero_1 == 'K':
            entero_1 = 13 

        if len(Torre) == 0:
            return "Movimiento invalido"
        elif ('P' in Torre[-1] and 'P' in tupla[columna][-1]) or ('C' in Torre[-1] and 'C' in tupla[columna][-1]) or ('D' in Torre[-1] and 'D' in tupla[columna][-1]) or ('T' in Torre[-1] and 'T' in tupla[columna][-1]) or ('P' in Torre[-1] and 'T' in tupla[columna][-1]) or ('T' in Torre[-1] and 'P' in tupla[columna][-1]) or ('C' in Torre[-1] and 'D' in tupla[columna][-1]) or ('D' in Torre[-1] and 'C' in tupla[columna][-1]):
            return "Movimiento invalido"
        elif int(entero) != int(entero_1) - 1:
            return "Movimiento invalido"
        else:
            tupla[columna].append(Torre[-1])
            tupla2[columna].append(Torre[-1])
            Torre.pop()

    def arrastre_a_columna(Y): ##Funcionalidad N3 
        carta = Cola_de_arrastre_2[-1]
        columnas = {1:b, 2:c, 3:d, 4:e, 5:f, 6:g, 7:h}
        destapadas = {1:b2, 2:c2, 3:d2, 4:e2, 5:f2, 6:g2, 7:h2}

        if len(Cola_de_arrastre_2) == 0:
            print('La cola de arrastre no esta destapada')
            return
        if len(Cola_de_arrastre_2) != 0:        
            carta = Cola_de_arrastre_2[-1]
        if Y > 7:
            print('jugada invalida')
        elif len(columnas[Y]) == 0 and carta[0] == 'K':
            card = Cola_de_arrastre_2.pop()
            columnas[Y].append(card)
            destapadas[Y].append(card)
        elif len(columnas[Y]) != 0:
            carta_2 = columnas[Y][-1]
            if (carta[-1] == 'D' or carta[-1] == 'C') and (carta_2[-1] == 'T' or carta_2[-1] == 'P'):
                if carta[0] == 'K':
                    print('jugada invalida')
                elif carta[:2] == '10' and carta_2[0] == 'J':
                    card = Cola_de_arrastre_2.pop()
                    columnas[Y].append(card)
                    destapadas[Y].append(card)
                elif carta[0] == '9' and carta_2[:2] == '10':
                    card = Cola_de_arrastre_2.pop()
                    columnas[Y].append(card)
                    destapadas[Y].append(card)
                elif carta[0] == 'J' and carta_2[0] == 'Q':
                    card = Cola_de_arrastre_2.pop()
                    columnas[Y].append(card)
                    destapadas[Y].append(card)
                elif carta[0] == 'Q' and carta_2[0] == 'K':
                    card = Cola_de_arrastre_2.pop()
                    columnas[Y].append(card)
                    destapadas[Y].append(card)
                elif carta[0] == 'A' and carta_2[0] == '2':
                    card = Cola_de_arrastre_2.pop()
                    columnas[Y].append(card)
                    destapadas[Y].append(card)
                elif int(carta[0]) < 10 and carta_2[0] != 'K' and carta_2[0] != 'Q' and carta_2[0] != 'J' and carta_2[0] != 'A' and carta_2[:2] != '10':
                    if int(carta_2[0]) == int(carta[0]) + 1:
                        card = Cola_de_arrastre_2.pop()
                        columnas[Y].append(card)
                        destapadas[Y].append(card)
                    else:
                        print('jugada invalida')
                else:
                    print('jugada invalida')
            elif (carta[-1] == 'T' or carta[-1] == 'P') and (carta_2[-1] == 'D' or carta_2[-1] == 'C'):
                if carta[0] == 'K':
                    print('jugada invalida')
                elif carta[:2] == '10' and carta_2[0] == 'J':
                    card = Cola_de_arrastre_2.pop()
                    columnas[Y].append(card)
                    destapadas[Y].append(card)
                elif carta[0] == '9' and carta_2[:2] == '10':
                    card = Cola_de_arrastre_2.pop()
                    columnas[Y].append(card)
                    destapadas[Y].append(card)
                elif carta[0] == 'J' and carta_2[0] == 'Q':
                    card = Cola_de_arrastre_2.pop()
                    columnas[Y].append(card)
                    destapadas[Y].append(card)
                elif carta[0] == 'Q' and carta_2[0] == 'K':
                    card = Cola_de_arrastre_2.pop()
                    columnas[Y].append(card)
                    destapadas[Y].append(card)
                elif carta[0] == 'A' and carta_2[0] == '2':
                    card = Cola_de_arrastre_2.pop()
                    columnas[Y].append(card)
                    destapadas[Y].append(card)
                elif int(carta[0]) < 10 and carta_2[0] != 'K' and carta_2[0] != 'Q' and carta_2[0] != 'J' and carta_2[0] != 'A' and carta_2[:2] != '10':
                    if int(carta_2[0]) == int(carta[0]) + 1:
                        card = Cola_de_arrastre_2.pop()
                        columnas[Y].append(card)
                        destapadas[Y].append(card)
                    else:
                        print('jugada invalida')
                else:
                    print('jugada invalida')
            else:
                print('jugada invalida')

    print(f'El juego se inicializa \n Columnas 1-7 \n Columna 1 {b[-1]} Tiene {len(b)} cartas \n Columna 2 {c[-1]} Tiene {len(c)} cartas \n Columna 3 {d[-1]} Tiene {len(d)} cartas \n Columna 4 {e[-1]} Tiene {len(e)} cartas \n Columna 5 {f[-1]} Tiene {len(f)} cartas \n Columna 6 {g[-1]} Tiene {len(g)} cartas \n Columna 7 {h[-1]} Tiene {len(h)} cartas \n\n En las torres de figuras (P,C,T,D) no hay cartas \n\n En la cola de arrastre hay {Cola_de_arrastre_2[-1]}  \n\n Las picas y treboles son de color Negro, Los corazones y diamentes son de color Rojo' )
    print(a)

    print(tupla)

elif(entradan1 == 2):
    print("Hasta luego ")

while(entradan1 == 1):
    print(f'\nSolitario: \nQue desea hacer? \n\nOpciones: \n 1.Destapar cola de arraste \n 2.Reiniciar cola de arraste \n 3.Llevar de cola de arrastre a Columna Y \n 4.Llevar de cola de arrastre a Torre de figura X (P: Pica, C: Corazón, T: Trébol, D: Diamante) \n 5.Llevar de Columna Y a Torre de figura X \n 6.Llevar Z cartas de la Columna X a la columna Y \n 7.LLevar de la torrre de figura Y a columna X \n 8.Teminar juego  \n 9.Imprimir Tablero  ')
    Opcion = str(input())
    if Opcion == '1' or Opcion == '2' or Opcion == '3' or Opcion == '4' or Opcion == '5' or Opcion == '6' or Opcion == '7' or Opcion == '8' or Opcion == '9':
        Opcion = int(Opcion)
    else:
        print("NO IDIOTA ASI NO ES.")
        Opcion = 0

    if(Opcion == 1):
        destapar_cola_arraste()
    elif(Opcion == 2):
        reiniciar_cola_ararste()
    elif(Opcion == 3):
        print("ingrese la columna, a la cual desea mover: ")
        opcion3_input= int(input())
        arrastre_a_columna(opcion3_input)
    elif(Opcion == 4):
        print("ingrese la torre, a la cual desea mover: ")
        n = input()
        arrastre_a_torre(n)
    elif(Opcion == 5):
        print()
    elif(Opcion == 6):
        MoverCartas(tupla, tupla2)
    elif(Opcion == 7):
        DTYaX(tupla, tupla2, Torre_P, Torre_C, Torre_T, Torre_D)
    elif(Opcion == 8):
        entradan1 = 2
        print("Gracias por jugar hasta luego")
        break
    elif(Opcion == 9):
        print(tuple(Torre_C), tuple(Torre_P), tuple(Torre_T), tuple(Torre_D))

        if len(Cola_de_arrastre_2) != 0:
            print(Cola_de_arrastre_2[-1])
        else:
            print("La cola de arrastre no esta destapada.")

        for i in range(len(tupla2)): 
            print(i+1, ' | '.join(tupla2[i]), "Tiene", len(tupla[i]), "Cartas")
    else:
        print("Funcionalidad elegida invalida")
    # FUNCIONES A EJECUTAR 


    # Destapar cola de arraste Laura / recordar notificar si alguna accion es invalida
    # Reiniciar cola de arraste Laura

    #POR Elegir
    #Llevar de cola de arrastre a Columna Y z Jose
    #Llevar de cola de arrastre a Torre de figura X (P: Pica, C: Corazón, T: Trébol, D: Diamante) Jose
    #Llevar de Columna Y a Torre de figura X Simon
    #Llevar Z cartas de la Columna X a la columna Y Joelle
    #LLevar de la torrre de figura Y a columna X (Ver wtts ED - 11 abril monitor hablo) Joelle
    #Teminar juego Simon listo
    #Imprimir Tablero ## a hacer 
