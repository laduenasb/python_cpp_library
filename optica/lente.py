from __future__ import division
from sys import path
path.append("/media/luis/MYLINUXLIVE1/programasl")
from definiciones import *
from sympy import *
t=Symbol("t")
x=Symbol("x")
theta=Symbol("theta")
alpha=1e-10  #### angulo que forma el rayo antes de refractarse con el eje optico, medido en grados 
s=0.5  ### distancia del objeto al vertice de la circunferencia de radio r 
r=3.0  ### radio de la circunferencia
n1=1.0 ### indice de refraccion del medio 1 
n2=1.56 ### indice de refraccion del medio 2
a1=(s+r)*n1*sin(theta)/(r*n2)  ### sin(phip)
a2=sqrt(1.0-a1**2.0)  ### cos(phip)
a3=(s+r)*sin(theta)/r  ### sin(phi)
a4=sqrt(1.0-a3**2.0) ### cos(phi)
a5=a3*cos(theta)-a4*sin(theta) ### sin(beta)
a6=a4*cos(theta)+a3*sin(theta)   ### cos(beta)
a7=(a6*a2+a5*a1)/(a5*a2-a6*a1)   ### cot(beta-phip)
p=r*a5*a7-r*a6+r  ### distancia desde el punto de intercepcion entre rayo refractado con el eje optico, hasta el vertice de la circunferencia
print p.subs(theta,alpha*pi/180.0).evalf() ## posicion de la imagen respecto al vertice de la circunferencia
E1=x**2*(tan(alpha*pi/180.0)**2+1)-2*x*(s+r)+(s+r)**2-r**2 ### puntos de corte entre el rayo y la circunferencia
print solve(E1,x)
print N(1/(((1/r)*(n2-n1)-n1/s)/n2),15) ### punto p con aproximacion paraxial 
print 
y1=minimo(solve(E1,x))*tan(alpha*pi/180.0)
beta=(asin(y1/r)*180.0/pi).evalf() ### en grados
phi=alpha+beta ## en grados
phip=asin(n1*sin(phi*pi/180.0)/n2)*180/pi ## en grados
lp=sqrt(r**2+(p.subs(theta,alpha*pi/180.0)-r)**2-2*r*(r-p.subs(theta,alpha*pi/180.0))*cos(beta*pi/180.0)).evalf()
l=sqrt(r**2+(s+r)**2-2*r*(s+r)*cos(beta*pi/180.0)).evalf()
print ((n2/-lp)+(n1/l)).evalf(),((1/r)*((n2*(-p.subs(theta,alpha*pi/180.0))/lp)-(n1*s/l))).evalf()
