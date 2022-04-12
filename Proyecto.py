from collections import deque
from random import randint

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

print(a)

print(tupla)










