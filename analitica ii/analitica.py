##### curvas de fase
from sys import path
path.append("/media/luis/MYLINUXLIVE1/programasl")
from definiciones import *
def funcion1(q,H,k,m): ## k<0, donde H es positivo y se obtienen hiperbolas verticales para p(q)
        f=sqrt(2.0*m*(H-k*(q**2)/2.0))
        return f
def funcion2(p,H,k,m): ## k<0, donde H es negativo y se obtienen hiperbolas horizontales para q(p)
        f=sqrt((2.0/k)*(H-(p**2/(2.0*m))))
        return f
def velocidadx(p,m):
        return float(p)/float(m)
def velocidady(k,q):
        return -float(k)*float(q)
k=-2.0
m=1.0
H1=3.0
qa=-10.0
qb=10.0
pa=-10.0
pb=10.0
npuntos=100.0
q=crear_vector(qa,qb,npuntos)
p=crear_vector(pa,pb,npuntos)
pp=[]
pn=[]
qp=[]
qn=[]
## velocidad de fase para hiperbolas verticales
vxv=[]
vyv=[]
## velocidad de fase para hiperbolas horizontales
vxh=[]
vyh=[]
qnew=[]
pnew=[]
for i in range(0,len(q)):
        pp.append(funcion1(q[i],H1,k,m))
	qnew.append(q[i])
	vxv.append(velocidadx(funcion1(q[i],H1,k,m),m))
	vyv.append(velocidady(k,q[i]))	
for i in range(0,len(q)):
        pp.append(-funcion1(q[i],H1,k,m))
        qnew.append(q[i])
	vxv.append(velocidadx(-funcion1(q[i],H1,k,m),m))
	vyv.append(velocidady(k,q[i]))
for i in range(0,len(q)):
        qp.append(funcion2(p[i],-H1,k,m))
	pnew.append(p[i])
	vxh.append(velocidadx(p[i],m))
	vyh.append(velocidady(k,funcion2(p[i],-H1,k,m)))
for i in range(0,len(q)):
        qp.append(-funcion2(p[i],-H1,k,m))
	pnew.append(p[i])
	vxh.append(velocidadx(p[i],m))
	vyh.append(velocidady(k,-funcion2(p[i],-H1,k,m)))
for i in range(0,len(pnew)):
	qnew.append(qp[i])
	pp.append(pnew[i])
for i in range(0,len(vxh)):
	vxv.append(vxh[i])
	vyv.append(vyh[i])
print vertical4(qnew,pp,vxv,vyv)
