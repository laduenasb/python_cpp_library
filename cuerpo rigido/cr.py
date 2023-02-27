from sys import path
path.append("/media/luis/MYLINUXLIVE1/programasl")
from definiciones import *
U=['u3', 'u5', '((Ixz*cos(u4)-Ixy*sin(u4))*(m*g*ycm*cos(u4)+m*g*zcm*sin(u4)+(-Iyy*sin(u4)*cos(u4)+Izz*sin(u4)*cos(u4)+Iyz*cos(2*u4))*u3**2)-Ix*((Ixz*sin(u4)+Ixy*cos(u4))*u5**2-2*u3*u5*(-Iyy*sin(u4)*cos(u4)+Izz*sin(u4)*cos(u4)+Iyz*cos(2*u4))))/((Ixz*cos(u4)-Ixy*sin(u4))**2-Ix*(Ixx+Iyy*(cos(u4)**2)+Izz*(sin(u4))**2+Iyz*sin(2*u4)))', '((Ixz*cos(u4)-Ixy*sin(u4))*((Ixz*sin(u4)+Ixy*cos(u4))*u5**2-2*u3*u5*(-Iyy*sin(u4)*cos(u4)+Izz*sin(u4)*cos(u4)+Iyz*cos(u4)+Iyz*cos(2*u4)))-(Ixx+Iyy*(cos(u4)**2)+Izz*(sin(u4)**2)+Iyz*sin(2*u4))*(m*g*ycm*cos(u4)+m*g*zcm*sin(u4)+(-Iyy*sin(u4)*cos(u4)+Izz*sin(u4)*cos(u4)+Iyz*cos(2*u4))*(u3**2)))/((Ixz*cos(u4)-Ixy*sin(u4))**2-Ix*(Ixx+Iyy*(cos(u4)**2)+Izz*(sin(u4))**2+Iyz*sin(2*u4)))']
xa=0.0
xb=1.0
de=6
h=1e-4
w=[0.0, 0.0, 0.0, 0.0]
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
        xk=[0.0]
        error=10**(-de-1)
        for i in range(0,len(w)):
                w1.append(float(w[i]))
                w2.append(float(w[i]))
                w9.append(float(w[i]))
                W1[0][i]=float(w[i])
        def funcion1(u1,u2,u3,u4,u5):
                f=u3
                return f
        def funcion2(u1,u2,u3,u4,u5):
                f=u5
                return f
        def funcion3(u1,u2,u3,u4,u5):                
                m=1.0
                g=9.8
                ycm=3.0
                zcm=-6.0
                Ixx=4.0
                Iyy=9.0
                Izz=36.0
                Iyz=-18.0
                Ixz=-12.0
                Ixy=6.0
                Ix=Iyy+Izz
                jkl=((Ixz*cos(u4)-Ixy*sin(u4))**2-Ix*(Ixx+Iyy*(cos(u4)**2)+Izz*(sin(u4)**2)+Iyz*sin(2*u4)))                
                f=((Ixz*cos(u4)-Ixy*sin(u4))*(m*g*ycm*cos(u4)+m*g*zcm*sin(u4)+(-Iyy*sin(u4)*cos(u4)+Izz*sin(u4)*cos(u4)+Iyz*cos(2*u4))*u3**2)-Ix*((Ixz*sin(u4)+Ixy*cos(u4))*(u5**2)-2*u3*u5*(-Iyy*sin(u4)*cos(u4)+Izz*sin(u4)*cos(u4)+Iyz*cos(2*u4))))/jkl                
                return f
        def funcion4(u1,u2,u3,u4,u5):
                m=1.0
                g=9.8
                ycm=3.0
                zcm=-6.0
                Ixx=4.0
                Iyy=9.0
                Izz=36.0
                Iyz=-18.0
                Ixz=-12.0
                Ixy=6.0
                Ix=Iyy+Izz
                jkl=((Ixz*cos(u4)-Ixy*sin(u4))**2-Ix*(Ixx+Iyy*(cos(u4)**2)+Izz*(sin(u4)**2)+Iyz*sin(2*u4)))
                f=((Ixz*cos(u4)-Ixy*sin(u4))*((Ixz*sin(u4)+Ixy*cos(u4))*(u5**2)-2*u3*u5*(-Iyy*sin(u4)*cos(u4)+Izz*sin(u4)*cos(u4)+Iyz*cos(2*u4)))-(Ixx+Iyy*(cos(u4)**2)+Izz*(sin(u4)**2)+Iyz*sin(2*u4))*(m*g*ycm*cos(u4)+m*g*zcm*sin(u4)+(-Iyy*sin(u4)*cos(u4)+Izz*sin(u4)*cos(u4)+Iyz*cos(2*u4))*(u3**2)))                
                return f        
        for i in range(1,len(vector_t)):
		k11=h*funcion1(vector_t[i-1],w1[0],w1[1],w1[2],w1[3])
