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

    tupla = (b, c, d, e, f, g, h)
    tupla2 = (b2, c2, d2, e2, f2, g2, h2)
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

    ## Columnas fantasmas, cartas boca arriba
    b2.append(b[-1])
    c2.append(c[-1])
    d2.append(d[-1])
    f2.append(f[-1])
    g2.append(g[-1])
    h2.append(h[-1])

    Torre_P = deque()
    Torre_C = deque()
    Torre_T = deque()
    Torre_D = deque()



    def reiniciar_cola_ararste(): ## Funcion 2 reiniciar cola
        longitud_cola_arraste_2 = len(Cola_de_arrastre_2)
        iterador_cola_arraste_2 = longitud_cola_arraste_2
        print("La cola de arraste se reincia")
        while (iterador_cola_arraste_2 != 0):
            Cola_de_arraste_1.append(Cola_de_arrastre_2.pop())
            iterador_cola_arraste_2 -= 1
        print(Cola_de_arraste_1)

    def destapar_cola_arraste(): ##Funcion 1 destapar cola
        longitud_cola_arraste = len(Cola_de_arraste_1)
        if(longitud_cola_arraste>0):
            Carta_del_arraste = Cola_de_arraste_1.pop()
            print(f"La carta que salio es {Carta_del_arraste} ")
            Cola_de_arrastre_2.append(Carta_del_arraste)
            print("Carta encima ")
        elif(longitud_cola_arraste == 0):
            print("Desea reinciar la cola de arraste? \n 1 para si, 2 para no ")
            Reinicio = int(input())
            if(Reinicio == 1):
                reiniciar_cola_ararste()

    def MoverCartas(tupla, tupla2):
        desde = int(input("Desde que columna desea mover las cartas? ")) - 1
        hasta = int(input("A que columna desea moverlas? ")) - 1
        N = str(input("Desde que elemento de la columna? "))
        b_t = tuple(tupla[desde])
        if len(tupla[desde]) == 0:
            print("Movimiento invalido")

        cont = 0
        for i in b_t:
            if i == N:
                cont += 1
                entero = i.split('-')[0]
                entero_1 = tupla[hasta][-1].split('-')[0]
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

                if ('P' in i and 'P' in tupla[hasta][-1]) or ('C' in i and 'C' in tupla[hasta][-1]) or ('D' in i and 'D' in tupla[hasta][-1]) or ('T' in i and 'T' in tupla[hasta][-1]) or ('P' in i and 'T' in tupla[hasta][-1]) or ('T' in i and 'P' in tupla[hasta][-1]) or ('C' in i and 'D' in tupla[hasta][-1]) or ('D' in i and 'C' in tupla[hasta][-1]):
                    print("Movimiento invalido")
                    break
                if int(entero) != int(entero_1) - 1:
                    print("Movimiento invalido")
                    break
                
                if cont == 1:
                    tupla[hasta].append(i)
                    tupla2[hasta].append(i)
                    tupla[desde].pop()
                    tupla[desde].pop()
                else:
                    print("Movimiento invalido")

    def arrastre_a_torre(x):
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

    print(f'El juego se inicializa \n Columnas 1-7 \n Columna 1 {b[-1]} Tiene {len(b)} cartas \n Columna 2 {c[-1]} Tiene {len(c)} cartas \n Columna 3 {d[-1]} Tiene {len(d)} cartas \n Columna 4 {e[-1]} Tiene {len(e)} cartas \n Columna 5 {f[-1]} Tiene {len(f)} cartas \n Columna 6 {g[-1]} Tiene {len(g)} cartas \n Columna 7 {h[-1]} Tiene {len(h)} cartas \n\n En las torres de figuras (P,C,T,D) no hay cartas \n\n En la cola de arrastre hay {Cola_de_arrastre_2[-1]}  \n\n Las picas y treboles son de color Negro, Los corazones y diamentes son de color Rojo' )
    print(a)

    print(tupla)

elif(entradan1 == 2):
    print("Hasta luego ")

for i in range(len(tupla)):
    print(i+1, tupla[i])

MoverCartas(tupla, tupla2)


while(entradan1 == 1):
    Opcion = int(input())
    print(f'')
    if(Opcion == 1):
        destapar_cola_arraste()
    elif(Opcion == 2):
        print()
    elif(Opcion == 3):
        print()
    elif(Opcion == 4):
        print()
    elif(Opcion == 5):
        print()
    elif(Opcion == 6):
        print()
    elif(Opcion == 7):
        print()
    elif(Opcion == 8):
        break
    elif(Opcion == 9):
        print()
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
    # Imprimir Tablero ## a hacer 
