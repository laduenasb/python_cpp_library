from sys import path
path.append("/media/luis/MYLINUXLIVE1/programasl")
from math import *
c1="(Ixx*((cos(u2)-1.0)**2.0+(sin(u4)**2.0)*(sin(u2)**2.0))+Izz*(sin(u2)**2.0)+Ixz*sin(u2)*cos(u4)*(cos(u2)-1.0))"
c2="(Ixx*(cos(u4)**2.0)+Izz)"
c3="(-Ixx*sin(2.0*u4)*sin(u2)+Ixz*sin(u4)*(cos(u2)-1.0))"
c1p="(Ixx*(-2.0*(cos(u2)-1.0)*sin(u2)*u3+2.0*sin(u4)*cos(u4)*u5*(sin(u2)**2.0)+2.0*(sin(u4)**2.0)*sin(u2)*cos(u2)*u3)+2.0*Izz*sin(u2)*cos(u2)*u3+Ixz*(cos(u2)*u3*cos(u4)*(cos(u2)-1.0)+sin(u2)*(-sin(u4)*u5*(cos(u2)-1.0)-cos(u4)*sin(u2)*u3)))"
c2p="(-2.0*Ixx*cos(u4)*sin(u4)*u5)"
c3p="(-Ixx*(2.0*cos(2.0*u4)*u5*sin(u2)+sin(2.0*u4)*cos(u2)*u3)+Ixz*(cos(u4)*u5*(cos(u2)-1.0)-sin(u4)*sin(u2)*u3))"
c1t="(Ixx*(-2.0*(cos(u2)-1.0)*sin(u2)+2.0*(sin(u4)**2.0)*sin(u2)*cos(u2))+2.0*Izz*sin(u2)*cos(u2)+Ixz*(cos(u4)*(cos(u2)*(cos(u2)-1.0)-sin(u2)*sin(u2))))"
c3t="(-Ixx*sin(2.0*u4)*cos(u2)-Ixz*sin(u4)*sin(u2))"
c1f="(Ixx*(2.0*sin(u4)*cos(u4)*(sin(u2)**2.0))-Ixz*sin(u2)*sin(u4)*(cos(u2)-1.0))"
c2f="(-2.0*Ixx*sin(u4)*cos(u4))"
c3f="(-2.0*Ixx*cos(2.0*u4)*sin(u2)+Ixz*cos(u4)*(cos(u2)-1.0))"
Qt="(m*g*xcm*cos(u4)*cos(u2)+m*g*ycm*sin(u4)*cos(u2)+m*g*zcm*sin(u2))"
Qf="(-m*g*xcm*sin(u4)*sin(u2)+m*g*ycm*cos(u4)*sin(u2))"
s="("+c1+"*"+c2+"-(1.0/4.0)*("+c3+"**2.0)"+")"
a1="("+Qf+"-"+c1p+"*u5"+"-"+"0.5*"+c3p+"*u3"+"+"+"0.5*"+"(u5**2.0)"+"*"+c1f+"+"+"0.5*(u3**2.0)*"+c2f+"+"+"0.5*u5*u3*"+c3f+")"
a2="("+Qt+"-"+c2p+"*u3"+"-"+"0.5*"+c3p+"*u5"+"+"+"0.5*(u5**2.0)*"+c1t+"+"+"0.5*u5*u3*"+c3t+")"
f2="("+a1+"*"+c2+"-"+"0.5*"+c3+"*"+a2+")/"+s
t2="("+c1+"*"+a2+"-"+"0.5*"+a1+"*"+c3+")/"+s
U=["u3",t2,"u5",f2]
print s
def det(Ixx,Ixz,Izz,u2,u4):
        f= ((Ixx*((cos(u2)-1.0)**2.0+(sin(u4)**2.0)*(sin(u2)**2.0))+Izz*(sin(u2)**2.0)+Ixz*sin(u2)*cos(u4)*(cos(u2)-1.0))*(Ixx*(cos(u4)**2.0)+Izz)-(1.0/4.0)*((-Ixx*sin(2.0*u4)*sin(u2)+Ixz*sin(u4)*(cos(u2)-1.0))**2.0))
        return f
print det(0.0,0.0,4.0,pi,45650)
