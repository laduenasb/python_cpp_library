from sys import path
path.append("/media/luis/MYLINUXLIVE1/programasl")
from definiciones import *
def sumav(A,B): ## suma del vector A y B, A+B
        C=[]
        for i in range(0,len(A)):
                C.append(A[i]+B[i])
        return C
def restav(A,B): ## resta del vector A y B, A-B
        C=[]
        for i in range(0,len(A)):
                C.append(A[i]-B[i])
        return C
def multiplicarc(c,A): ## multiplicar la constante c al vector A, c*A
        C=[]
        for i in range(0,len(A)):
                C.append(c*A[i])
        return C
def proyeccion(u,v): ## Proyeccion del vector u sobre el vector v.
        v2=modulo_vector(v)**2.0
        f=multiplicarc(producto_punto(u,v)/v2,v)
        return f
def rotar(r,p,theta): ###rotar un angulo theta el vector r a lo largo de la recta p, en sentido antihorario si theta es positivo, con theta en radianes
        P=proyeccion(r,p)
        rmp=restav(r,P)
        rcp=producto_cruz(r,p)
        s1=sumav(P,multiplicarc(cos(theta),rmp))
        s2=multiplicarc(-sin(theta)/modulo_vector(p),rcp)
        return sumav(s1,s2)
r=[1,0,0]
z=[3,0,3]
#print rotar(r,z,pi/4.0)
#print error_multiplicacion(25.9,0.1,19.5,0.1)
