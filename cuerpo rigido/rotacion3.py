import time
start=time.time()
from sys import path
path.append("/media/luis/MYLINUXLIVE1/programasl")
from definiciones import *
xk,yk,zk,t,xcm,ycm,zcm,m,g=symbols("xk,yk,zk,t,xcm,ycm,zcm,m,g")
theta,phi,psi=symbols("theta,phi,psi")
r=[xk,yk,zk]
ez=[0,0,1]
l0=[cos(psi),sin(psi),0]
p0=producto_cruz(ez,l0)
rp=rotar(r,p0,theta)
lf=[sin(theta)*cos(psi),sin(theta)*sin(psi),cos(theta)]
#rpf=simplificarv(rotar(rp,lf,phi))
rpf=[xk*sin(psi)*sin(phi - psi)*cos(theta) - xk*sin(psi)*sin(phi - psi) + xk*cos(phi)*cos(theta) - yk*sin(phi)*cos(theta) + yk*sin(psi)*cos(theta)*cos(phi - psi) - yk*sin(psi)*cos(phi - psi) + zk*sin(theta)*cos(psi), xk*sin(phi) + xk*sin(psi)*cos(theta)*cos(phi - psi) - xk*sin(psi)*cos(phi - psi) - yk*sin(psi)*sin(phi - psi)*cos(theta) + yk*sin(psi)*sin(phi - psi) + yk*cos(phi) + zk*sin(psi)*sin(theta), -xk*sin(theta)*cos(phi - psi) + yk*sin(theta)*sin(phi - psi) + zk*cos(theta)]
rpf2=[]
for i in range(0,len(rpf)):
	rpf2.append(rpf[i].subs(theta,theta(t)))
	rpf2[i]=rpf2[i].subs(phi,phi(t))
	rpf2[i]=rpf2[i].subs(psi,psi(t))