#		print k11,i
		k12=h*funcion2(vector_t[i-1],w1[0],w1[1],w1[2],w1[3])
#		print k12
		k13=h*funcion3(vector_t[i-1],w1[0],w1[1],w1[2],w1[3])
#		print k13
		k14=h*funcion4(vector_t[i-1],w1[0],w1[1],w1[2],w1[3])
#		print k14
		k21=h*funcion1(vector_t[i-1]+(h/4.0),w1[0]+(1.0/4.0)*k11,w1[1]+(1.0/4.0)*k12,w1[2]+(1.0/4.0)*k13,w1[3]+(1.0/4.0)*k14)
#		print k21
		k22=h*funcion2(vector_t[i-1]+(h/4.0),w1[0]+(1.0/4.0)*k11,w1[1]+(1.0/4.0)*k12,w1[2]+(1.0/4.0)*k13,w1[3]+(1.0/4.0)*k14)
#		print k22
		k23=h*funcion3(vector_t[i-1]+(h/4.0),w1[0]+(1.0/4.0)*k11,w1[1]+(1.0/4.0)*k12,w1[2]+(1.0/4.0)*k13,w1[3]+(1.0/4.0)*k14)
#		print k23
		k24=h*funcion4(vector_t[i-1]+(h/4.0),w1[0]+(1.0/4.0)*k11,w1[1]+(1.0/4.0)*k12,w1[2]+(1.0/4.0)*k13,w1[3]+(1.0/4.0)*k14)
#		print k24
		k31=h*funcion1(vector_t[i-1]+(3.0*h/8.0),w1[0]+(3.0/32.0)*k11+(9.0/32.0)*k21,w1[1]+(3.0/32.0)*k12+(9.0/32.0)*k22,w1[2]+(3.0/32.0)*k13+(9.0/32.0)*k23,w1[3]+(3.0/32.0)*k14+(9.0/32.0)*k24)
#		print k31
		k32=h*funcion2(vector_t[i-1]+(3.0*h/8.0),w1[0]+(3.0/32.0)*k11+(9.0/32.0)*k21,w1[1]+(3.0/32.0)*k12+(9.0/32.0)*k22,w1[2]+(3.0/32.0)*k13+(9.0/32.0)*k23,w1[3]+(3.0/32.0)*k14+(9.0/32.0)*k24)
#		print k32
		k33=h*funcion3(vector_t[i-1]+(3.0*h/8.0),w1[0]+(3.0/32.0)*k11+(9.0/32.0)*k21,w1[1]+(3.0/32.0)*k12+(9.0/32.0)*k22,w1[2]+(3.0/32.0)*k13+(9.0/32.0)*k23,w1[3]+(3.0/32.0)*k14+(9.0/32.0)*k24)
#		print k33
		k34=h*funcion4(vector_t[i-1]+(3.0*h/8.0),w1[0]+(3.0/32.0)*k11+(9.0/32.0)*k21,w1[1]+(3.0/32.0)*k12+(9.0/32.0)*k22,w1[2]+(3.0/32.0)*k13+(9.0/32.0)*k23,w1[3]+(3.0/32.0)*k14+(9.0/32.0)*k24)
#		print k34
		k41=h*funcion1(vector_t[i-1]+(12.0*h/13.0),w1[0]+(1932.0/2197.0)*k11-(7200.0/2197.0)*k21+(7296.0/2197.0)*k31,w1[1]+(1932.0/2197.0)*k12-(7200.0/2197.0)*k22+(7296.0/2197.0)*k32,w1[2]+(1932.0/2197.0)*k13-(7200.0/2197.0)*k23+(7296.0/2197.0)*k33,w1[3]+(1932.0/2197.0)*k14-(7200.0/2197.0)*k24+(7296.0/2197.0)*k34)
#		print k41
		k42=h*funcion2(vector_t[i-1]+(12.0*h/13.0),w1[0]+(1932.0/2197.0)*k11-(7200.0/2197.0)*k21+(7296.0/2197.0)*k31,w1[1]+(1932.0/2197.0)*k12-(7200.0/2197.0)*k22+(7296.0/2197.0)*k32,w1[2]+(1932.0/2197.0)*k13-(7200.0/2197.0)*k23+(7296.0/2197.0)*k33,w1[3]+(1932.0/2197.0)*k14-(7200.0/2197.0)*k24+(7296.0/2197.0)*k34)
