########### Runge kutta ecuaciones diferenciales orden n
#-*-coding:utf-8-*-
from sys import path
path.append("/media/luis/MYLINUXLIVE1/programasl")
from definiciones import *
from matplotlib.pyplot import *
from matplotlib import pyplot
from math import sin,pi
xa=0.0   ##### años 
xb=10.0
n_puntos=1001.0
h=(xb-xa)/(n_puntos-1.0)
t=[xa]
for i in range(0,int(n_puntos)-1):
        xa+=h
        t.append(xa)
xa=0.0
def funcion_1(t,w1,w2,w3,w4):   #### dx/dt
        h=w2
        return h
def funcion_2(t,w1,w2,w3,w4):
        h=(-4*(pi**2.0)*w1)/((w1**2.0+w3**2.0)**1.5)
        return h
def funcion_3(t,w1,w2,w3,w4):
        h=w4
        return h
def funcion_4(t,w1,w2,w3,w4):
	h=(-4*(pi**2.0)*w3)/((w1**2.0+w3**2.0)**1.5)
        return h
w1=1.392 
w2=0.0
w3=0.0
w4=5.573
print "tiempo","X=w1","w2","Y=w3","w4"
print xa,w1,w2,w3,w4
x=[w1]
y=[w2]
z=[w3]
k=[w4]
for j in range(1,len(t)):
        k11=h*funcion_1(t[j-1],w1,w2,w3,w4)
        k12=h*funcion_2(t[j-1],w1,w2,w3,w4)
	k13=h*funcion_3(t[j-1],w1,w2,w3,w4)
	k14=h*funcion_4(t[j-1],w1,w2,w3,w4)
        k21=h*funcion_1(t[j-1]+0.5*h,w1+0.5*k11,w2+0.5*k12,w3+0.5*k13,w4+0.5*k14)
        k22=h*funcion_2(t[j-1]+0.5*h,w1+0.5*k11,w2+0.5*k12,w3+0.5*k13,w4+0.5*k14)
	k23=h*funcion_3(t[j-1]+0.5*h,w1+0.5*k11,w2+0.5*k12,w3+0.5*k13,w4+0.5*k14)
	k24=h*funcion_4(t[j-1]+0.5*h,w1+0.5*k11,w2+0.5*k12,w3+0.5*k13,w4+0.5*k14)
        k31=h*funcion_1(t[j-1]+0.5*h,w1+0.5*k21,w2+0.5*k22,w3+0.5*k23,w4+0.5*k24)
        k32=h*funcion_2(t[j-1]+0.5*h,w1+0.5*k21,w2+0.5*k22,w3+0.5*k23,w4+0.5*k24)
	k33=h*funcion_3(t[j-1]+0.5*h,w1+0.5*k21,w2+0.5*k22,w3+0.5*k23,w4+0.5*k24)
	k34=h*funcion_4(t[j-1]+0.5*h,w1+0.5*k21,w2+0.5*k22,w3+0.5*k23,w4+0.5*k24)
        k41=h*funcion_1(t[j-1]+h,w1+k31,w2+k32,w3+k33,w4+k34)
        k42=h*funcion_2(t[j-1]+h,w1+k31,w2+k32,w3+k33,w4+k34)
	k43=h*funcion_3(t[j-1]+h,w1+k31,w2+k32,w3+k33,w4+k34)
	k44=h*funcion_4(t[j-1]+h,w1+k31,w2+k32,w3+k33,w4+k34)
        w1=w1+(1.0/6.0)*(k11+2*k21+2*k31+k41)
        w2=w2+(1.0/6.0)*(k12+2*k22+2*k32+k42)
	w3=w3+(1.0/6.0)*(k13+2*k23+2*k33+k43)
	w4=w4+(1.0/6.0)*(k14+2*k24+2*k34+k44)
	x.append(w1)
	y.append(w2)
	z.append(w3)
	k.append(w4)
        print t[j],w1,w2,w3,w4
pyplot.plot(x,z,".")
pyplot.show()
print crear(x,z)


