from sys import path
path.append("/media/luis/MYLINUXLIVE1/programasl")
from definiciones import *
init_printing()
x,y,f,t,s=symbols("x,y,f,t,s")
### primera rotacion
u1=[cos(s),sin(s),0]
v1=[-sin(s),cos(s),0]
w1=[0,0,1]
D=[u1,v1,w1] ### matriz de rotacion
### segunda rotacion
u2=[1,0,0]
v2=[0,cos(t),sin(t)]
w2=[0,-sin(t),cos(t)]
C=[u2,v2,w2]
### tercera rotacion
u3=[cos(f),sin(f),0]
v3=[-sin(f),cos(f),0]
w3=[0,0,1]
B=[u3,v3,w3]
#### matriz de rotacion BCD
A=producto(B,producto(C,D))