#######
T=0.5*m*(-2*xk**2*sin(phi(t))**2*sin(psi(t))**2*sin(theta(t))**2*Derivative(psi(t), t)**2 + 2*xk**2*sin(phi(t))**2*sin(psi(t))**2*Derivative(theta(t), t)**2 + 4*xk**2*sin(phi(t))**2*sin(psi(t))*sin(theta(t))*cos(psi(t))*Derivative(psi(t), t)*Derivative(theta(t), t) + xk**2*sin(phi(t))**2*sin(theta(t))**2*Derivative(psi(t), t)**2 - xk**2*sin(phi(t))**2*Derivative(theta(t), t)**2 - 4*xk**2*sin(phi(t))*sin(psi(t))**2*sin(theta(t))*cos(phi(t))*Derivative(psi(t), t)*Derivative(theta(t), t) - 2*xk**2*sin(phi(t))*sin(psi(t))*sin(theta(t))**2*cos(phi(t))*cos(psi(t))*Derivative(psi(t), t)**2 + 2*xk**2*sin(phi(t))*sin(psi(t))*cos(phi(t))*cos(psi(t))*Derivative(theta(t), t)**2 + 2*xk**2*sin(phi(t))*sin(theta(t))*cos(phi(t))*Derivative(psi(t), t)*Derivative(theta(t), t) + xk**2*sin(psi(t))**2*sin(theta(t))**2*Derivative(psi(t), t)**2 - xk**2*sin(psi(t))**2*Derivative(theta(t), t)**2 - 2*xk**2*sin(psi(t))*sin(theta(t))*cos(psi(t))*Derivative(psi(t), t)*Derivative(theta(t), t) - xk**2*sin(theta(t))**2*Derivative(psi(t), t)**2 + 2*xk**2*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t) - 2*xk**2*cos(theta(t))*Derivative(psi(t), t)**2 + xk**2*Derivative(phi(t), t)**2 - 2*xk**2*Derivative(phi(t), t)*Derivative(psi(t), t) + 2*xk**2*Derivative(psi(t), t)**2 + xk**2*Derivative(theta(t), t)**2 + 2*xk*yk*sin(phi(t) - psi(t))*sin(theta(t))**2*cos(phi(t) - psi(t))*Derivative(psi(t), t)**2 - 2*xk*yk*sin(phi(t) - psi(t))*cos(phi(t) - psi(t))*Derivative(theta(t), t)**2 + 8*xk*yk*sin(phi(t))**2*sin(psi(t))**2*sin(theta(t))*Derivative(psi(t), t)*Derivative(theta(t), t) - 4*xk*yk*sin(phi(t))**2*sin(theta(t))*Derivative(psi(t), t)*Derivative(theta(t), t) + 8*xk*yk*sin(phi(t))*sin(psi(t))*sin(theta(t))*cos(phi(t))*cos(psi(t))*Derivative(psi(t), t)*Derivative(theta(t), t) - 4*xk*yk*sin(psi(t))**2*sin(theta(t))*Derivative(psi(t), t)*Derivative(theta(t), t) + 2*xk*yk*sin(theta(t))*Derivative(psi(t), t)*Derivative(theta(t), t) - 2*xk*zk*sin(phi(t) - psi(t))*cos(theta(t))*Derivative(psi(t), t)*Derivative(theta(t), t) + 2*xk*zk*sin(phi(t) - psi(t))*Derivative(psi(t), t)*Derivative(theta(t), t) + 3*xk*zk*sin(phi(t))*sin(psi(t))*sin(theta(t))*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t)/2 + 3*xk*zk*sin(phi(t))*sin(psi(t))*sin(theta(t))*cos(theta(t))*Derivative(theta(t), t)**2/2 + 2*xk*zk*sin(phi(t))*sin(psi(t))*sin(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t) - 2*xk*zk*sin(phi(t))*cos(psi(t))*Derivative(phi(t), t)*Derivative(theta(t), t) - 2*xk*zk*sin(psi(t))**2*sin(theta(t))*cos(phi(t) - psi(t))*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t) - 2*xk*zk*sin(psi(t))**2*sin(theta(t))*cos(phi(t) - psi(t))*cos(theta(t))*Derivative(theta(t), t)**2 + 2*xk*zk*sin(psi(t))*cos(phi(t))*Derivative(phi(t), t)*Derivative(theta(t), t) - xk*zk*sin(theta(t))*cos(phi(t) - 3*psi(t))*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t)/2 - xk*zk*sin(theta(t))*cos(phi(t) - 3*psi(t))*cos(theta(t))*Derivative(theta(t), t)**2/2 + 2*xk*zk*sin(theta(t))*cos(phi(t) - psi(t))*cos(theta(t))*Derivative(psi(t), t)**2 - 2*xk*zk*sin(theta(t))*cos(phi(t) - psi(t))*Derivative(psi(t), t)**2 + xk*zk*sin(theta(t))*cos(phi(t))*cos(psi(t))*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t)/2 + xk*zk*sin(theta(t))*cos(phi(t))*cos(psi(t))*cos(theta(t))*Derivative(theta(t), t)**2/2 + 2*xk*zk*sin(theta(t))*cos(phi(t))*cos(psi(t))*Derivative(phi(t), t)*Derivative(psi(t), t) + 2*yk**2*sin(phi(t))**2*sin(psi(t))**2*sin(theta(t))**2*Derivative(psi(t), t)**2 - 2*yk**2*sin(phi(t))**2*sin(psi(t))**2*Derivative(theta(t), t)**2 - 4*yk**2*sin(phi(t))**2*sin(psi(t))*sin(theta(t))*cos(psi(t))*Derivative(psi(t), t)*Derivative(theta(t), t) - yk**2*sin(phi(t))**2*sin(theta(t))**2*Derivative(psi(t), t)**2 + yk**2*sin(phi(t))**2*Derivative(theta(t), t)**2 + 4*yk**2*sin(phi(t))*sin(psi(t))**2*sin(theta(t))*cos(phi(t))*Derivative(psi(t), t)*Derivative(theta(t), t) + 2*yk**2*sin(phi(t))*sin(psi(t))*sin(theta(t))**2*cos(phi(t))*cos(psi(t))*Derivative(psi(t), t)**2 - 2*yk**2*sin(phi(t))*sin(psi(t))*cos(phi(t))*cos(psi(t))*Derivative(theta(t), t)**2 - 2*yk**2*sin(phi(t))*sin(theta(t))*cos(phi(t))*Derivative(psi(t), t)*Derivative(theta(t), t) - yk**2*sin(psi(t))**2*sin(theta(t))**2*Derivative(psi(t), t)**2 + yk**2*sin(psi(t))**2*Derivative(theta(t), t)**2 + 2*yk**2*sin(psi(t))*sin(theta(t))*cos(psi(t))*Derivative(psi(t), t)*Derivative(theta(t), t) + 2*yk**2*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t) - 2*yk**2*cos(theta(t))*Derivative(psi(t), t)**2 + yk**2*Derivative(phi(t), t)**2 - 2*yk**2*Derivative(phi(t), t)*Derivative(psi(t), t) + 2*yk**2*Derivative(psi(t), t)**2 + yk*zk*sin(phi(t) - 3*psi(t))*sin(theta(t))*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t)/2 + yk*zk*sin(phi(t) - 3*psi(t))*sin(theta(t))*cos(theta(t))*Derivative(theta(t), t)**2/2 + 2*yk*zk*sin(phi(t) - psi(t))*sin(psi(t))**2*sin(theta(t))*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t) + 2*yk*zk*sin(phi(t) - psi(t))*sin(psi(t))**2*sin(theta(t))*cos(theta(t))*Derivative(theta(t), t)**2 - 2*yk*zk*sin(phi(t) - psi(t))*sin(theta(t))*cos(theta(t))*Derivative(psi(t), t)**2 + 2*yk*zk*sin(phi(t) - psi(t))*sin(theta(t))*Derivative(psi(t), t)**2 - 2*yk*zk*sin(phi(t))*sin(psi(t))*Derivative(phi(t), t)*Derivative(theta(t), t) - yk*zk*sin(phi(t))*sin(theta(t))*cos(psi(t))*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t)/2 - yk*zk*sin(phi(t))*sin(theta(t))*cos(psi(t))*cos(theta(t))*Derivative(theta(t), t)**2/2 - 2*yk*zk*sin(phi(t))*sin(theta(t))*cos(psi(t))*Derivative(phi(t), t)*Derivative(psi(t), t) + 3*yk*zk*sin(psi(t))*sin(theta(t))*cos(phi(t))*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t)/2 + 3*yk*zk*sin(psi(t))*sin(theta(t))*cos(phi(t))*cos(theta(t))*Derivative(theta(t), t)**2/2 + 2*yk*zk*sin(psi(t))*sin(theta(t))*cos(phi(t))*Derivative(phi(t), t)*Derivative(psi(t), t) - 2*yk*zk*cos(phi(t) - psi(t))*cos(theta(t))*Derivative(psi(t), t)*Derivative(theta(t), t) + 2*yk*zk*cos(phi(t) - psi(t))*Derivative(psi(t), t)*Derivative(theta(t), t) - 2*yk*zk*cos(phi(t))*cos(psi(t))*Derivative(phi(t), t)*Derivative(theta(t), t) + zk**2*sin(theta(t))**2*Derivative(psi(t), t)**2 + zk**2*Derivative(theta(t), t)**2)

