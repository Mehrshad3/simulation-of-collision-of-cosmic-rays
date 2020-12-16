import pygame as pg
import time as none
from pygame.locals import *
def collision(u1,u2,m1,m2):
    v=(u1*m1+u2*m2)/(m1+m2)
    u_1=u1-v
    u_2=u2-v
    return -u_1+v,-u_2+v
x1=-100
x2=300
m1=float(input('m1 =  '))
m2=float(input('m2 =  '))
r1=int(input('r1 =  '))
r2=int(input('r2 =  '))
v1=150
v2=0
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
    if x2-x1<r2+r1:
        v1,v2=collision(v1,v2,m1,m2)
    x1+=v1*dt
    x2+=v2*dt
    #draws
    sc.fill((50,100,200))
    pg.draw.circle(sc,(0,0,0),(int(x1),300),r1)
    pg.draw.circle(sc,(0,0,0),(int(x2),300),r2)
    pg.display.update()
