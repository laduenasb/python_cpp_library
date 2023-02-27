from definiciones import *
from sympy import *
init_printing()
u1,u2,u3,u4=symbols("u1,u2,u3,u4")
x0,y0,z0=symbols("x0 y0 z0")
a1,a2,a3,a4,a5,a6,a7,a8,a9=symbols("a1,a2,a3,a4,a5,a6,a7,a8,a9")
t,theta,phi,psi=symbols("t theta phi psi")
B=[[cos(psi(t)),sin(psi(t)),0],[-sin(psi(t)),cos(psi(t)),0],[0,0,1]]
C=[[1,0,0],[0,cos(theta(t)),sin(theta(t))],[0,-sin(theta(t)),cos(theta(t))]]
D=[[cos(phi(t)),sin(phi(t)),0],[-sin(phi(t)),cos(phi(t)),0],[0,0,1]]
A0=producto(producto(B,C),D)
A=transpuesta(A0) ### lambda
#T=simplificarm(producto(derivarm(A,t),A0))
#T2=simplificarm(producto(derivarm(A0,t),A))
r=[[x0],[y0],[z0]]
rp=producto(A,r)
#print vertical(T2)
#F1=expand(producto_punto(rp[0],rp[0]))
#F2=expand(producto_punto(rp[1],rp[1]))
#pprint(simplify(F1+F2))
#pprint(rotar(r,[0,0,1],theta))
I1=[x0**2,x0*y0,x0*z0]
I2=[y0*x0,y0**2,y0*z0]
I3=[z0*x0,z0*y0,z0**2]
I=[I1,I2,I3]
v1=[a1,a2,a3]
v2=[a4,a5,a6]
v3=[a7,a8,a9]
V=[v1,v2,v3]
rp2=producto(V,r)
Ip1=producto(V,producto(I,transpuesta(V)))
n1=[rp2[0][0]**2,rp2[0][0]*rp2[1][0],rp2[0][0]*rp2[2][0]]
n2=[rp2[1][0]*rp2[0][0],rp2[1][0]**2,rp2[1][0]*rp2[2][0]]
n3=[rp2[2][0]*rp2[0][0],rp2[2][0]*rp2[1][0],rp2[2][0]**2]
Ip2=[n1,n2,n3]
for i in range(0,len(I)):
	for j in range(0,len(I[0])):
		if expand(Ip1[i][j])==expand(Ip2[i][j]):
			print "True"
		else:
			print "False"