T1=0.5*m*(-2*xk**2*sin(phi(t))**2*sin(psi(t))**2*sin(theta(t))**2*Derivative(psi(t), t)**2 + 2*xk**2*sin(phi(t))**2*sin(psi(t))**2*Derivative(theta(t), t)**2 + 4*xk**2*sin(phi(t))**2*sin(psi(t))*sin(theta(t))*cos(psi(t))*Derivative(psi(t), t)*Derivative(theta(t), t) + xk**2*sin(phi(t))**2*sin(theta(t))**2*Derivative(psi(t), t)**2 - xk**2*sin(phi(t))**2*Derivative(theta(t), t)**2 - 4*xk**2*sin(phi(t))*sin(psi(t))**2*sin(theta(t))*cos(phi(t))*Derivative(psi(t), t)*Derivative(theta(t), t) - 2*xk**2*sin(phi(t))*sin(psi(t))*sin(theta(t))**2*cos(phi(t))*cos(psi(t))*Derivative(psi(t), t)**2 + 2*xk**2*sin(phi(t))*sin(psi(t))*cos(phi(t))*cos(psi(t))*Derivative(theta(t), t)**2 + 2*xk**2*sin(phi(t))*sin(theta(t))*cos(phi(t))*Derivative(psi(t), t)*Derivative(theta(t), t) + xk**2*sin(psi(t))**2*sin(theta(t))**2*Derivative(psi(t), t)**2 - xk**2*sin(psi(t))**2*Derivative(theta(t), t)**2 - 2*xk**2*sin(psi(t))*sin(theta(t))*cos(psi(t))*Derivative(psi(t), t)*Derivative(theta(t), t) - xk**2*sin(theta(t))**2*Derivative(psi(t), t)**2 + 2*xk**2*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t) - 2*xk**2*cos(theta(t))*Derivative(psi(t), t)**2 + xk**2*Derivative(phi(t), t)**2 - 2*xk**2*Derivative(phi(t), t)*Derivative(psi(t), t) + 2*xk**2*Derivative(psi(t), t)**2 + xk**2*Derivative(theta(t), t)**2) ####### xk**2

