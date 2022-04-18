from collections import deque
from random import randint
from re import A



print("Bienvenido a solitario spider \n Desea jugar un nuevo juego? \n  1 para si \n  2 para no " )


entradan1 = int(input())
if(entradan1 == 1):
    cartas = ('A-P','2-P', '3-P', '4-P', '5-P', '6-P', '7-P', '8-P', '9-P', '10-P', 'J-P', 'Q-P', 'K-P', 
            'A-T', '2-T', '3-T', '4-T', '5-T', '6-T', '7-T', '8-T', '9-T', '10-T', 'J-T', 'Q-T', 'K-T',
            'A-D', '2-D', '3-D', '4-D', '5-D', '6-D', '7-D', '8-D', '9-D', '10-D', 'J-D', 'Q-D', 'K-D', 
            'A-C', '2-C', '3-C', '4-C', '5-C', '6-C', '7-C', '8-C', '9-C', '10-C', 'J-C', 'Q-C', 'K-C')

    a = deque()
    while True:
        ran = randint(1, 52)
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

    ## Columnas 1-7 del juego, filas cartas descubiertas
    b1 = deque()
    c2 = deque()
    d2 = deque()
    e2 = deque()
    f2 = deque()
    g2 = deque()
    h2 = deque()

    variable_con = False

    tupla = (b, c, d, e, f, g, h)

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



        


    print(f'El juego se inicializa \n Columnas 1-7 \n Columna 1 {b[-1]} Tiene {len(b)} cartas \n Columna 2 {c[-1]} Tiene {len(c)} cartas \n Columna 3 {d[-1]} Tiene {len(d)} cartas \n Columna 4 {e[-1]} Tiene {len(e)} cartas \n Columna 5 {f[-1]} Tiene {len(f)} cartas \n Columna 6 {g[-1]} Tiene {len(g)} cartas \n Columna 7 {h[-1]} Tiene {len(h)} cartas \n\n En las torres de figuras (P,C,T,D) no hay cartas \n\n En la cola de arrastre hay {Cola_de_arrastre_2[-1]}  \n\n Las picas y treboles son de color Negro, Los corazones y diamentes son de color Rojo' )
    print(a)

    print(tupla)

elif(entradan1 == 2):
    print("Hasta luego ")





while(entradan1 == 1):
   

   
    Opcion = int(input())
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
        print()
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
    #Teminar juego Simon
    # Imprimir Tablero ## a hacer 






