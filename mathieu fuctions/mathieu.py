from sys import path
path.append("/media/luis/MYLINUXLIVE1/programasl")
from definiciones import *
from scipy import special
from math import *
x=crear_vector(-2,2,50)
y=crear_vector(-2,2,50)
x1=[]
y1=[]
z1=[]
def m(x,y):
	return special.mathieu_sem(4,1.5,x*180/pi)[0]*special.mathieu_cem(1,1.5,y*180/pi)[0]	
for i in range(0,len(x)):
	for j in range(0,len(y)):
		x1.append(x[i])
		y1.append(y[j])
		z1.append(m(x[i],y[j]))
print vertical3(x1,y1,z1)