T2=0.5*m*(2*xk*yk*sin(phi(t) - psi(t))*sin(theta(t))**2*cos(phi(t) - psi(t))*Derivative(psi(t), t)**2 - 2*xk*yk*sin(phi(t) - psi(t))*cos(phi(t) - psi(t))*Derivative(theta(t), t)**2 + 8*xk*yk*sin(phi(t))**2*sin(psi(t))**2*sin(theta(t))*Derivative(psi(t), t)*Derivative(theta(t), t) - 4*xk*yk*sin(phi(t))**2*sin(theta(t))*Derivative(psi(t), t)*Derivative(theta(t), t) + 8*xk*yk*sin(phi(t))*sin(psi(t))*sin(theta(t))*cos(phi(t))*cos(psi(t))*Derivative(psi(t), t)*Derivative(theta(t), t) - 4*xk*yk*sin(psi(t))**2*sin(theta(t))*Derivative(psi(t), t)*Derivative(theta(t), t) + 2*xk*yk*sin(theta(t))*Derivative(psi(t), t)*Derivative(theta(t), t)) ####xk*yk

T3=0.5*m*(- 2*xk*zk*sin(phi(t) - psi(t))*cos(theta(t))*Derivative(psi(t), t)*Derivative(theta(t), t) + 2*xk*zk*sin(phi(t) - psi(t))*Derivative(psi(t), t)*Derivative(theta(t), t) + 3*xk*zk*sin(phi(t))*sin(psi(t))*sin(theta(t))*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t)/2 + 3*xk*zk*sin(phi(t))*sin(psi(t))*sin(theta(t))*cos(theta(t))*Derivative(theta(t), t)**2/2 + 2*xk*zk*sin(phi(t))*sin(psi(t))*sin(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t) - 2*xk*zk*sin(phi(t))*cos(psi(t))*Derivative(phi(t), t)*Derivative(theta(t), t) - 2*xk*zk*sin(psi(t))**2*sin(theta(t))*cos(phi(t) - psi(t))*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t) - 2*xk*zk*sin(psi(t))**2*sin(theta(t))*cos(phi(t) - psi(t))*cos(theta(t))*Derivative(theta(t), t)**2 + 2*xk*zk*sin(psi(t))*cos(phi(t))*Derivative(phi(t), t)*Derivative(theta(t), t) - xk*zk*sin(theta(t))*cos(phi(t) - 3*psi(t))*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t)/2 - xk*zk*sin(theta(t))*cos(phi(t) - 3*psi(t))*cos(theta(t))*Derivative(theta(t), t)**2/2 + 2*xk*zk*sin(theta(t))*cos(phi(t) - psi(t))*cos(theta(t))*Derivative(psi(t), t)**2 - 2*xk*zk*sin(theta(t))*cos(phi(t) - psi(t))*Derivative(psi(t), t)**2 + xk*zk*sin(theta(t))*cos(phi(t))*cos(psi(t))*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t)/2 + xk*zk*sin(theta(t))*cos(phi(t))*cos(psi(t))*cos(theta(t))*Derivative(theta(t), t)**2/2 + 2*xk*zk*sin(theta(t))*cos(phi(t))*cos(psi(t))*Derivative(phi(t), t)*Derivative(psi(t), t)) #### xk*zk

