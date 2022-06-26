import random
from collections import deque

print('''                                                             ..',,;;;;;,,'..
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
                                         ';;;;;;;;;;;;;;,  ''')

lista_cartas = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "RB", "RC", "R2", "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "RB", "RC", "R2", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "AB", "AC", "A2", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "AB", "AC", "A2", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "VB", "VC", "V2", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "VB", "VC", "V2", "Z1", "Z2", "Z3", "Z4", "Z5", "Z6", "Z7", "Z8", "Z9", "ZB", "ZC", "Z2", "Z1", "Z2", "Z3", "Z4", "Z5", "Z6", "Z7", "Z8", "Z9", "ZB", "ZC", "Z2"]

def BusquedaDeCarta(turno, cartaCentro, masoRestante):
    encontrada = False
    for carta in turno:
        if carta[0] == cartaCentro[-1][0] or carta[1] == cartaCentro[-1][1]:
            cartaCentro.append(carta)
            turno.remove(carta)
            encontrada = True
            return 1
    if encontrada == False and masoRestante[-1][0] == cartaCentro[-1][0] or masoRestante[-1][1] == cartaCentro[-1][1]:
        cartaCentro.append(masoRestante.pop())
        return 1
    else:
        turno.append(masoRestante.pop())
        return -1



def CartaEspecial(cartaCentro, turnos):
    global sentido
    B = cartaCentro[-1]
    if B[1] == 'C' and sentido == True:
        sentido = False
    elif B[1] == 'C' and sentido == False:
        sentido = True




maso = []

random.shuffle(lista_cartas)

turnos = deque()
turno_1 = []
turno_2 = []
turno_3 = []
turno_4 = []

turno_1.append("turno_1")
turno_2.append("turno_2")
turno_3.append("turno_3")
turno_4.append("turno_4")

turnos.append(turno_1)
turnos.append(turno_2)
turnos.append(turno_3)
turnos.append(turno_4)

for AddCards in range(8):
    turno_1.append(lista_cartas.pop())
    turno_2.append(lista_cartas.pop())
    turno_3.append(lista_cartas.pop())
    turno_4.append(lista_cartas.pop())

maso.append(lista_cartas.pop())
sentido = True
while True:
    if len(lista_cartas) == 0:
        Centro = maso.pop()
        lista_cartas = list(maso)
        maso = []
        maso.append(Centro)
    entrada = str(input())

    BusquedaDeCarta(turnos[0], maso, lista_cartas)
    CartaEspecial(maso, turnos)

    if len(turnos[0]) == 0:
        break

    print(' CARTAS DEL CENTRO ')
    print(" ")
    print(" ")
    print(maso)
    print(" ")
    print(" ")
    for k in turnos:
        print(k)

    print(" ")

    print(maso)
    print(sentido)
    print(lista_cartas)
    if sentido == True:
        turnos.append(turnos.popleft())
    if sentido == False:
        turnos.appendleft(turnos.pop())

# Faltante
# - Cartas especiales: +2, bloqueo
# - Automatizar turnos
