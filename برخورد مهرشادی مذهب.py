import pygame as pg
import time as none
from pygame.locals import *
import mehrshad_soheil_math as math
def collision(direct,u1,u2,m1,m2):
    wall_dir=math.direction2Ds([-direct[1],direct[0]])
    w1,w2 = math.Analytical_2D_vector_into_2_prependicular_directions(u1,wall_dir)
    v1 = direct*w2*((m1-m2)/(m1+m2)) - wall_dir*w1
    v2 = direct*w1*(2*m1/(m1+m2))
    return v1,v2
x1=-100
x2=300
y1=-float(input('impact factor = '))
y2=0
m1=float(input('m1 =  '))
m2=float(input('m2 =  '))
r1=int(input('r1 =  '))
r2=int(input('r2 =  '))
v1=math.Vector2Ds([150,0])
v2=math.Vector2Ds([0,0])
sc=pg.display.set_mode((800,600))
t0=none.time()
while True:
    for event in pg.event.get():
        if event.type==QUIT:
            pg.quit()
            raise SystemExit
    # updates
    t1=none.time()
    dt=t1-t0
    t0=t1
    if (x2-x1)**2+(y2-y1)**2<(r2+r1)**2:
        v1,v2=collision(math.direction2Ds([x1-x2,y1-y2]),v1,v2,m1,m2)
    x1+=v1[0]*dt
    x2+=v2[0]*dt
    y1+=v1[1]*dt
    y2+=v2[1]*dt
    #draws
    sc.fill((50,100,200))
    pg.draw.circle(sc,(0,0,0),(int(x1),300+int(y1)),r1)
    pg.draw.circle(sc,(0,0,0),(int(x2),300+int(y2)),r2)
    pg.display.update()
