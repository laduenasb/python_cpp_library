from sys import path
path.append("/media/luis/MYLINUXLIVE1/programasl")
from definiciones import *
from math import *
t=crear_vector(0,8*pi,1000)
x=[]
for i in range(0,len(t)):
	a=2.0*sin(t[i])
	x.append(a)
print crear(t,x)