T4=0.5*m*(2*yk**2*sin(phi(t))**2*sin(psi(t))**2*sin(theta(t))**2*Derivative(psi(t), t)**2 - 2*yk**2*sin(phi(t))**2*sin(psi(t))**2*Derivative(theta(t), t)**2 - 4*yk**2*sin(phi(t))**2*sin(psi(t))*sin(theta(t))*cos(psi(t))*Derivative(psi(t), t)*Derivative(theta(t), t) - yk**2*sin(phi(t))**2*sin(theta(t))**2*Derivative(psi(t), t)**2 + yk**2*sin(phi(t))**2*Derivative(theta(t), t)**2 + 4*yk**2*sin(phi(t))*sin(psi(t))**2*sin(theta(t))*cos(phi(t))*Derivative(psi(t), t)*Derivative(theta(t), t) + 2*yk**2*sin(phi(t))*sin(psi(t))*sin(theta(t))**2*cos(phi(t))*cos(psi(t))*Derivative(psi(t), t)**2 - 2*yk**2*sin(phi(t))*sin(psi(t))*cos(phi(t))*cos(psi(t))*Derivative(theta(t), t)**2 - 2*yk**2*sin(phi(t))*sin(theta(t))*cos(phi(t))*Derivative(psi(t), t)*Derivative(theta(t), t) - yk**2*sin(psi(t))**2*sin(theta(t))**2*Derivative(psi(t), t)**2 + yk**2*sin(psi(t))**2*Derivative(theta(t), t)**2 + 2*yk**2*sin(psi(t))*sin(theta(t))*cos(psi(t))*Derivative(psi(t), t)*Derivative(theta(t), t) + 2*yk**2*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t) - 2*yk**2*cos(theta(t))*Derivative(psi(t), t)**2 + yk**2*Derivative(phi(t), t)**2 - 2*yk**2*Derivative(phi(t), t)*Derivative(psi(t), t) + 2*yk**2*Derivative(psi(t), t)**2) ##### yk**2

T5=0.5*m*(yk*zk*sin(phi(t) - 3*psi(t))*sin(theta(t))*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t)/2 + yk*zk*sin(phi(t) - 3*psi(t))*sin(theta(t))*cos(theta(t))*Derivative(theta(t), t)**2/2 + 2*yk*zk*sin(phi(t) - psi(t))*sin(psi(t))**2*sin(theta(t))*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t) + 2*yk*zk*sin(phi(t) - psi(t))*sin(psi(t))**2*sin(theta(t))*cos(theta(t))*Derivative(theta(t), t)**2 - 2*yk*zk*sin(phi(t) - psi(t))*sin(theta(t))*cos(theta(t))*Derivative(psi(t), t)**2 + 2*yk*zk*sin(phi(t) - psi(t))*sin(theta(t))*Derivative(psi(t), t)**2 - 2*yk*zk*sin(phi(t))*sin(psi(t))*Derivative(phi(t), t)*Derivative(theta(t), t) - yk*zk*sin(phi(t))*sin(theta(t))*cos(psi(t))*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t)/2 - yk*zk*sin(phi(t))*sin(theta(t))*cos(psi(t))*cos(theta(t))*Derivative(theta(t), t)**2/2 - 2*yk*zk*sin(phi(t))*sin(theta(t))*cos(psi(t))*Derivative(phi(t), t)*Derivative(psi(t), t) + 3*yk*zk*sin(psi(t))*sin(theta(t))*cos(phi(t))*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t)/2 + 3*yk*zk*sin(psi(t))*sin(theta(t))*cos(phi(t))*cos(theta(t))*Derivative(theta(t), t)**2/2 + 2*yk*zk*sin(psi(t))*sin(theta(t))*cos(phi(t))*Derivative(phi(t), t)*Derivative(psi(t), t) - 2*yk*zk*cos(phi(t) - psi(t))*cos(theta(t))*Derivative(psi(t), t)*Derivative(theta(t), t) + 2*yk*zk*cos(phi(t) - psi(t))*Derivative(psi(t), t)*Derivative(theta(t), t) - 2*yk*zk*cos(phi(t))*cos(psi(t))*Derivative(phi(t), t)*Derivative(theta(t), t)) ##### yk*zk

