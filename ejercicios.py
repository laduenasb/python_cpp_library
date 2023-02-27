#-*-coding:utf-8-*- 
from definiciones import *
def suma(x): ### suma de los valores de x
    s=0.0
    for i in range(0,len(x)):
            s+=x[i]
    return s
def xim(x): ### xi-promedio
    p=promedio(x)
    a=0.0
    for i in range(0,len(x)):
	    a+=x[i]-p
            print str(i+1),x[i]-p
    return "suma=",a
def ximc(x): ### (xi-promedio)**2
    p=promedio(x)
    a=0.0
    for i in range(0,len(x)):
            a+=(x[i]-p)**2
            print str(i+1),(x[i]-p)**2
    return "suma=",a
def desviacion_media(s,n,N): ### s desviacion estandar, n muestra, N poblacion
	sxp=sqrt((float(N-n)/float(N))*float(s)**2/float(n))
	return sxp
def sp(p,n,N): ### p proporcion, n muestra, N poblacion
	sxc=sqrt(float(N-n)*p*(1-p)/float(N*(n-1)))
	return sxc
def nxp(EE,N,s,z): ## EE error, N poblacion, s desviacion estandar 
	qq=float(N*s**2)/float((N-1)*float(EE/z)**2+s**2)
	return qq
def Np(EE,N,p,z): ## EE error, N poblacion, p proporcion
	qw=float(N*p*(1-p))/float((N-1)*(float(EE/z))**2+p*(1-p))
	return qw
