from collections import deque
from random import randint



print("Bienvenido a solitario spider \n Desea jugar un nuevo juego? \n  1 para si \n  2 para no " )


entradan1 = int(input())
if(entradan1 == 1):
    cartas = ('A-P', '1-P', '2-P', '3-P', '4-P', '5-P', '6-P', '7-P', '8-P', '9-P', '10-P', 'J-P', 'Q-P', 'K-P', 
            'A-T', '1-T', '2-T', '3-T', '4-T', '5-T', '6-T', '7-T', '8-T', '9-T', '10-T', 'J-T', 'Q-T', 'K-T',
            'A-D', '1-D', '2-D', '3-D', '4-D', '5-D', '6-D', '7-D', '8-D', '9-D', '10-D', 'J-D', 'Q-D', 'K-D', 
            'A-C', '1-C', '2-C', '3-C', '4-C', '5-C', '6-C', '7-C', '8-C', '9-C', '10-C', 'J-C', 'Q-C', 'K-C')

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

    Cola_de_arraste = a ## Fila de arraste!!

    # Inicializacion torres de figuras

    Torre_P = deque()
    Torre_C = deque()
    Torre_T = deque()
    Torre_D = deque()


    print(f'El juego se inicializa \n Columnas 1-7 \n Columna 1 {b[-1]} Tiene {len(b)} cartas \n Columna 2 {c[-1]} Tiene {len(c)} cartas \n Columna 3 {d[-1]} Tiene {len(d)} cartas \n Columna 4 {e[-1]} Tiene {len(e)} cartas \n Columna 5 {f[-1]} Tiene {len(f)} cartas \n Columna 6 {g[-1]} Tiene {len(g)} cartas \n Columna 7 {h[-1]} Tiene {len(h)} cartas \n\n En las torres de figuras (P,C,T,D) no hay cartas \n\n En la cola de arraste no hay cartas destapadas \n\n Las picas y treboles son de color Negro, Los corazones y diamentes son de color Rojo' )

    print(a)

    print(tupla)

elif(entradan1 == 2):
    print("Hasta luego ")



Varialbe_controlsalida = False
while(entradan1 == 1 and variable_con == False):
    entradan1 == 2
    Varialbe_controlsalida = True
    
    # FUNCIONES A EJECUTAR 


    # Destapar cola de arraste Laura / recordar notificar si alguna accion es invalida
    # Reiniciar cola de arraste Laura




  
## POR Elegir
  #Llevar de cola de arrastre a Columna Y z
  #Llevar de cola de arrastre a Torre de figura X (P: Pica, C: Corazón, T: Trébol, D: Diamante)
  #Llevar de Columna Y a Torre de figura X
  #Llevar Z cartas de la Columna X a la columna Y 
  #LLevar de la torrre de figura Y a columna X (Ver wtts ED - 11 abril monitor hablo)