T6=0.5*m*(zk**2*sin(theta(t))**2*Derivative(psi(t), t)**2 + zk**2*Derivative(theta(t), t)**2) ### zk**2.0 

T1p=0.5*m*(xk**2*(4*sin(phi(t) - psi(t))*sin(phi(t))*sin(psi(t))*sin(theta(t))*Derivative(psi(t), t)*Derivative(theta(t), t) + sin(phi(t))**2*sin(theta(t))**2*Derivative(psi(t), t)**2 - sin(phi(t))**2*Derivative(theta(t), t)**2 - 2*sin(phi(t))*sin(psi(t))*sin(theta(t))**2*cos(phi(t) - psi(t))*Derivative(psi(t), t)**2 + 2*sin(phi(t))*sin(psi(t))*cos(phi(t) - psi(t))*Derivative(theta(t), t)**2 + 2*sin(phi(t))*sin(theta(t))*cos(phi(t))*Derivative(psi(t), t)*Derivative(theta(t), t) + sin(psi(t))**2*sin(theta(t))**2*Derivative(psi(t), t)**2 - sin(psi(t))**2*Derivative(theta(t), t)**2 - 2*sin(psi(t))*sin(theta(t))*cos(psi(t))*Derivative(psi(t), t)*Derivative(theta(t), t) - sin(theta(t))**2*Derivative(psi(t), t)**2 + 2*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t) - 2*cos(theta(t))*Derivative(psi(t), t)**2 + Derivative(phi(t), t)**2 - 2*Derivative(phi(t), t)*Derivative(psi(t), t) + 2*Derivative(psi(t), t)**2 + Derivative(theta(t), t)**2))

T2p=0.5*m*(2*xk*yk*((sin(-2*phi(t) + 2*psi(t) + theta(t)) + sin(2*phi(t) - 2*psi(t) + theta(t)) + sin(2*phi(t) + 2*psi(t) - theta(t)) - sin(2*phi(t) + 2*psi(t) + theta(t)))*Derivative(psi(t), t)*Derivative(theta(t), t)/4 + sin(phi(t) - psi(t))*sin(theta(t))**2*cos(phi(t) - psi(t))*Derivative(psi(t), t)**2 - sin(2*phi(t) - 2*psi(t))*Derivative(theta(t), t)**2/2 + 4*sin(phi(t))**2*sin(psi(t))**2*sin(theta(t))*Derivative(psi(t), t)*Derivative(theta(t), t) - 2*sin(phi(t))**2*sin(theta(t))*Derivative(psi(t), t)*Derivative(theta(t), t) - 2*sin(psi(t))**2*sin(theta(t))*Derivative(psi(t), t)*Derivative(theta(t), t) + sin(theta(t))*Derivative(psi(t), t)*Derivative(theta(t), t)))

T3p=0.5*m*(xk*zk*(-4*sin(phi(t) - psi(t))*cos(theta(t))*Derivative(psi(t), t)*Derivative(theta(t), t) - 4*sin(phi(t) - psi(t))*Derivative(phi(t), t)*Derivative(theta(t), t) + 4*sin(phi(t) - psi(t))*Derivative(psi(t), t)*Derivative(theta(t), t) + 3*sin(phi(t))*sin(psi(t))*sin(theta(t))*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t) + 3*sin(phi(t))*sin(psi(t))*sin(theta(t))*cos(theta(t))*Derivative(theta(t), t)**2 - 4*sin(psi(t))**2*sin(theta(t))*cos(phi(t) - psi(t))*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t) - 4*sin(psi(t))**2*sin(theta(t))*cos(phi(t) - psi(t))*cos(theta(t))*Derivative(theta(t), t)**2 - sin(theta(t))*cos(phi(t) - 3*psi(t))*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t) - sin(theta(t))*cos(phi(t) - 3*psi(t))*cos(theta(t))*Derivative(theta(t), t)**2 + 4*sin(theta(t))*cos(phi(t) - psi(t))*cos(theta(t))*Derivative(psi(t), t)**2 + 4*sin(theta(t))*cos(phi(t) - psi(t))*Derivative(phi(t), t)*Derivative(psi(t), t) - 4*sin(theta(t))*cos(phi(t) - psi(t))*Derivative(psi(t), t)**2 + sin(theta(t))*cos(phi(t))*cos(psi(t))*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t) + sin(theta(t))*cos(phi(t))*cos(psi(t))*cos(theta(t))*Derivative(theta(t), t)**2)/2)

