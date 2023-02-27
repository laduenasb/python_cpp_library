### serie de fourier
from matplotlib import pyplot
from math import sin,pi,cos
from sys import path
path.append("/media/luis/MYLINUXLIVE1/programasl")
from definiciones import *
def fourier(n,x):
	a=2.0
	for i in range(1,int(n+1)):
		a+=(-2.0/(i*pi))*sin(i*pi*x)	
	return a
n=100
x=crear_vector(0.0,10.0,10000.0)
y=[]
for i in range(0,len(x)):
	k=fourier(n,x[i])
	y.append(k)	
pyplot.plot(x,y)
pyplot.show()
print crear(x,y)
