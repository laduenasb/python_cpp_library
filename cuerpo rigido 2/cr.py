from __future__ import division
from sys import path
path.append("/media/luis/MYLINUXLIVE1/programasl")
from definiciones import *
U=['u3', '0.000833333333333333*(-1500.0*u3*u5*cos(u4) + u5*(600.0*u3*cos(u4) + 1500.0*u7))/sin(u4)', 'u5', '-0.125*u3**2*sin(2.0*u4) - 1.25*u3*u7*sin(u4) + 0.49*sin(u4)', 'u7', '5.55555555555556e-7*(1500.0*u3*u5*(1200.0*sin(u4)**2 + 1500.0*cos(u4)**2) + u5*(-900000.0*u3*cos(u4) - 2250000.0*u7)*cos(u4))/sin(u4)']
xa=0.0
xb=10.0
de=4
h=0.1
w=[0.0, 0.0, pi/4.0, 0.0, 0.0, 0.2]
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
        def funcion1(u1,u2,u3,u4,u5,u6,u7):
                f=u3
                return f
        def funcion2(u1,u2,u3,u4,u5,u6,u7):
                f=0.000833333333333333*(-1500.0*u3*u5*cos(u4) + u5*(600.0*u3*cos(u4) + 1500.0*u7))/sin(u4)
                return f
        def funcion3(u1,u2,u3,u4,u5,u6,u7):
                f=u5
                return f
        def funcion4(u1,u2,u3,u4,u5,u6,u7):
                f=-0.125*u3**2*sin(2.0*u4) - 1.25*u3*u7*sin(u4) + 0.49*sin(u4)
                return f
        def funcion5(u1,u2,u3,u4,u5,u6,u7):
                f=u7
                return f
        def funcion6(u1,u2,u3,u4,u5,u6,u7):
                f=5.55555555555556e-7*(1500.0*u3*u5*(1200.0*sin(u4)**2 + 1500.0*cos(u4)**2) + u5*(-900000.0*u3*cos(u4) - 2250000.0*u7)*cos(u4))/sin(u4)
                return f

        for i in range(1,len(vector_t)):
		k11=h*funcion1(vector_t[i-1],w1[0],w1[1],w1[2],w1[3],w1[4],w1[5])
		k12=h*funcion2(vector_t[i-1],w1[0],w1[1],w1[2],w1[3],w1[4],w1[5])
		k13=h*funcion3(vector_t[i-1],w1[0],w1[1],w1[2],w1[3],w1[4],w1[5])
		k14=h*funcion4(vector_t[i-1],w1[0],w1[1],w1[2],w1[3],w1[4],w1[5])
		k15=h*funcion5(vector_t[i-1],w1[0],w1[1],w1[2],w1[3],w1[4],w1[5])
		k16=h*funcion6(vector_t[i-1],w1[0],w1[1],w1[2],w1[3],w1[4],w1[5])
		k21=h*funcion1(vector_t[i-1]+(h/4.0),w1[0]+(1.0/4.0)*k11,w1[1]+(1.0/4.0)*k12,w1[2]+(1.0/4.0)*k13,w1[3]+(1.0/4.0)*k14,w1[4]+(1.0/4.0)*k15,w1[5]+(1.0/4.0)*k16)
		k22=h*funcion2(vector_t[i-1]+(h/4.0),w1[0]+(1.0/4.0)*k11,w1[1]+(1.0/4.0)*k12,w1[2]+(1.0/4.0)*k13,w1[3]+(1.0/4.0)*k14,w1[4]+(1.0/4.0)*k15,w1[5]+(1.0/4.0)*k16)
		k23=h*funcion3(vector_t[i-1]+(h/4.0),w1[0]+(1.0/4.0)*k11,w1[1]+(1.0/4.0)*k12,w1[2]+(1.0/4.0)*k13,w1[3]+(1.0/4.0)*k14,w1[4]+(1.0/4.0)*k15,w1[5]+(1.0/4.0)*k16)
		k24=h*funcion4(vector_t[i-1]+(h/4.0),w1[0]+(1.0/4.0)*k11,w1[1]+(1.0/4.0)*k12,w1[2]+(1.0/4.0)*k13,w1[3]+(1.0/4.0)*k14,w1[4]+(1.0/4.0)*k15,w1[5]+(1.0/4.0)*k16)
		k25=h*funcion5(vector_t[i-1]+(h/4.0),w1[0]+(1.0/4.0)*k11,w1[1]+(1.0/4.0)*k12,w1[2]+(1.0/4.0)*k13,w1[3]+(1.0/4.0)*k14,w1[4]+(1.0/4.0)*k15,w1[5]+(1.0/4.0)*k16)
		k26=h*funcion6(vector_t[i-1]+(h/4.0),w1[0]+(1.0/4.0)*k11,w1[1]+(1.0/4.0)*k12,w1[2]+(1.0/4.0)*k13,w1[3]+(1.0/4.0)*k14,w1[4]+(1.0/4.0)*k15,w1[5]+(1.0/4.0)*k16)
		k31=h*funcion1(vector_t[i-1]+(3.0*h/8.0),w1[0]+(3.0/32.0)*k11+(9.0/32.0)*k21,w1[1]+(3.0/32.0)*k12+(9.0/32.0)*k22,w1[2]+(3.0/32.0)*k13+(9.0/32.0)*k23,w1[3]+(3.0/32.0)*k14+(9.0/32.0)*k24,w1[4]+(3.0/32.0)*k15+(9.0/32.0)*k25,w1[5]+(3.0/32.0)*k16+(9.0/32.0)*k26)
		k32=h*funcion2(vector_t[i-1]+(3.0*h/8.0),w1[0]+(3.0/32.0)*k11+(9.0/32.0)*k21,w1[1]+(3.0/32.0)*k12+(9.0/32.0)*k22,w1[2]+(3.0/32.0)*k13+(9.0/32.0)*k23,w1[3]+(3.0/32.0)*k14+(9.0/32.0)*k24,w1[4]+(3.0/32.0)*k15+(9.0/32.0)*k25,w1[5]+(3.0/32.0)*k16+(9.0/32.0)*k26)
		k33=h*funcion3(vector_t[i-1]+(3.0*h/8.0),w1[0]+(3.0/32.0)*k11+(9.0/32.0)*k21,w1[1]+(3.0/32.0)*k12+(9.0/32.0)*k22,w1[2]+(3.0/32.0)*k13+(9.0/32.0)*k23,w1[3]+(3.0/32.0)*k14+(9.0/32.0)*k24,w1[4]+(3.0/32.0)*k15+(9.0/32.0)*k25,w1[5]+(3.0/32.0)*k16+(9.0/32.0)*k26)
		k34=h*funcion4(vector_t[i-1]+(3.0*h/8.0),w1[0]+(3.0/32.0)*k11+(9.0/32.0)*k21,w1[1]+(3.0/32.0)*k12+(9.0/32.0)*k22,w1[2]+(3.0/32.0)*k13+(9.0/32.0)*k23,w1[3]+(3.0/32.0)*k14+(9.0/32.0)*k24,w1[4]+(3.0/32.0)*k15+(9.0/32.0)*k25,w1[5]+(3.0/32.0)*k16+(9.0/32.0)*k26)
		k35=h*funcion5(vector_t[i-1]+(3.0*h/8.0),w1[0]+(3.0/32.0)*k11+(9.0/32.0)*k21,w1[1]+(3.0/32.0)*k12+(9.0/32.0)*k22,w1[2]+(3.0/32.0)*k13+(9.0/32.0)*k23,w1[3]+(3.0/32.0)*k14+(9.0/32.0)*k24,w1[4]+(3.0/32.0)*k15+(9.0/32.0)*k25,w1[5]+(3.0/32.0)*k16+(9.0/32.0)*k26)
		k36=h*funcion6(vector_t[i-1]+(3.0*h/8.0),w1[0]+(3.0/32.0)*k11+(9.0/32.0)*k21,w1[1]+(3.0/32.0)*k12+(9.0/32.0)*k22,w1[2]+(3.0/32.0)*k13+(9.0/32.0)*k23,w1[3]+(3.0/32.0)*k14+(9.0/32.0)*k24,w1[4]+(3.0/32.0)*k15+(9.0/32.0)*k25,w1[5]+(3.0/32.0)*k16+(9.0/32.0)*k26)
		k41=h*funcion1(vector_t[i-1]+(12.0*h/13.0),w1[0]+(1932.0/2197.0)*k11-(7200.0/2197.0)*k21+(7296.0/2197.0)*k31,w1[1]+(1932.0/2197.0)*k12-(7200.0/2197.0)*k22+(7296.0/2197.0)*k32,w1[2]+(1932.0/2197.0)*k13-(7200.0/2197.0)*k23+(7296.0/2197.0)*k33,w1[3]+(1932.0/2197.0)*k14-(7200.0/2197.0)*k24+(7296.0/2197.0)*k34,w1[4]+(1932.0/2197.0)*k15-(7200.0/2197.0)*k25+(7296.0/2197.0)*k35,w1[5]+(1932.0/2197.0)*k16-(7200.0/2197.0)*k26+(7296.0/2197.0)*k36)
		k42=h*funcion2(vector_t[i-1]+(12.0*h/13.0),w1[0]+(1932.0/2197.0)*k11-(7200.0/2197.0)*k21+(7296.0/2197.0)*k31,w1[1]+(1932.0/2197.0)*k12-(7200.0/2197.0)*k22+(7296.0/2197.0)*k32,w1[2]+(1932.0/2197.0)*k13-(7200.0/2197.0)*k23+(7296.0/2197.0)*k33,w1[3]+(1932.0/2197.0)*k14-(7200.0/2197.0)*k24+(7296.0/2197.0)*k34,w1[4]+(1932.0/2197.0)*k15-(7200.0/2197.0)*k25+(7296.0/2197.0)*k35,w1[5]+(1932.0/2197.0)*k16-(7200.0/2197.0)*k26+(7296.0/2197.0)*k36)
		k43=h*funcion3(vector_t[i-1]+(12.0*h/13.0),w1[0]+(1932.0/2197.0)*k11-(7200.0/2197.0)*k21+(7296.0/2197.0)*k31,w1[1]+(1932.0/2197.0)*k12-(7200.0/2197.0)*k22+(7296.0/2197.0)*k32,w1[2]+(1932.0/2197.0)*k13-(7200.0/2197.0)*k23+(7296.0/2197.0)*k33,w1[3]+(1932.0/2197.0)*k14-(7200.0/2197.0)*k24+(7296.0/2197.0)*k34,w1[4]+(1932.0/2197.0)*k15-(7200.0/2197.0)*k25+(7296.0/2197.0)*k35,w1[5]+(1932.0/2197.0)*k16-(7200.0/2197.0)*k26+(7296.0/2197.0)*k36)
		k44=h*funcion4(vector_t[i-1]+(12.0*h/13.0),w1[0]+(1932.0/2197.0)*k11-(7200.0/2197.0)*k21+(7296.0/2197.0)*k31,w1[1]+(1932.0/2197.0)*k12-(7200.0/2197.0)*k22+(7296.0/2197.0)*k32,w1[2]+(1932.0/2197.0)*k13-(7200.0/2197.0)*k23+(7296.0/2197.0)*k33,w1[3]+(1932.0/2197.0)*k14-(7200.0/2197.0)*k24+(7296.0/2197.0)*k34,w1[4]+(1932.0/2197.0)*k15-(7200.0/2197.0)*k25+(7296.0/2197.0)*k35,w1[5]+(1932.0/2197.0)*k16-(7200.0/2197.0)*k26+(7296.0/2197.0)*k36)
		k45=h*funcion5(vector_t[i-1]+(12.0*h/13.0),w1[0]+(1932.0/2197.0)*k11-(7200.0/2197.0)*k21+(7296.0/2197.0)*k31,w1[1]+(1932.0/2197.0)*k12-(7200.0/2197.0)*k22+(7296.0/2197.0)*k32,w1[2]+(1932.0/2197.0)*k13-(7200.0/2197.0)*k23+(7296.0/2197.0)*k33,w1[3]+(1932.0/2197.0)*k14-(7200.0/2197.0)*k24+(7296.0/2197.0)*k34,w1[4]+(1932.0/2197.0)*k15-(7200.0/2197.0)*k25+(7296.0/2197.0)*k35,w1[5]+(1932.0/2197.0)*k16-(7200.0/2197.0)*k26+(7296.0/2197.0)*k36)
		k46=h*funcion6(vector_t[i-1]+(12.0*h/13.0),w1[0]+(1932.0/2197.0)*k11-(7200.0/2197.0)*k21+(7296.0/2197.0)*k31,w1[1]+(1932.0/2197.0)*k12-(7200.0/2197.0)*k22+(7296.0/2197.0)*k32,w1[2]+(1932.0/2197.0)*k13-(7200.0/2197.0)*k23+(7296.0/2197.0)*k33,w1[3]+(1932.0/2197.0)*k14-(7200.0/2197.0)*k24+(7296.0/2197.0)*k34,w1[4]+(1932.0/2197.0)*k15-(7200.0/2197.0)*k25+(7296.0/2197.0)*k35,w1[5]+(1932.0/2197.0)*k16-(7200.0/2197.0)*k26+(7296.0/2197.0)*k36)
		k51=h*funcion1(vector_t[i-1]+h,w1[0]+(439.0/216.0)*k11-8.0*k21+(3680.0/513.0)*k31-(845.0/4104.0)*k41,w1[1]+(439.0/216.0)*k12-8.0*k22+(3680.0/513.0)*k32-(845.0/4104.0)*k42,w1[2]+(439.0/216.0)*k13-8.0*k23+(3680.0/513.0)*k33-(845.0/4104.0)*k43,w1[3]+(439.0/216.0)*k14-8.0*k24+(3680.0/513.0)*k34-(845.0/4104.0)*k44,w1[4]+(439.0/216.0)*k15-8.0*k25+(3680.0/513.0)*k35-(845.0/4104.0)*k45,w1[5]+(439.0/216.0)*k16-8.0*k26+(3680.0/513.0)*k36-(845.0/4104.0)*k46)
		k52=h*funcion2(vector_t[i-1]+h,w1[0]+(439.0/216.0)*k11-8.0*k21+(3680.0/513.0)*k31-(845.0/4104.0)*k41,w1[1]+(439.0/216.0)*k12-8.0*k22+(3680.0/513.0)*k32-(845.0/4104.0)*k42,w1[2]+(439.0/216.0)*k13-8.0*k23+(3680.0/513.0)*k33-(845.0/4104.0)*k43,w1[3]+(439.0/216.0)*k14-8.0*k24+(3680.0/513.0)*k34-(845.0/4104.0)*k44,w1[4]+(439.0/216.0)*k15-8.0*k25+(3680.0/513.0)*k35-(845.0/4104.0)*k45,w1[5]+(439.0/216.0)*k16-8.0*k26+(3680.0/513.0)*k36-(845.0/4104.0)*k46)
		k53=h*funcion3(vector_t[i-1]+h,w1[0]+(439.0/216.0)*k11-8.0*k21+(3680.0/513.0)*k31-(845.0/4104.0)*k41,w1[1]+(439.0/216.0)*k12-8.0*k22+(3680.0/513.0)*k32-(845.0/4104.0)*k42,w1[2]+(439.0/216.0)*k13-8.0*k23+(3680.0/513.0)*k33-(845.0/4104.0)*k43,w1[3]+(439.0/216.0)*k14-8.0*k24+(3680.0/513.0)*k34-(845.0/4104.0)*k44,w1[4]+(439.0/216.0)*k15-8.0*k25+(3680.0/513.0)*k35-(845.0/4104.0)*k45,w1[5]+(439.0/216.0)*k16-8.0*k26+(3680.0/513.0)*k36-(845.0/4104.0)*k46)
		k54=h*funcion4(vector_t[i-1]+h,w1[0]+(439.0/216.0)*k11-8.0*k21+(3680.0/513.0)*k31-(845.0/4104.0)*k41,w1[1]+(439.0/216.0)*k12-8.0*k22+(3680.0/513.0)*k32-(845.0/4104.0)*k42,w1[2]+(439.0/216.0)*k13-8.0*k23+(3680.0/513.0)*k33-(845.0/4104.0)*k43,w1[3]+(439.0/216.0)*k14-8.0*k24+(3680.0/513.0)*k34-(845.0/4104.0)*k44,w1[4]+(439.0/216.0)*k15-8.0*k25+(3680.0/513.0)*k35-(845.0/4104.0)*k45,w1[5]+(439.0/216.0)*k16-8.0*k26+(3680.0/513.0)*k36-(845.0/4104.0)*k46)
		k55=h*funcion5(vector_t[i-1]+h,w1[0]+(439.0/216.0)*k11-8.0*k21+(3680.0/513.0)*k31-(845.0/4104.0)*k41,w1[1]+(439.0/216.0)*k12-8.0*k22+(3680.0/513.0)*k32-(845.0/4104.0)*k42,w1[2]+(439.0/216.0)*k13-8.0*k23+(3680.0/513.0)*k33-(845.0/4104.0)*k43,w1[3]+(439.0/216.0)*k14-8.0*k24+(3680.0/513.0)*k34-(845.0/4104.0)*k44,w1[4]+(439.0/216.0)*k15-8.0*k25+(3680.0/513.0)*k35-(845.0/4104.0)*k45,w1[5]+(439.0/216.0)*k16-8.0*k26+(3680.0/513.0)*k36-(845.0/4104.0)*k46)
		k56=h*funcion6(vector_t[i-1]+h,w1[0]+(439.0/216.0)*k11-8.0*k21+(3680.0/513.0)*k31-(845.0/4104.0)*k41,w1[1]+(439.0/216.0)*k12-8.0*k22+(3680.0/513.0)*k32-(845.0/4104.0)*k42,w1[2]+(439.0/216.0)*k13-8.0*k23+(3680.0/513.0)*k33-(845.0/4104.0)*k43,w1[3]+(439.0/216.0)*k14-8.0*k24+(3680.0/513.0)*k34-(845.0/4104.0)*k44,w1[4]+(439.0/216.0)*k15-8.0*k25+(3680.0/513.0)*k35-(845.0/4104.0)*k45,w1[5]+(439.0/216.0)*k16-8.0*k26+(3680.0/513.0)*k36-(845.0/4104.0)*k46)
		k61=h*funcion1(vector_t[i-1]+(h/2.0),w1[0]-(8.0/27.0)*k11+2.0*k21-(3544.0/2565.0)*k31+(1859.0/4104.0)*k41-(11.0/40.0)*k51,w1[1]-(8.0/27.0)*k12+2.0*k22-(3544.0/2565.0)*k32+(1859.0/4104.0)*k42-(11.0/40.0)*k52,w1[2]-(8.0/27.0)*k13+2.0*k23-(3544.0/2565.0)*k33+(1859.0/4104.0)*k43-(11.0/40.0)*k53,w1[3]-(8.0/27.0)*k14+2.0*k24-(3544.0/2565.0)*k34+(1859.0/4104.0)*k44-(11.0/40.0)*k54,w1[4]-(8.0/27.0)*k15+2.0*k25-(3544.0/2565.0)*k35+(1859.0/4104.0)*k45-(11.0/40.0)*k55,w1[5]-(8.0/27.0)*k16+2.0*k26-(3544.0/2565.0)*k36+(1859.0/4104.0)*k46-(11.0/40.0)*k56)
		k62=h*funcion2(vector_t[i-1]+(h/2.0),w1[0]-(8.0/27.0)*k11+2.0*k21-(3544.0/2565.0)*k31+(1859.0/4104.0)*k41-(11.0/40.0)*k51,w1[1]-(8.0/27.0)*k12+2.0*k22-(3544.0/2565.0)*k32+(1859.0/4104.0)*k42-(11.0/40.0)*k52,w1[2]-(8.0/27.0)*k13+2.0*k23-(3544.0/2565.0)*k33+(1859.0/4104.0)*k43-(11.0/40.0)*k53,w1[3]-(8.0/27.0)*k14+2.0*k24-(3544.0/2565.0)*k34+(1859.0/4104.0)*k44-(11.0/40.0)*k54,w1[4]-(8.0/27.0)*k15+2.0*k25-(3544.0/2565.0)*k35+(1859.0/4104.0)*k45-(11.0/40.0)*k55,w1[5]-(8.0/27.0)*k16+2.0*k26-(3544.0/2565.0)*k36+(1859.0/4104.0)*k46-(11.0/40.0)*k56)
		k63=h*funcion3(vector_t[i-1]+(h/2.0),w1[0]-(8.0/27.0)*k11+2.0*k21-(3544.0/2565.0)*k31+(1859.0/4104.0)*k41-(11.0/40.0)*k51,w1[1]-(8.0/27.0)*k12+2.0*k22-(3544.0/2565.0)*k32+(1859.0/4104.0)*k42-(11.0/40.0)*k52,w1[2]-(8.0/27.0)*k13+2.0*k23-(3544.0/2565.0)*k33+(1859.0/4104.0)*k43-(11.0/40.0)*k53,w1[3]-(8.0/27.0)*k14+2.0*k24-(3544.0/2565.0)*k34+(1859.0/4104.0)*k44-(11.0/40.0)*k54,w1[4]-(8.0/27.0)*k15+2.0*k25-(3544.0/2565.0)*k35+(1859.0/4104.0)*k45-(11.0/40.0)*k55,w1[5]-(8.0/27.0)*k16+2.0*k26-(3544.0/2565.0)*k36+(1859.0/4104.0)*k46-(11.0/40.0)*k56)
		k64=h*funcion4(vector_t[i-1]+(h/2.0),w1[0]-(8.0/27.0)*k11+2.0*k21-(3544.0/2565.0)*k31+(1859.0/4104.0)*k41-(11.0/40.0)*k51,w1[1]-(8.0/27.0)*k12+2.0*k22-(3544.0/2565.0)*k32+(1859.0/4104.0)*k42-(11.0/40.0)*k52,w1[2]-(8.0/27.0)*k13+2.0*k23-(3544.0/2565.0)*k33+(1859.0/4104.0)*k43-(11.0/40.0)*k53,w1[3]-(8.0/27.0)*k14+2.0*k24-(3544.0/2565.0)*k34+(1859.0/4104.0)*k44-(11.0/40.0)*k54,w1[4]-(8.0/27.0)*k15+2.0*k25-(3544.0/2565.0)*k35+(1859.0/4104.0)*k45-(11.0/40.0)*k55,w1[5]-(8.0/27.0)*k16+2.0*k26-(3544.0/2565.0)*k36+(1859.0/4104.0)*k46-(11.0/40.0)*k56)
		k65=h*funcion5(vector_t[i-1]+(h/2.0),w1[0]-(8.0/27.0)*k11+2.0*k21-(3544.0/2565.0)*k31+(1859.0/4104.0)*k41-(11.0/40.0)*k51,w1[1]-(8.0/27.0)*k12+2.0*k22-(3544.0/2565.0)*k32+(1859.0/4104.0)*k42-(11.0/40.0)*k52,w1[2]-(8.0/27.0)*k13+2.0*k23-(3544.0/2565.0)*k33+(1859.0/4104.0)*k43-(11.0/40.0)*k53,w1[3]-(8.0/27.0)*k14+2.0*k24-(3544.0/2565.0)*k34+(1859.0/4104.0)*k44-(11.0/40.0)*k54,w1[4]-(8.0/27.0)*k15+2.0*k25-(3544.0/2565.0)*k35+(1859.0/4104.0)*k45-(11.0/40.0)*k55,w1[5]-(8.0/27.0)*k16+2.0*k26-(3544.0/2565.0)*k36+(1859.0/4104.0)*k46-(11.0/40.0)*k56)
		k66=h*funcion6(vector_t[i-1]+(h/2.0),w1[0]-(8.0/27.0)*k11+2.0*k21-(3544.0/2565.0)*k31+(1859.0/4104.0)*k41-(11.0/40.0)*k51,w1[1]-(8.0/27.0)*k12+2.0*k22-(3544.0/2565.0)*k32+(1859.0/4104.0)*k42-(11.0/40.0)*k52,w1[2]-(8.0/27.0)*k13+2.0*k23-(3544.0/2565.0)*k33+(1859.0/4104.0)*k43-(11.0/40.0)*k53,w1[3]-(8.0/27.0)*k14+2.0*k24-(3544.0/2565.0)*k34+(1859.0/4104.0)*k44-(11.0/40.0)*k54,w1[4]-(8.0/27.0)*k15+2.0*k25-(3544.0/2565.0)*k35+(1859.0/4104.0)*k45-(11.0/40.0)*k55,w1[5]-(8.0/27.0)*k16+2.0*k26-(3544.0/2565.0)*k36+(1859.0/4104.0)*k46-(11.0/40.0)*k56)
		w1[0]=w1[0]+(25.0/216.0)*k11+(1408.0/2565.0)*k31+(2197.0/4104.0)*k41-(1.0/5.0)*k51
		W1[i][0]=w1[0]
		w1[1]=w1[1]+(25.0/216.0)*k12+(1408.0/2565.0)*k32+(2197.0/4104.0)*k42-(1.0/5.0)*k52
		W1[i][1]=w1[1]
		w1[2]=w1[2]+(25.0/216.0)*k13+(1408.0/2565.0)*k33+(2197.0/4104.0)*k43-(1.0/5.0)*k53
		W1[i][2]=w1[2]
		w1[3]=w1[3]+(25.0/216.0)*k14+(1408.0/2565.0)*k34+(2197.0/4104.0)*k44-(1.0/5.0)*k54
		W1[i][3]=w1[3]
		w1[4]=w1[4]+(25.0/216.0)*k15+(1408.0/2565.0)*k35+(2197.0/4104.0)*k45-(1.0/5.0)*k55
		W1[i][4]=w1[4]
		w1[5]=w1[5]+(25.0/216.0)*k16+(1408.0/2565.0)*k36+(2197.0/4104.0)*k46-(1.0/5.0)*k56
		W1[i][5]=w1[5]
		w2[0]=w2[0]+(16.0/135.0)*k11+(6656.0/12825.0)*k31+(28561.0/56430.0)*k41-(9.0/50.0)*k51+(2.0/55.0)*k61
                if abs(w1[0]-w2[0])!=0.0:
                        lo=(0.5*(h**5)*error/abs(w1[0]-w2[0]))**(1.0/4.0)
                        h_new.append(lo)
		w2[1]=w2[1]+(16.0/135.0)*k12+(6656.0/12825.0)*k32+(28561.0/56430.0)*k42-(9.0/50.0)*k52+(2.0/55.0)*k62
                if abs(w1[1]-w2[1])!=0.0:
                        lo=(0.5*(h**5)*error/abs(w1[1]-w2[1]))**(1.0/4.0)
                        h_new.append(lo)
		w2[2]=w2[2]+(16.0/135.0)*k13+(6656.0/12825.0)*k33+(28561.0/56430.0)*k43-(9.0/50.0)*k53+(2.0/55.0)*k63
                if abs(w1[2]-w2[2])!=0.0:
                        lo=(0.5*(h**5)*error/abs(w1[2]-w2[2]))**(1.0/4.0)
                        h_new.append(lo)
		w2[3]=w2[3]+(16.0/135.0)*k14+(6656.0/12825.0)*k34+(28561.0/56430.0)*k44-(9.0/50.0)*k54+(2.0/55.0)*k64
                if abs(w1[3]-w2[3])!=0.0:
                        lo=(0.5*(h**5)*error/abs(w1[3]-w2[3]))**(1.0/4.0)
                        h_new.append(lo)
		w2[4]=w2[4]+(16.0/135.0)*k15+(6656.0/12825.0)*k35+(28561.0/56430.0)*k45-(9.0/50.0)*k55+(2.0/55.0)*k65
                if abs(w1[4]-w2[4])!=0.0:
                        lo=(0.5*(h**5)*error/abs(w1[4]-w2[4]))**(1.0/4.0)
                        h_new.append(lo)
		w2[5]=w2[5]+(16.0/135.0)*k16+(6656.0/12825.0)*k36+(28561.0/56430.0)*k46-(9.0/50.0)*k56+(2.0/55.0)*k66
                if abs(w1[5]-w2[5])!=0.0:
                        lo=(0.5*(h**5)*error/abs(w1[5]-w2[5]))**(1.0/4.0)
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
def verticalnc(t,M):
        for j in range(0,len(M)):
                print t[j],M[j][0],M[j][1],M[j][2],M[j][3],M[j][4],M[j][5]
	return ""
F=Runge_kutta_s2(U,w,xa,xb,de,h)
vt=F[0]
H=F[1]
hn=F[2]
hmin=F[3]
print vertical2(vt,H)
print 'h=',hn
print 'hmin=',hmin