T4p=0.5*m*(yk**2*(-4*sin(phi(t) - psi(t))*sin(phi(t))*sin(psi(t))*sin(theta(t))*Derivative(psi(t), t)*Derivative(theta(t), t) - sin(phi(t))**2*sin(theta(t))**2*Derivative(psi(t), t)**2 + sin(phi(t))**2*Derivative(theta(t), t)**2 + 2*sin(phi(t))*sin(psi(t))*sin(theta(t))**2*cos(phi(t) - psi(t))*Derivative(psi(t), t)**2 - 2*sin(phi(t))*sin(psi(t))*cos(phi(t) - psi(t))*Derivative(theta(t), t)**2 - 2*sin(phi(t))*sin(theta(t))*cos(phi(t))*Derivative(psi(t), t)*Derivative(theta(t), t) - sin(psi(t))**2*sin(theta(t))**2*Derivative(psi(t), t)**2 + sin(psi(t))**2*Derivative(theta(t), t)**2 + 2*sin(psi(t))*sin(theta(t))*cos(psi(t))*Derivative(psi(t), t)*Derivative(theta(t), t) + 2*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t) - 2*cos(theta(t))*Derivative(psi(t), t)**2 + Derivative(phi(t), t)**2 - 2*Derivative(phi(t), t)*Derivative(psi(t), t) + 2*Derivative(psi(t), t)**2))

T5p=0.5*m*(yk*zk*(sin(phi(t) - 3*psi(t))*sin(theta(t))*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t) + sin(phi(t) - 3*psi(t))*sin(theta(t))*cos(theta(t))*Derivative(theta(t), t)**2 + 4*sin(phi(t) - psi(t))*sin(psi(t))**2*sin(theta(t))*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t) + 4*sin(phi(t) - psi(t))*sin(psi(t))**2*sin(theta(t))*cos(theta(t))*Derivative(theta(t), t)**2 - 4*sin(phi(t) - psi(t))*sin(theta(t))*cos(theta(t))*Derivative(psi(t), t)**2 - 4*sin(phi(t) - psi(t))*sin(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t) + 4*sin(phi(t) - psi(t))*sin(theta(t))*Derivative(psi(t), t)**2 - sin(phi(t))*sin(theta(t))*cos(psi(t))*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t) - sin(phi(t))*sin(theta(t))*cos(psi(t))*cos(theta(t))*Derivative(theta(t), t)**2 + 3*sin(psi(t))*sin(theta(t))*cos(phi(t))*cos(theta(t))*Derivative(phi(t), t)*Derivative(psi(t), t) + 3*sin(psi(t))*sin(theta(t))*cos(phi(t))*cos(theta(t))*Derivative(theta(t), t)**2 - 4*cos(phi(t) - psi(t))*cos(theta(t))*Derivative(psi(t), t)*Derivative(theta(t), t) - 4*cos(phi(t) - psi(t))*Derivative(phi(t), t)*Derivative(theta(t), t) + 4*cos(phi(t) - psi(t))*Derivative(psi(t), t)*Derivative(theta(t), t))/2)

T6p=0.5*m*(zk**2*(sin(theta(t))**2*Derivative(psi(t), t)**2 + Derivative(theta(t), t)**2))

