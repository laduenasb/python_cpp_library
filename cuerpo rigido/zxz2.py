from __future__ import division
from sys import path
path.append("/media/luis/MYLINUXLIVE1/programasl")
from definiciones import *
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
xk,yk,zk,t,xcm,ycm,zcm,m,g,Ixx,Iyy,Izz,Ixy,Ixz,Iyz=symbols("xk,yk,zk,t,xcm,ycm,zcm,m,g,Ixx,Iyy,Izz,Ixy,Ixz,Iyz")
theta,phi,psi=symbols("theta,phi,psi")
nv=7
r=[xk,yk,zk]
ex=[1,0,0]
ez=[0,0,1]
l0=[cos(u6),sin(u6),0]
p0=producto_cruz(ez,l0)
rp1=rotar(r,ez,u2)
rp=rotar(rp1,p0,u4)
rpt=[]
for i in range(0,len(rp)):
        rpt.append(substituir_t(rp[i],nv))
rptp=trigsimp(collect(collect(collect(collect(collect(collect(expand(modulo_vector(derivarv(rpt,u1))**2),xk*yk).subs(xk*yk,Ixy),xk*zk).subs(xk*zk,Ixz),yk*zk).subs(yk*zk,Iyz),xk**2).subs(xk**2,Ixx),yk**2).subs(yk**2,Iyy),zk**2).subs(zk**2,Izz))
T1=substituiru([rptp],nv)
T1=R(1,2)*T1[0]
T2=substituir_t(T1,nv)
T1u2=diff(T2,u2(u1))
T1u4=diff(T2,u4(u1))
T1u6=diff(T2,u6(u1))
T1u3p=diff(diff(T2,u3(u1)),u1)
T1u5p=diff(diff(T2,u5(u1)),u1)
T1u7p=diff(diff(T2,u7(u1)),u1)
Qu2=-m*g*xcm*sin(u2(u1)-u6(u1))*sin(u4(u1))-m*g*ycm*cos(u2(u1)-u6(u1))*sin(u4(u1))
Qu4=m*g*zcm*sin(u4(u1))+m*g*xcm*cos(u2*(u1)-u6(u1))*cos(u4(u1))-m*g*ycm*sin(u2(u1)-u6(u1))*cos(u4(u1))
Qu6=m*g*xcm*sin(u2*(u1)-u6(u1))*sin(u4(u1))+m*g*ycm*cos(u2*(u1)-u6(u1))*sin(u4(u1))
E1=substituirun([T1u3p-T1u2-Qu2],nv)
E2=substituirun([T1u5p-T1u4-Qu4],nv)
E3=substituirun([T1u7p-T1u6-Qu6],nv)
E1=collect(collect(collect(expand(E1[0]),diff(u3(u1),u1)),diff(u5(u1))),diff(u7(u1),u1))
E2=collect(collect(collect(expand(E2[0]),diff(u3(u1),u1)),diff(u5(u1))),diff(u7(u1),u1))
E3=collect(collect(collect(expand(E3[0]),diff(u3(u1),u1)),diff(u5(u1))),diff(u7(u1),u1))
E1=[E1.coeff(diff(u3(u1),u1)),E1.coeff(diff(u5(u1),u1)),E1.coeff(diff(u7(u1),u1)),-(E1-E1.coeff(diff(u3(u1),u1))*diff(u3(u1),u1)-E1.coeff(diff(u5(u1),u1))*diff(u5(u1),u1)-E1.coeff(diff(u7(u1),u1))*diff(u7(u1),u1))]
E2=[E2.coeff(diff(u3(u1),u1)),E2.coeff(diff(u5(u1),u1)),E2.coeff(diff(u7(u1),u1)),-(E2-E2.coeff(diff(u3(u1),u1))*diff(u3(u1),u1)-E2.coeff(diff(u5(u1),u1))*diff(u5(u1),u1)-E2.coeff(diff(u7(u1),u1))*diff(u7(u1),u1))]
E3=[E3.coeff(diff(u3(u1),u1)),E3.coeff(diff(u5(u1),u1)),E3.coeff(diff(u7(u1),u1)),-(E3-E3.coeff(diff(u3(u1),u1))*diff(u3(u1),u1)-E3.coeff(diff(u5(u1),u1))*diff(u5(u1),u1)-E3.coeff(diff(u7(u1),u1))*diff(u7(u1),u1))]
####
E1=[rsubstituir_t(E1[0],nv),rsubstituir_t(E1[1],nv),rsubstituir_t(E1[2],nv),rsubstituir_t(E1[3],nv)]
E2=[rsubstituir_t(E2[0],nv),rsubstituir_t(E2[1],nv),rsubstituir_t(E2[2],nv),rsubstituir_t(E2[3],nv)]
E3=[rsubstituir_t(E3[0],nv),rsubstituir_t(E3[1],nv),rsubstituir_t(E3[2],nv),rsubstituir_t(E3[3],nv)]
M=[E1,E2,E3]
S=cramer(M)
u3p=0.0
u5p=0.0
u7p=0.0
U=[u3,S[0],u5,S[1],u7,S[2]]
w=[0.0,0.0,0.0,0.0,0.0,0.0]
xa=0.0
xb=10.0
de=4
h=1e-3
print Runge_kutta_sm(U,w,xa,xb,de,h)
