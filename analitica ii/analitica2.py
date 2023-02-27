##### curvas de fase
from sys import path
path.append("/media/luis/MYLINUXLIVE1/programasl")
from definiciones import *
def funcion1(q,H,m,l,g): ## p(q)  con q el angulo theta
        f=sqrt(2.0*m*(l**2)*(H+m*g*l*cos(q)))
        return f
def velocidadx(p,m,l):
        return float(p)/(float(m*(l**2)))
def velocidady(m,g,l,q):
        return -float(m*g*l*sin(q))
m=1.0
l=1.0
g=9.8
H1=1.0
qa=-84.14*pi/180.0
qb=84.14*pi/180.0
npuntos=100.0
q=crear_vector(qa,qb,npuntos)
pp=[]
pn=[]
qp=[]
qn=[]
## velocidad de fase para hiperbolas verticales
vx=[]
vy=[]
## velocidad de fase para hiperbolas horizontales
qnew=[]
for i in range(0,len(q)):
        pp.append((funcion1(q[i],H1,m,l,g)))
        qnew.append(q[i])
        vx.append((velocidadx(funcion1(q[i],H1,m,l,g),m,l)))
        vy.append((velocidady(m,g,l,q[i])))
for i in range(0,len(q)):
        pp.append(-(funcion1(q[i],H1,m,l,g)))
        qnew.append(q[i])
        vx.append((velocidadx(-funcion1(q[i],H1,m,l,g),m,l)))
        vy.append((velocidady(m,g,l,q[i])))
#pyplot.plot(qnew,pp,"*")
#pyplot.show()
print vertical4(qnew,pp,vx,vy)
