from sys import path
path.append("/media/luis/MYLINUXLIVE1/programasl")
from definiciones import *
xk,yk,zk,t,xcm,ycm,zcm,m,g,Ixx,Iyy,Izz,Ixy,Ixz,Iyz,Ix,Iz=symbols("xk,yk,zk,t,xcm,ycm,zcm,m,g,Ixx,Iyy,Izz,Ixy,Ixz,Iyz,Ix,Iz")
def substituiru(S1,nv):
        S=[]
        for i in range(0,len(S1)):
                S.append(S1[i].subs(diff(u2(u1),u1),u3(u1)))
                S[i]=S[i].subs(diff(u4(u1),u1),u5(u1))
                S[i]=S[i].subs(diff(u6(u1),u1),u7(u1))
                S[i]=rsubstituir_t(S[i],nv)
        return S
def substituirun(S1,nv):
        S=[]
        for i in range(0,len(S1)):
                S.append(S1[i].subs(diff(u2(u1),u1),u3(u1)))
                S[i]=S[i].subs(diff(u4(u1),u1),u5(u1))
                S[i]=S[i].subs(diff(u6(u1),u1),u7(u1))
        return S
nv=7
T1=R(1,2)*Ix*(u3(u1)**2*sin(u4(u1))**2+u5**2)+R(1,2)*Iz*(u3(u1)*cos(u4(u1))+u7**2)**2
T2=substituir_t(T1,nv)
T1u2=diff(T2,u2(u1))
T1u4=diff(T2,u4(u1))
T1u6=diff(T2,u6(u1))
T1u3p=diff(diff(T2,u3(u1)),u1)
T1u5p=diff(diff(T2,u5(u1)),u1)
T1u7p=diff(diff(T2,u7(u1)),u1)
Qu2=-m*g*xcm*cos(u2(u1))*sin(u4(u1))+m*g*ycm*sin(u2(u1))*sin(u4(u1))
Qu4=m*g*zcm*sin(u4(u1))-m*g*xcm*sin(u2*(u1))*cos(u4(u1))-m*g*ycm*cos(u2(u1))*cos(u4(u1))
Qu6=0.0
E1=substituirun([T1u3p-T1u2-Qu2],nv)
E2=substituirun([T1u5p-T1u4-Qu4],nv)
E3=substituirun([T1u7p-T1u6-Qu6],nv)
#Q=solve([E1[0],E2[0],E3[0]], [diff(u3(u1),u1),diff(u5(u1)),diff(u7(u1),u1)], dict=True)
#E1=collect(collect(collect(expand(E1[0]),diff(u3(u1),u1)),diff(u5(u1),u1)),diff(u7(u1),u1))
#E2=collect(collect(collect(expand(E2[0]),diff(u3(u1),u1)),diff(u5(u1),u1)),diff(u7(u1),u1))
#E3=collect(expand(E3[0]),diff(u3(u1),u1))
#E1=[E1.coeff(diff(u3(u1),u1)),E1.coeff(diff(u5(u1),u1)),E1.coeff(diff(u7(u1),u1)),-(E1-E1.coeff(diff(u3(u1),u1))*diff(u3(u1),u1)-E1.coeff(diff(u7(u1),u1))*diff(u7(u1),u1))]
#E2=[E2.coeff(diff(u3(u1),u1)),E2.coeff(diff(u5(u1),u1)),E2.coeff(diff(u7(u1),u1)),-(E2-E2.coeff(diff(u5(u1),u1))*diff(u5(u1),u1))]
#E3=[E3.coeff(diff(u3(u1),u1)),E3.coeff(diff(u5(u1),u1)),E3.coeff(diff(u7(u1),u1)),-(E3-E3.coeff(diff(u3(u1),u1))*diff(u3(u1),u1)-E3.coeff(diff(u5(u1),u1))*diff(u5(u1),u1)-E3.coeff(diff(u7(u1),u1))*diff(u7(u1),u1))]
####
#E1=[rsubstituir_t(E1[0],nv),rsubstituir_t(E1[1],nv),rsubstituir_t(E1[2],nv),rsubstituir_t(E1[3],nv)]
#E2=[rsubstituir_t(E2[0],nv),rsubstituir_t(E2[1],nv),rsubstituir_t(E2[2],nv),rsubstituir_t(E2[3],nv)]
#E3=[rsubstituir_t(E3[0],nv),rsubstituir_t(E3[1],nv),rsubstituir_t(E3[2],nv),rsubstituir_t(E3[3],nv)]
#M=[E1,E2,E3]
#S=cramer(M)
#S1=[simplify(cancel(S[0])),simplify(cancel(S[1])),simplify(cancel(S[2]))]
u3p=rsubstituir_t((2*Iz*u3(u1)*u5(u1)*u7(u1)**2*cos(u4(u1)) - (u3(u1)*cos(u4(u1)) + 3*u7(u1)**2)*(-2*Ix*u3(u1)*u5(u1)*cos(u4(u1)) + 2*Iz*u3(u1)*u5(u1)*cos(u4(u1)) + Iz*u5(u1)*u7(u1)**2 - g*m*xcm*cos(u2(u1)) + g*m*ycm*sin(u2(u1))))*sin(u4(u1))/(2*Iz*u7(u1)**2*cos(u4(u1))**2 - (Ix*sin(u4(u1))**2 + Iz*cos(u4(u1))**2)*(u3(u1)*cos(u4(u1)) + 3*u7(u1)**2)),nv)
u5p=rsubstituir_t((Ix*u3(u1)**2*sin(2*u4(u1))/2 - Iz*u3(u1)**2*sin(2*u4(u1))/2 - Iz*u3(u1)*u7(u1)**2*sin(u4(u1)) - g*m*xcm*sin(u1*u2)*cos(u4(u1)) - g*m*ycm*cos(u2(u1))*cos(u4(u1)) + g*m*zcm*sin(u4(u1)))/Ix,nv)
u7p=rsubstituir_t((-Ix*u3(u1)*u5(u1)*cos(u4(u1))**2 - Ix*u3(u1)*u5(u1) + Iz*u3(u1)*u5(u1)*cos(u4(u1))**2 + Iz*u5(u1)*u7(u1)**2*cos(u4(u1)) - g*m*xcm*cos(u2(u1))*cos(u4(u1)) + g*m*ycm*sin(u2(u1))*cos(u4(u1)))*u7(u1)*sin(u4(u1))/(2*Iz*u7(u1)**2*cos(u4(u1))**2 - (Ix*sin(u4(u1))**2 + Iz*cos(u4(u1))**2)*(u3(u1)*cos(u4(u1)) + 3*u7(u1)**2)),nv)
U=[u3,u3p,u5,u5p,u7,u7p]
w=[0.0,0.0,0.0,0.0,0.0,0.0]
xa=0.0
xb=10.0
de=4
h=1e-2
print Runge_kutta_sm(U,w,xa,xb,de,h)