#		print k42
		k43=h*funcion3(vector_t[i-1]+(12.0*h/13.0),w1[0]+(1932.0/2197.0)*k11-(7200.0/2197.0)*k21+(7296.0/2197.0)*k31,w1[1]+(1932.0/2197.0)*k12-(7200.0/2197.0)*k22+(7296.0/2197.0)*k32,w1[2]+(1932.0/2197.0)*k13-(7200.0/2197.0)*k23+(7296.0/2197.0)*k33,w1[3]+(1932.0/2197.0)*k14-(7200.0/2197.0)*k24+(7296.0/2197.0)*k34)
		k44=h*funcion4(vector_t[i-1]+(12.0*h/13.0),w1[0]+(1932.0/2197.0)*k11-(7200.0/2197.0)*k21+(7296.0/2197.0)*k31,w1[1]+(1932.0/2197.0)*k12-(7200.0/2197.0)*k22+(7296.0/2197.0)*k32,w1[2]+(1932.0/2197.0)*k13-(7200.0/2197.0)*k23+(7296.0/2197.0)*k33,w1[3]+(1932.0/2197.0)*k14-(7200.0/2197.0)*k24+(7296.0/2197.0)*k34)
		k51=h*funcion1(vector_t[i-1]+h,w1[0]+(439.0/216.0)*k11-8.0*k21+(3680.0/513.0)*k31-(845.0/4104.0)*k41,w1[1]+(439.0/216.0)*k12-8.0*k22+(3680.0/513.0)*k32-(845.0/4104.0)*k42,w1[2]+(439.0/216.0)*k13-8.0*k23+(3680.0/513.0)*k33-(845.0/4104.0)*k43,w1[3]+(439.0/216.0)*k14-8.0*k24+(3680.0/513.0)*k34-(845.0/4104.0)*k44)
		k52=h*funcion2(vector_t[i-1]+h,w1[0]+(439.0/216.0)*k11-8.0*k21+(3680.0/513.0)*k31-(845.0/4104.0)*k41,w1[1]+(439.0/216.0)*k12-8.0*k22+(3680.0/513.0)*k32-(845.0/4104.0)*k42,w1[2]+(439.0/216.0)*k13-8.0*k23+(3680.0/513.0)*k33-(845.0/4104.0)*k43,w1[3]+(439.0/216.0)*k14-8.0*k24+(3680.0/513.0)*k34-(845.0/4104.0)*k44)
		k53=h*funcion3(vector_t[i-1]+h,w1[0]+(439.0/216.0)*k11-8.0*k21+(3680.0/513.0)*k31-(845.0/4104.0)*k41,w1[1]+(439.0/216.0)*k12-8.0*k22+(3680.0/513.0)*k32-(845.0/4104.0)*k42,w1[2]+(439.0/216.0)*k13-8.0*k23+(3680.0/513.0)*k33-(845.0/4104.0)*k43,w1[3]+(439.0/216.0)*k14-8.0*k24+(3680.0/513.0)*k34-(845.0/4104.0)*k44)
		k54=h*funcion4(vector_t[i-1]+h,w1[0]+(439.0/216.0)*k11-8.0*k21+(3680.0/513.0)*k31-(845.0/4104.0)*k41,w1[1]+(439.0/216.0)*k12-8.0*k22+(3680.0/513.0)*k32-(845.0/4104.0)*k42,w1[2]+(439.0/216.0)*k13-8.0*k23+(3680.0/513.0)*k33-(845.0/4104.0)*k43,w1[3]+(439.0/216.0)*k14-8.0*k24+(3680.0/513.0)*k34-(845.0/4104.0)*k44)
		k61=h*funcion1(vector_t[i-1]+(h/2.0),w1[0]-(8.0/27.0)*k11+2.0*k21-(3544.0/2565.0)*k31+(1859.0/4104.0)*k41-(11.0/40.0)*k51,w1[1]-(8.0/27.0)*k12+2.0*k22-(3544.0/2565.0)*k32+(1859.0/4104.0)*k42-(11.0/40.0)*k52,w1[2]-(8.0/27.0)*k13+2.0*k23-(3544.0/2565.0)*k33+(1859.0/4104.0)*k43-(11.0/40.0)*k53,w1[3]-(8.0/27.0)*k14+2.0*k24-(3544.0/2565.0)*k34+(1859.0/4104.0)*k44-(11.0/40.0)*k54)
		k62=h*funcion2(vector_t[i-1]+(h/2.0),w1[0]-(8.0/27.0)*k11+2.0*k21-(3544.0/2565.0)*k31+(1859.0/4104.0)*k41-(11.0/40.0)*k51,w1[1]-(8.0/27.0)*k12+2.0*k22-(3544.0/2565.0)*k32+(1859.0/4104.0)*k42-(11.0/40.0)*k52,w1[2]-(8.0/27.0)*k13+2.0*k23-(3544.0/2565.0)*k33+(1859.0/4104.0)*k43-(11.0/40.0)*k53,w1[3]-(8.0/27.0)*k14+2.0*k24-(3544.0/2565.0)*k34+(1859.0/4104.0)*k44-(11.0/40.0)*k54)
		k63=h*funcion3(vector_t[i-1]+(h/2.0),w1[0]-(8.0/27.0)*k11+2.0*k21-(3544.0/2565.0)*k31+(1859.0/4104.0)*k41-(11.0/40.0)*k51,w1[1]-(8.0/27.0)*k12+2.0*k22-(3544.0/2565.0)*k32+(1859.0/4104.0)*k42-(11.0/40.0)*k52,w1[2]-(8.0/27.0)*k13+2.0*k23-(3544.0/2565.0)*k33+(1859.0/4104.0)*k43-(11.0/40.0)*k53,w1[3]-(8.0/27.0)*k14+2.0*k24-(3544.0/2565.0)*k34+(1859.0/4104.0)*k44-(11.0/40.0)*k54)
		k64=h*funcion4(vector_t[i-1]+(h/2.0),w1[0]-(8.0/27.0)*k11+2.0*k21-(3544.0/2565.0)*k31+(1859.0/4104.0)*k41-(11.0/40.0)*k51,w1[1]-(8.0/27.0)*k12+2.0*k22-(3544.0/2565.0)*k32+(1859.0/4104.0)*k42-(11.0/40.0)*k52,w1[2]-(8.0/27.0)*k13+2.0*k23-(3544.0/2565.0)*k33+(1859.0/4104.0)*k43-(11.0/40.0)*k53,w1[3]-(8.0/27.0)*k14+2.0*k24-(3544.0/2565.0)*k34+(1859.0/4104.0)*k44-(11.0/40.0)*k54)
		w1[0]=w1[0]+(25.0/216.0)*k11+(1408.0/2565.0)*k31+(2197.0/4104.0)*k41-(1.0/5.0)*k51
		W1[i][0]=asin(sin(w1[0]))*180/pi
