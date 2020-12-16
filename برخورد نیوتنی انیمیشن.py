import pygame as pg
import time as none
from pygame.locals import *
import mehrshad_soheil_math as math
import tkinter as tk
def collision(direct,u1,u2,m1,m2):
    wall_dir=math.cross_product([direct])
    w1,w2 = math.Analytical_2D_vector_into_2_prependicular_directions(u1,wall_dir)
    w3,w4 = math.Analytical_2D_vector_into_2_prependicular_directions(u2,wall_dir)
    v1 = -direct*(w2*((m1-m2)/(m1+m2))+w4*(2*m2/(m1+m2)))+wall_dir*w1
    v2 = -direct*(w2*(2*m1/(m1+m2))+w4*((m2-m1)/(m1+m2)))+wall_dir*w3
    return v1,v2
def get_out_balls(x1,y1,x2,y2,r1,r2,R):
    error=(r1+r2-R)/2+1
    dirx=(x1-x2)/R
    diry=(y1-y2)/R
    return (x1+error*dirx, y1+error*diry, x2-error*dirx, y2-error*diry)
def color(q1,q2):
    c1=(150,150,150)
    c2=c1
    if q1<0:
        c1=(255,0,0)
        if q1>q2:
            c1=(255,150,150)
    if q1>0:
        c1=(0,0,255)
        if q1<q2:
            c1=(150,150,255)
    if q2<0:
        c2=(255,0,0)
        if q2>q1:
            c2=(255,150,150)
    if q2>0:
        c2=(0,0,255)
        if q2<q1:
            c2=(150,150,255)
    return c1,c2
def save1():
    q[0]=float(q_entry[0].get())
    m[0]=float(m_entry[0].get())
    r[0]=int(r_entry[0].get())
    v_x[0]=float(v_x_entry[0].get())
    y[0]=-float(y_entry[0].get())
    flag[0]=True
    print('body 1 properties saved.')
def save2():
    q[1]=float(q_entry[1].get())
    m[1]=float(m_entry[1].get())
    r[1]=int(r_entry[1].get())
    v_x[1]=-float(v_x_entry[1].get())
    y[1]=-float(y_entry[1].get())
    flag[1]=True
    print('body 2 proberties saved.')
win=[0,0]
q=[0,0]
q_entry=[0,0]
m=[0,0]
m_entry=[0,0]
r=[0,0]
r_entry=[0,0]
v_x=[0,0]
v_x_entry=[0,0]
y=[0,0]
y_entry=[0,0]
button=[0,0]
flag=[False,False]
while not all(flag):
    for i in range(2):
        if flag[i]:
            continue
        win[i]=tk.Tk()
        win[i].geometry('200x300+'+str(75+300*i)+'+75')
        win[i].title('body '+str(i+1)+' details')
        win[i].maxsize(300,500)
        w=tk.Label(win[i],text='Hello')
        w.pack()
        #q
        f=tk.Frame(win[i])
        f.pack(side='top',fill='x')
        tk.Label(f,text='Charge :').pack(side='left')
        q_entry[i]=tk.Entry(f,width=1000)
        q_entry[i].pack(side='right',padx=10)
        #m
        f=tk.Frame(win[i])
        f.pack(side='top',fill='x')
        tk.Label(f,text='Mass :').pack(side='left')
        m_entry[i]=tk.Entry(f,width=1000)
        m_entry[i].pack(side='right',padx=10)
        #r
        f=tk.Frame(win[i])
        f.pack(side='top',fill='x')
        tk.Label(f,text='Radius :').pack(side='left')
        r_entry[i]=tk.Entry(f,width=1000)
        r_entry[i].pack(side='right',padx=10)
        #v
        # body2:0
        f=tk.Frame(win[i])
        f.pack(side='top',fill='x')
        tk.Label(f,text='v_x :').pack(side='left')
        v_x_entry[i]=tk.Entry(f,width=1000)
        v_x_entry[i].pack(side='right',padx=10)
        #y
        # body2:0
        f=tk.Frame(win[i])
        f.pack(side='top',fill='x')
        tk.Label(f,text='y :').pack(side='left')
        y_entry[i]=tk.Entry(f,width=1000)
        y_entry[i].pack(side='right',padx=10)
        #
        button[i]=tk.Button(win[i],text='done',command=[save1,save2][i])
        button[i].pack()
    if not flag[0]:
        v_x_entry[0].insert(0,'150')
    if not flag[1]:
        v_x_entry[1].insert(0,'0')
        y_entry[1].insert(0,'0')
    tk.mainloop()
q1,q2=q
m1,m2=m
r1,r2=r
y1,y2=y
G=6.6740831e-11
K=8.98e+9
x1=-100
x2=300
B=float(input('External magnetic field = '))
c1,c2=color(q1,q2)
v1=math.Vector2Ds([v_x[0],0])
v2=math.Vector2Ds([v_x[1],0])
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
    R=math.sqrt((x2-x1)**2+(y[1]-y[0])**2)
    a1=G*m2/R**2
    a2=G*m1/R**2
    F1=(math.cross_product([v1])*B+math.Vector2Ds([x1-x2,y1-y2])*K*q2/R**3)*q1
    F2=(math.cross_product([v2])*B+math.Vector2Ds([x2-x1,y2-y1])*K*q1/R**3)*q2
    v1+=(math.Vector2Ds([a1*(x2-x1)/R,a1*(y2-y1)/R])+F1/m1)*dt
    v2+=(math.Vector2Ds([a2*(x1-x2)/R,a2*(y1-y2)/R])+F2/m2)*dt
    if R<r1+r2:
        v1,v2=collision(math.direction2Ds([x1-x2,y1-y2]),v1,v2,m1,m2)
        x1,y1,x2,y2 = get_out_balls(x1,y1,x2,y2,r1,r2,R)
    x1+=v1[0]*dt
    x2+=v2[0]*dt
    y1+=v1[1]*dt
    y2+=v2[1]*dt
    #draws
    sc.fill((255,255,255))
    pg.draw.circle(sc,c1,(int(x1),300+int(y1)),r1)
    pg.draw.circle(sc,c2,(int(x2),300+int(y2)),r2)
    pg.display.update()
