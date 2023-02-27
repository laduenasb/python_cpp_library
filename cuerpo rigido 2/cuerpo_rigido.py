######### Ecuaciones del cuerpo rigido usando angulos de euler 
from sys import path
path.append("/media/luis/MYLINUXLIVE1/programasl")
from definiciones import * 
init_printing()
u1,u2,u3,u4,u5,u6,u7=symbols("u1,u2,u3,u4,u5,u6,u7")
x,y,z=symbols("x,y,z")
m=10.0
g=9.8
xcm=0.0
ycm=0.0
zcm=6.0
I1=1200.0
I2=1500.0
T=(I1/2.0)*(u3**2*(sin(u4)**2)+u5**2)+(I2/2.0)*(u3*cos(u4)+u7)**2
T=substituir_t(T,7)
r=[x,y,z]
l1=[0,0,1]
l2=[1,0,0]
Qt=m*g*zcm*sin(u4(u1))-m*g*xcm*sin(u6(u1))*cos(u4(u1))-m*g*ycm*cos(u6(u1))*cos(u4(u1))
Qph=0
Qps=-m*g*xcm*cos(u6(u1))*sin(u4(u1))+m*g*ycm*sin(u6(u1))*sin(u4(u1))
E1=diff(diff(T,u3(u1)),u1)-diff(T,u2(u1))-Qph
E2=diff(diff(T,u5(u1)),u1)-diff(T,u4(u1))-Qt
E3=diff(diff(T,u7(u1)),u1)-diff(T,u6(u1))-Qps
M=[E1,E2,E3]
#print (solve(M,[diff(u3(u1),u1),diff(u5(u1),u1),diff(u7(u1),u1)]))
u3p=((-2.0*I1*u3(u1)*cos(u4(u1)) + 2.0*I2*u3(u1)*cos(u4(u1)) + I2*u7(u1))*u5(u1) - (I2*u3(u1)*u5(u1) - g*m*xcm*cos(u6(u1)) + g*m*ycm*sin(u6(u1)))*cos(u4(u1)))/(I1*sin(u4(u1)))
u5p=(0.5*I1*u3(u1)**2*sin(2.0*u4(u1)) - 0.5*I2*u3(u1)**2*sin(2.0*u4(u1)) - I2*u3(u1)*u7(u1)*sin(u4(u1)) - g*m*xcm*sin(u6(u1))*cos(u4(u1)) - g*m*ycm*cos(u4(u1))*cos(u6(u1)) + g*m*zcm*sin(u4(u1)))/I1
u7p=(-I2*(-2.0*I1*u3(u1)*cos(u4(u1)) + 2.0*I2*u3(u1)*cos(u4(u1)) + I2*u7(u1))*cos(u4(u1))*u5(u1) + (I1*sin(u4(u1))**2 + I2*cos(u4(u1))**2)*(I2*u3(u1)*u5(u1) - g*m*xcm*cos(u6(u1)) + g*m*ycm*sin(u6(u1))))/(I1*I2*sin(u4(u1)))
u3p=rsubstituir_t(u3p,7)
u5p=rsubstituir_t(u5p,7)
u7p=rsubstituir_t(u7p,7)
U=["u3",str(u3p),"u5",str(u5p),"u7",str(u7p)]
w=[0.0,0.0,pi/6.0,0.0,0.0,2.0]
h=0.1
de=4
xa=0.0
xb=10.0
print Runge_kutta_sm(U,w,xa,xb,de,h)