#		print w1[0]*180/pi
		w1[1]=w1[1]+(25.0/216.0)*k12+(1408.0/2565.0)*k32+(2197.0/4104.0)*k42-(1.0/5.0)*k52
		W1[i][1]=asin(sin(w1[1]))*180/pi
		w1[2]=w1[2]+(25.0/216.0)*k13+(1408.0/2565.0)*k33+(2197.0/4104.0)*k43-(1.0/5.0)*k53
		W1[i][2]=asin(sin(w1[2]))*180/pi
		w1[3]=w1[3]+(25.0/216.0)*k14+(1408.0/2565.0)*k34+(2197.0/4104.0)*k44-(1.0/5.0)*k54
		xk.append(-3.0*sin(w1[0])*cos(w1[2])-9.0*sin(w1[0])*sin(w1[2]))
		W1[i][3]=asin(sin(w1[3]))*180/pi
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
        return vector_t,W1,h,minimo(h_new),xk
F=Runge_kutta_s2(U,w,xa,xb,de,h)
vt=F[0]
H=F[1]
hn=F[2]
hmin=F[3]
xk=F[4]
print vertical3(vt,H,xk)
print 'h=',hn
print 'hmin=',hmin    
print vt[len(vt)-400],H[len(vt)-400][0],H[len(vt)-400][1],H[len(vt)-400][2],H[len(vt)-400][3]
print vt[len(vt)-300],H[len(vt)-300][0],H[len(vt)-300][1],H[len(vt)-300][2],H[len(vt)-300][3]
print vt[len(vt)-200],H[len(vt)-200][0],H[len(vt)-200][1],H[len(vt)-200][2],H[len(vt)-200][3]
print vt[20],H[20][0],H[20][1],H[20][2],H[20][3]
print atan(-6.0/3.0)*180/pi