T=T1p+T2p+T3p+T4p+T5p+T6p
#### energia cinetica en terminos de u1,u2,u3,u4,u5,u6,u7
u1,u2,u3,u4,u5,u6,u7=symbols("u1 u2 u3 u4 u5 u6 u7")
nv=7 ### numero de variables de T
T=T.subs(diff(phi(t),t),u7)
T=T.subs(diff(theta(t),t),u3)
T=T.subs(diff(psi(t),t),u5)
T=T.subs(theta(t),u2)
T=T.subs(phi(t),u6)
T=T.subs(psi(t),u4)
Tu2=substituir_t(diff(T,u2),nv)
Tu4=substituir_t(diff(T,u4),nv)
Tu6=substituir_t(diff(T,u6),nv)
Tu3=substituir_t(diff(T,u3),nv)
Tu5=substituir_t(diff(T,u5),nv)
Tu7=substituir_t(diff(T,u7),nv)
Tu3p=diff(substituir_t(Tu3,nv),u1)
Tu5p=diff(substituir_t(Tu5,nv),u1)
Tu7p=diff(substituir_t(Tu7,nv),u1)
### fuerzas generalizadas
def substituiru(S1,nv):
	S=[]
	for i in range(0,len(S1)):
		S.append(S1[i].subs(diff(u2(u1),u1),u3(u1)))
		S[i]=S[i].subs(diff(u4(u1),u1),u4(u1))
		S[i]=S[i].subs(diff(u6(u1),u1),u7(u1))
		S[i]=rsubstituir_t(S[i],nv)
	return S	
Qth=m*g*xcm*cos(u2(u1))*cos(u6(u1)-u4(u1))-m*g*ycm*cos(u2(u1))*sin(u6(u1)-u4(u1))+m*g*zcm*sin(u2(u1))
Qps=m*g*xcm*sin(u2(u1))*sin(u6(u1)-u4(u1))+m*g*ycm*sin(u2(u1))*cos(u6(u1)-u4(u1))
Qph=-m*g*xcm*sin(u2(u1))*sin(u6(u1)-u4(u1))-m*g*ycm*sin(u2(u1))*cos(u6(u1)-u4(u1))
## q1=theta
E1=collect(collect(collect(expand(Tu3p-Tu2-Qth),diff(u3(u1),u1)),diff(u5(u1),u1)),diff(u7(u1),u1))
## q2=psi
E2=collect(collect(collect(expand(Tu5p-Tu4-Qps),diff(u3(u1),u1)),diff(u5(u1),u1)),diff(u7(u1),u1))
## q3=phi
E3=collect(collect(collect(expand(Tu7p-Tu6-Qph),diff(u3(u1),u1)),diff(u5(u1),u1)),diff(u7(u1),u1))
E1p=[E1.coeff(diff(u3(u1),u1)),E1.coeff(diff(u5(u1),u1)),E1.coeff(diff(u7(u1),u1))]
E2p=[E2.coeff(diff(u3(u1),u1)),E2.coeff(diff(u5(u1),u1)),E2.coeff(diff(u7(u1),u1))]
E3p=[E3.coeff(diff(u3(u1),u1)),E3.coeff(diff(u5(u1),u1)),E3.coeff(diff(u7(u1),u1))]
E1p=[E1p[0],E1p[1],E1p[2],-(E1-E1p[0]*diff(u3(u1),u1)-E1p[1]*diff(u5(u1),u1)-E1p[2]*diff(u7(u1),u1))]
E2p=[E2p[0],E2p[1],E2p[2],-(E2-E2p[0]*diff(u3(u1),u1)-E2p[1]*diff(u5(u1),u1)-E2p[2]*diff(u7(u1),u1))]
E3p=[E3p[0],E3p[1],E3p[2],-(E3-E3p[0]*diff(u3(u1),u1)-E3p[1]*diff(u5(u1),u1)-E3p[2]*diff(u7(u1),u1))]
M=[E1p,E2p,E3p]
det=determinante(M)
pprint(det.evalf(subs={u2(u1):2,u3(u1):1,u4(u1):3,u5(u1):2,u6(u1):1.2,u7(u1):0.2,diff(u2(u1),u1):1,diff(u4(u1),u1):3,diff(u6(u1),u1):0.2,m:1.0,g:9.8,xk:1,yk:0,zk:1}))
E3p=substituiru(E3p,nv)
i3p=substituiru(E3p,nv)
E3p=substituiru(E3p,nv)
#start=time.time()
#S1=cramer(M)
#S=[]
#S=substituiru(S,nv)
#end=time.time()
#U=[u3,S[0],u5,S[1],u7,S[2]]
#w=[0.0,0.0,0.0,0.0,0.0,0.0]
#xa=0.0
#xb=10.0
#de=4
#h=1e-1
#print Runge_kutta_sm(U,w,xa,xb,de,h)
