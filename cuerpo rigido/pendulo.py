from sys import path
path.append("/media/luis/MYLINUXLIVE1/programasl")
from definiciones import *
U=['u3', '-5*sin(u2)']
xa=0.0
xb=10.0
de=4
h=0.01
w=[0, 0.1]
def Runge_kutta_s2(U,w,xa,xb,de,h):
        xa=float(xa)
        xb=float(xb)
        m=len(U)
        npuntos=int(ceil((xb-xa)/h+1.0))
        vector_t=crear_vector(xa,xb,npuntos)
        h=vector_t[1]-vector_t[0]
        W1=crear_matriz(len(vector_t),len(U))
        w1=[]
        w2=[]
        w9=[]
        h_new=[]
        error=10**(-de-1)
        for i in range(0,len(w)):
                w1.append(float(w[i]))
                w2.append(float(w[i]))
                w9.append(float(w[i]))
                W1[0][i]=float(w[i])
        def funcion1(u1,u2,u3):
                f=u3
                return f
        def funcion2(u1,u2,u3):
                f=-5*sin(u2)
                return f

        for i in range(1,len(vector_t)):
		k11=h*funcion1(vector_t[i-1],w1[0],w1[1])
		k12=h*funcion2(vector_t[i-1],w1[0],w1[1])
		k21=h*funcion1(vector_t[i-1]+(h/4.0),w1[0]+(1.0/4.0)*k11,w1[1]+(1.0/4.0)*k12)
		k22=h*funcion2(vector_t[i-1]+(h/4.0),w1[0]+(1.0/4.0)*k11,w1[1]+(1.0/4.0)*k12)
		k31=h*funcion1(vector_t[i-1]+(3.0*h/8.0),w1[0]+(3.0/32.0)*k11+(9.0/32.0)*k21,w1[1]+(3.0/32.0)*k12+(9.0/32.0)*k22)
		k32=h*funcion2(vector_t[i-1]+(3.0*h/8.0),w1[0]+(3.0/32.0)*k11+(9.0/32.0)*k21,w1[1]+(3.0/32.0)*k12+(9.0/32.0)*k22)
		k41=h*funcion1(vector_t[i-1]+(12.0*h/13.0),w1[0]+(1932.0/2197.0)*k11-(7200.0/2197.0)*k21+(7296.0/2197.0)*k31,w1[1]+(1932.0/2197.0)*k12-(7200.0/2197.0)*k22+(7296.0/2197.0)*k32)
		k42=h*funcion2(vector_t[i-1]+(12.0*h/13.0),w1[0]+(1932.0/2197.0)*k11-(7200.0/2197.0)*k21+(7296.0/2197.0)*k31,w1[1]+(1932.0/2197.0)*k12-(7200.0/2197.0)*k22+(7296.0/2197.0)*k32)
		k51=h*funcion1(vector_t[i-1]+h,w1[0]+(439.0/216.0)*k11-8.0*k21+(3680.0/513.0)*k31-(845.0/4104.0)*k41,w1[1]+(439.0/216.0)*k12-8.0*k22+(3680.0/513.0)*k32-(845.0/4104.0)*k42)
		k52=h*funcion2(vector_t[i-1]+h,w1[0]+(439.0/216.0)*k11-8.0*k21+(3680.0/513.0)*k31-(845.0/4104.0)*k41,w1[1]+(439.0/216.0)*k12-8.0*k22+(3680.0/513.0)*k32-(845.0/4104.0)*k42)
		k61=h*funcion1(vector_t[i-1]+(h/2.0),w1[0]-(8.0/27.0)*k11+2.0*k21-(3544.0/2565.0)*k31+(1859.0/4104.0)*k41-(11.0/40.0)*k51,w1[1]-(8.0/27.0)*k12+2.0*k22-(3544.0/2565.0)*k32+(1859.0/4104.0)*k42-(11.0/40.0)*k52)
		k62=h*funcion2(vector_t[i-1]+(h/2.0),w1[0]-(8.0/27.0)*k11+2.0*k21-(3544.0/2565.0)*k31+(1859.0/4104.0)*k41-(11.0/40.0)*k51,w1[1]-(8.0/27.0)*k12+2.0*k22-(3544.0/2565.0)*k32+(1859.0/4104.0)*k42-(11.0/40.0)*k52)
		w1[0]=w1[0]+(25.0/216.0)*k11+(1408.0/2565.0)*k31+(2197.0/4104.0)*k41-(1.0/5.0)*k51
		W1[i][0]=w1[0]
		w1[1]=w1[1]+(25.0/216.0)*k12+(1408.0/2565.0)*k32+(2197.0/4104.0)*k42-(1.0/5.0)*k52
		W1[i][1]=w1[1]
		w2[0]=w2[0]+(16.0/135.0)*k11+(6656.0/12825.0)*k31+(28561.0/56430.0)*k41-(9.0/50.0)*k51+(2.0/55.0)*k61
                if abs(w1[0]-w2[0])!=0.0:
                        lo=(0.5*(h**5)*error/abs(w1[0]-w2[0]))**(1.0/4.0)
                        h_new.append(lo)
		w2[1]=w2[1]+(16.0/135.0)*k12+(6656.0/12825.0)*k32+(28561.0/56430.0)*k42-(9.0/50.0)*k52+(2.0/55.0)*k62
                if abs(w1[1]-w2[1])!=0.0:
                        lo=(0.5*(h**5)*error/abs(w1[1]-w2[1]))**(1.0/4.0)
                        h_new.append(lo)
        equalv(w9,w)
        hkl=""
        for i in range(0,len(U)+1):
                d=str(i+1)
                g="u"
                ghj=" "
                hkl+=g+d+ghj
        print hkl
        h=vector_t[1]-vector_t[0]
        if len(h_new)==0:
                h_new.append(h)
        return vector_t,W1,h,minimo(h_new)
F=Runge_kutta_s2(U,w,xa,xb,de,h)
vt=F[0]
H=F[1]
hn=F[2]
hmin=F[3]
print vertical2(vt,H)
print 'h=',hn
print 'hmin=',hmin

