#-*-coding:utf-8-*- 
from matplotlib import pyplot
from math import *
#from sympy import *
#from sympy import Rational as R
#u1,u2,u3,u4,u5,u6,u7,x=symbols("u1,u2,u3,u4,u5,u6,u7,x")
def ncrear(kl):   #### codigo para escribir los vectores x1,x2,...,xn de U=[x1,x2,...,xn] en columnas en el fichero .dat con U una matriz donde sus filas son los vectores x1,x2,...,xn, de izquierda a derecha en el mismo orden en que se ubican en U, con kl=len(U)
        print("def n"+str(kl)+"crear(U,n1,g): ### n1 nombre del fichero a crear o modificar y g nombre de los .dat al abrir el fichero, los nombres deben estar entre comillas")
        print('        xv="####"+g')
        print('        k=open(n1,"w")')
        print('        k.write(xv)')
        print('        k.write("\\n")')
        print('        for i in range(0,len(U[0])):')
        for i in range(0,kl):
                print('                s'+str(i)+'='+'str(U['+str(i)+'][i])')
        print('                e=" "')                
        ax=""
        e="+e+"
        for j in range(0,kl-1):
                ax+='s'+str(j)+e
        ax+='s'+str(kl-1)
        print('                jl='+ax)
        print('                k.write(jl)')
        print('                k.write("\\n")')
        print('        k.close()')
        print('        return ""')
        return ""
def nvertical(k): ### k el numero de vectores que se muestran en forma vertical, U=[x1,x2,...,xn], Matriz U con filas los vectores x1,x2,...,xn. codigo de la definicion escrita para mostrar de forma vertical los vectores x1,x2,...,xn de izquierda a derecha, donde x1,x2,...,xn tienen la misma longitud.
        print("def n"+str(k)+"vertical(U):")
        print("        for i in range(0,len(U[0])):")
        a=""
        for i in range(0,k-1):
                a+="U["+str(i)+"]"+"[i],"
        a+="U["+str(k-1)+"][i]"
        print("                print "+a)
        print('        return ""')
        return ""
def vertical(x): #mostrar matrices de forma vertical
        for i in range(0,len(x)-1):
                pprint(x[i])
        pprint(x[i+1])
        return ""
def vertical2(x,y): #### mostrar en columnas los vectores x,y
	for i in range(0,len(x)):
		print(x[i],y[i])
	return ""
def vertical3(x,y,z): ## mostrar en columnas los vectores x,y,z
	for i in range(0,len(x)):
		print(x[i],y[i],z[i])
	return "" 
def vertical4(x,y,z,k): ## mostrar en columnas los vectores x,y,z,k
	for i in range(0,len(x)):
		print(x[i],y[i],z[i],k[i])
	return "" 
def cambiar(M,n):  #intercambia con otra fila por debajo de la fila n-esima, tal que M[n][n]!=0 sin alterar las anteriores filas a n-esima
	if M[n][n]==0:
		for i in range(n+1,len(M)):
				if M[i][n]!=0:
					fd=M[n]
					M[n]=M[i]
					M[i]=fd
					break
	return M
def solucion(M): #muestra las soluciones de la matriz M por gaussjordan
        n=0
        while n<=(len(M)-1):  #reduciendo a cero los elementos diferentes de la diagonal de la matriz M
                cambiar(M,n)
                for i in range(0,len(M)):
                        gfj=float(M[i][n])
                        for j in range(0,len(M[0])):
                                if gfj!=0 and i!=n and M[n][n]!=0:
                                        M[i][j]=((M[i][j]*M[n][n])/gfj)-M[n][j]
                n+=1
        I=[]  #vector con elementos iguales al numero de la fila de la matriz dependiendo del caso
        try:
                x=[]
                for hj in range(0,len(M)):  #encontrando las soluciones de la matriz M 
                        fgk=M[hj][len(M)]/float(M[hj][hj])
                        hg="="
                        if M[len(M)-1][len(M)-1]!=0:
                                x.append(fgk)
        except ZeroDivisionError:
                for i in range(0,len(M)):
                        for j in range(0,len(M[0])):
                                if M[i][j]==0:
                                        I.append(i)
                k=True
                for i in range(I[0],len(I)):
                        if I.count(i)==(len(M[0])-1):
                                k=False
                                break
                if k==True:
                        print("El sistema de ecuaciones tiene infinitas soluciones")
                else:
                        print("El sistema de ecuaciones no tiene solucion")
        return x
def producto(A,B):   #producto entre matrices
        AB=[0.0]*len(A[0])
        for lkg in range(0,len(A[0])):
                AB[lkg]=[0.0]*len(B[0])
        for i in range(0,len(A)):
                for j in range(0,len(B[0])):
                        AB[i][j]=0
                        for r in range(0,len(B)):
                                AB[i][j]+=A[i][r]*B[r][j]
        return AB
def crear_matriz(i,j):  #i numero de filas, j numero de columnas
	A=[0.0]*int(i)
	for k in range(0,len(A)):
	        A[k]=[0.0]*int(j)
	return A
def crear_vector(xa,xb,k):   #xa y xb el intervalo con xa<xb, y k la cantidad de puntos
	deltax=(xb-xa)/(float(k)-1.0)
	x=[float(xa)]
	for i in range(0,int(k)-1):
		xa+=deltax
		x.append(xa)
	return x
def factorial(z):
        k=1
        for i in range(1,int(z)):
                k*=i+1
        return k
def incertidumbre(x,y):  ## x vector con los datos y "y" la minima cantidad que puede medir el instrumento de medicion
	sigma=0.0
	ELM=float(y)/2.0
	for i in range(0,len(x)):
		sigma+=((promedio(x)-x[i])**2.0)/float(len(x))
	sigma=sigma**0.5
	Ea=3.0*sigma/(float(len(x)-1.0)**0.5)
	Error=((ELM**2.0)+(Ea**2.0))**0.5
	E=str(Error)
	D="x= "
	G=" +- "	
	P=str(promedio(x))
	print("El valor de la medicion es:")
	return D+P+G+E
def error_suma(x,dx,y,dy):   #### "x" y "y" son promedios de un conjunto de datos,cuando queremos hallar x+y, dx y dy sus incertidumbres respectivamente
	z=float(x)+float(y)
	dz=((dx**2.0)+(dy**2.0))**0.5
	k="z= "
	G=" +- "
	P=str(z)
	l=str(dz)
	print(k+P+G+l)
	return "" 	
def error_resta(x,dx,y,dy):   #### "x" y "y" son promedios de un conjunto de datos, cuando queremos hallar x-y, dx y dy sus incertidumbres respectivamente
	z=x-y
	dz=((dx**2.0)+(dy**2.0))**0.5
	k="z= "
	G=" +- "
	P=str(z)
	l=str(dz)
	print(k+P+G+l)
	return "" 
def error_multiplicacion(x,dx,y,dy): ### cuando queremos hallar x*y
	z=float(x)*float(y)
	dz=z*((((float(dx)/float(x))**2.0)+((float(dy)/float(y))**2.0))**0.5)
	k="z= "
	G=" +- "
	P=str(z)
	l=str(dz)
	print(k+P+G+l)
	return ""
def error_division(x,dx,y,dy):  ##cuando queremos hallar x/y
        z=float(x)/float(y)
        dz=z*((((float(dx)/float(x))**2.0)+((float(dy)/float(y))**2.0))**0.5)
        k="z= "
        G=" +- "
        P=str(z)
        l=str(dz)
        print(k+P+G+l)
        return ""	
def error_potenciacion(x,dx,exp,k):  ### cuando queremos hallar k*(x^exp)
	z=k*(float(x)**exp)	
	dz=exp*(float(dx)/float(x))*z
	k="z= "
	G=" +- "
	P=str(z)
	l=str(dz)
	print(k+P+G+l)
	return ""
def promedio(x):
	p=0.0  ##promedio
	for i in range(0,len(x)):
		p+=x[i]
	p=p/float(len(x))
	return p
def desviacion_estandar(x):   ##x = vector de los datos, y p el promedio de los datos
	p=promedio(x)
	s=0.0  ##desviacion estandar
	for i in range(0,len(x)):
		s+=(x[i]-p)**2.0
	s=(s/(len(x)-1.0))**0.5
	return s
def minimos_cuadrados(x,y):   #### x eje x, y eje y
	from math import factorial as fac
	kj=1.0
	while kj<=len(x)*(len(x)-1.0)/2.0:
		for j in range(0,len(x)-1):
			if x[j]>x[j+1]:#cuando ordene los a, hara los mismos cambios al vector b                                
				n=x[j]
				x[j]=x[j+1]
				x[j+1]=n
				l=y[j]
				y[j]=y[j+1]
				y[j+1]=l
				break
		kj+=1.0
	s_xi=0.0   #suma(xi)
	s_yi=0.0   #suma(yi)
	s_xiyi=0.0 #suma(xi*yi) 
	s_xixi=0.0 #suma(xi**2)
	s_yiyi=0.0 #suma(yi**2)
	k=0.0
	def lineal(x,a,b): #y=a*x+b
		y=a*x+b
		return y
	for i in range(0,len(x)):
		s_xi+=x[i]
		s_yi+=y[i]
		s_xixi+=x[i]**2.0
		s_xiyi+=x[i]*y[i]
		s_yiyi+=y[i]**2.0
	sxy=s_xiyi-(s_xi*s_yi/float(len(x)))
	sxx=s_xixi-((s_xi**2.0)/float(len(x)))
	syy=s_yiyi-((s_yi**2.0)/float(len(x)))
	r=sxy/((sxx*syy)**0.5)
	a0=((s_xixi*s_yi)-(s_xiyi*s_xi))/((len(x)*s_xixi)-((s_xi)**2.0)) #intercepto  
	a1=((len(x)*s_xiyi)-(s_xi*s_yi))/((len(x)*s_xixi)-((s_xi)**2.0)) #pendiente
	print()
	print("#El intercepto y la pendiente de la recta son respectivamente:")
	print()
	print("#a0=",a0)
	print("#a1=",a1)
	E=0.0
	for i in range(0,len(y)):
		E+=(y[i]-(a1*x[i]+a0))**2.0  #error=sumatoria(yi-(a1*xi+a0))  
	print()
	sigma=(E/(len(x)-2.0))
	deltam=sigma*((len(x)/((len(x)*s_xixi)-((s_xi)**2.0)))**0.5)
	deltab=sigma*((((s_xi)**2.0)/((len(x)*s_xixi)-((s_xi)**2.0)))**0.5)
	print("#Error=",E)
	print()
	print("#Deltam=",deltam)
	print()
	print("#Deltab=",deltab)
	print()
	print("#r=",r)
	print()
	xa=x[0]
	xb=x[len(x)-1]
	npuntos=100.0
	deltax=(xb-xa)/(npuntos-1.0)
	x_puntos=[xa]  #grilla para x
	y_puntos=[]    #grilla para y           
	for jk in range(0,int(npuntos)-1):
		xa+=deltax
		x_puntos.append(xa)
	for hj in range(0,int(npuntos)):
		l=lineal(x_puntos[hj],a1,a0)
		y_puntos.append(l)
	pyplot.plot(x,y,"*",x_puntos,y_puntos)
	pyplot.show()
	print(vertical2(x,y))
	return ""
#n1 nombre del archivo donde se encuentran los datos nombre.dat
#n2 nombre de los puntos experimentales que aparecen arriba en la derecha, por ejemplo puntos experimentales
#x nombre del eje x
#y nombre del eje y
#t titulo de los datos 
#f la funcion que queremos graficar
#nf nombre de la funcion a graficar
### para cargar el archivo a donde se envia escribir en la consola de gnuplot load "nombre.g" por ejemplo
def grafica():
	x=str(input("Nombre del eje x: "))
	print(x)
	y=str(input("Nombre del eje y: "))
	print(y)
	t=str(input("Titulo de la grafica: "))
	print(t)
	n1=str(input("Nombre del .dat: "))
	print(n1)
	n2=str(input("Nombre de los datos: "))
	print(n2)
	f=str(input("F(x)=: "))
	print(f)
	nf=str(input("Nombre de F(x): "))	
	print(nf)
	print()
	h='"'
	k=")"
	z=","
	print("set xlabel("+h+x+h+k)
	print("set ylabel("+h+y+h+k)
	print("set title("+h+t+h+k)
	print('set label 1 "r=0.99" at 0.0,0.0')
	print("plot",h+n1+h,"t",h+n2+h+z,f,"t",h+nf+h)
	return ""
def crear2(x,y,n1,g):  ### crear un fichero de nombre n1 y titulo g con los vectores x,y en colummna de izquierda a derecha, los nombres deben ir entre comillas
        xv="####"+g
        k=open(n1,"w")
        k.write(xv)
        k.write("\n")
        for i in range(0,len(x)):
                s=str(x[i])
                d=str(y[i])
                e=" "
                jl=s+e+d
                k.write(jl)
                k.write("\n")
        k.close()
        return ""
def crear3(x,y,z,n1,g): ### crear un fichero de nombre n1 y titulo g con los vectores x,y,z en colummna de izquierda a derecha, los nombres deden ir entre comillas 
	xv="####"+g
	k=open(n1,"w")
	k.write(xv)
	k.write("\n")
	for i in range(0,len(x)):
		s=str(x[i])
		d=str(y[i])
		we=str(z[i])
		e=" "
		jl=s+e+d+e+we
		k.write(jl)
		k.write("\n")
	k.close()
	return ""
def crear6(x1,y1,z1,x2,y2,z2,n1,g): ### crear un fichero de nombre g1 y titulo g con los vectores x1,y1,z1,x2,y2,z2 en colummna de izquierda a derecha, los nombres deben ir entre comillas
	xv="####"+g
	k=open(n1,"w")
	k.write(xv)
	k.write("\n")
	for i in range(0,len(x1)):
		s=str(x1[i])
		d=str(y1[i])
		we=str(z1[i])
		d1=str(x2[i])
		d2=str(y2[i])
		d3=str(z2[i])
		e=" "
		jl=s+e+d+e+we+e+d1+e+d2+e+d3
		k.write(jl)
		k.write("\n")
	k.close()
	return ""
def m_c(x,y,er,n1,g):   #### Minimos cuadrados 'x' vector del eje x, 'y' vector del eje y, con er el vector error del eje x con 'n1' nombre del fichero a crear o modificar y 'g' Titulo de los .dat al abrir el fichero, los nombres entre comillas
	from math import factorial as fac
	kj=1.0
	while kj<=len(x)*(len(x)-1.0)/2.0:
		for j in range(0,len(x)-1):
			if x[j]>x[j+1]:#cuando ordene los a, hara los mismos cambios al vector b                                
				n=x[j]
				x[j]=x[j+1]
				x[j+1]=n
				l=y[j]
				y[j]=y[j+1]
				y[j+1]=l
				break
		kj+=1.0
	print()
	xv="####"+g
	k=open(n1,"w")
	k.write(xv)
	k.write("\n")
	s_xi=0.0   #suma(xi)
	s_yi=0.0   #suma(yi)
	s_xiyi=0.0 #suma(xi*yi) 
	s_xixi=0.0 #suma(xi**2)
	s_yiyi=0.0 #suma(yi**2)
	def lineal(x,a,b): #y=a*x+b
		y=a*x+b
		return y
	for i in range(0,len(x)):
		s_xi+=x[i]
		s_yi+=y[i]
		s_xixi+=x[i]**2.0
		s_xiyi+=x[i]*y[i]
		s_yiyi+=y[i]**2.0
	sxy=s_xiyi-(s_xi*s_yi/float(len(x)))
	sxx=s_xixi-((s_xi**2.0)/float(len(x)))
	syy=s_yiyi-((s_yi**2.0)/float(len(x)))
	r=sxy/((sxx*syy)**0.5)
	a0=((s_xixi*s_yi)-(s_xiyi*s_xi))/((len(x)*s_xixi)-((s_xi)**2.0)) #intercepto  
	a1=((len(x)*s_xiyi)-(s_xi*s_yi))/((len(x)*s_xixi)-((s_xi)**2.0)) #pendiente
	dqw="El intercepto y la pendiente de la recta son respectivamente:"
	f1="#a0= "
	f2="#a1= "
	dqw="####"+dqw
	w1=str(a0)
	w2=str(a1)
	k.write(dqw)
	k.write("\n")
	k.write(f1+w1)
	k.write("\n")
	k.write(f2+w2)
	k.write("\n")
	E=0.0
	for i in range(0,len(y)):
		E+=(y[i]-(a1*x[i]+a0))**2.0  #error=sumatoria(yi-(a1*xi+a0))**2.0  
	sigma=(E/(len(x)-2.0))
	deltam=sigma*((len(x)/((len(x)*s_xixi)-((s_xi)**2.0)))**0.5)
	deltab=sigma*((((s_xi)**2.0)/((len(x)*s_xixi)-((s_xi)**2.0)))**0.5)
	qw1="#Error= "
	qw2=str(E)
	qw3="#Deltam= "
	qw4="#Deltab= "
	qw5=str(deltam)
	qw6=str(deltab)
	qw9="#r= "
	qw8=str(r)
	k.write(qw1+qw2)
	k.write("\n")
	k.write(qw3+qw5)
	k.write("\n")
	k.write(qw4+qw6)
	k.write("\n")
	k.write(qw9+qw8)
	k.write("\n")
	k.write("\n")
	xa=x[0]
	xb=x[len(x)-1]
	npuntos=100.0
	deltax=(xb-xa)/(npuntos-1.0)
	x_puntos=[xa]  #grilla para x
	y_puntos=[]    #grilla para y           
	for jk in range(0,int(npuntos)-1):
		xa+=deltax
		x_puntos.append(xa)
	for hj in range(0,int(npuntos)):
		l=lineal(x_puntos[hj],a1,a0)
		y_puntos.append(l)
	for i in range(0,len(x)):
		s=str(x[i])
		d=str(y[i])
		hjk=str(er[i])
		e=" "
		jl=s+e+d+e+hjk
		k.write(jl)
		k.write("\n")
	k.close()
	return ""

def minimo(x):     ####minimo de un vector
	minimo=x[0]
	if len(x)>1:
		for i in range(1,len(x)):
			if minimo>x[i]:
				minimo=x[i]
	return minimo
def maximo(x):     ####maximo de un vector
	maximo=x[0]
	if len(x)>1:
		for i in range(1,len(x)):
			if maximo<x[i]:
				maximo=x[i]
	return maximo
def ordenar(x):    ###ordenar una lista de numeros del vector x, cantidad de operaciones len(x)
        o=[]
        s=[]
        jk=len(x)
        for i in range(0,jk):
                af=minimo(x)
                o.append(af)
                x.remove(af)
        return o
def ordenar2(a,b):   ##### no es muy confiable porque no se conocen las cantidad de operaciones para ordenar por este metodo
        for k in range(0,len(a)):
                for j in range(0,len(a)-1):
                        if a[j]>a[j+1]:#cuando ordene los a, hara los mismos cambios a b                                
                                n=a[j]
                                a[j]=a[j+1]
                                a[j+1]=n
                                l=b[j]
                                b[j]=b[j+1]
                                b[j+1]=l
        return a,b
def ordenar3(a,b):   #### cantidad de operaciones maxima para ordenar el vector "a" es len(a)*(len(a)-1.0)/2.0
        kj=1.0
        while kj<=len(a)*(len(a)-1.0)/2.0:
                for j in range(0,len(a)-1):
                        if a[j]>a[j+1]:#cuando ordene los a, hara los mismos cambios al vector b                                
                                n=a[j]
                                a[j]=a[j+1]
                                a[j+1]=n
                                l=b[j]
                                b[j]=b[j+1]
                                b[j+1]=l
                                break
                kj+=1.0
        return a,b
def ordenar4(a,b,c):  #### cantidad de operaciones maxima para ordenar el vector "a" es len(a)*(len(a)-1.0)/2.0
	kj=1.0
	while kj<=len(a)*(len(a)-1.0)/2.0:
		for j in range(0,len(a)-1):
			if a[j]>a[j+1]:#cuando ordene los a, hara los mismos cambios al vector b y al vector c                               
				n=a[j]
				a[j]=a[j+1]
				a[j+1]=n
				l=b[j]
				b[j]=b[j+1]
				b[j+1]=l
				e=c[j]
				c[j]=c[j+1]
				c[j+1]=e
				break
		kj+=1.0
	return a,b,c
def determinante(M):   ### para evitar problemas como 3/2=1 escribir R(3,2) para cada division entre enteros
	for i in range(0,len(M)):
		for j in range(0,len(M[0])):
			if type(M[i][j])==int or type(M[i][j])==float:
				M[i][j]=R(M[i][j],1)
	L=crear_matriz(len(M),len(M[0]))
	def renovar(M,G):    ## renovar G a partir de M es decir que son iguales esto se hace porque al usar cambio(G,b,i) la matriz G cambia
		for i in range(0,len(M)):
			for j in range(0,len(M[0])):
				G[i][j]=M[i][j]
		return G
	D=renovar(M,L)
	def cambiar(M,n): #si el elemento de la diagonal de la matriz es cero, esta definicion cambia esta fila con otra para que el elemento M[n][n] deje de ser cero
		if M[n][n]==0:
			for i in range(n+1,len(M)):
				if M[i][n]!=0:
					fd=M[n]
					M[n]=M[i]
					M[i]=fd
					break
		return M
	lj=1
	try:
		ladb=1 ## Luis Dueñas 
		for o in range(0,len(M)-1): #reduciendo a cero los elementos por debajo de la diagonal de la matriz M
			if M[o][o]==0.0:
				cambiar(M,o)
				ladb*=-1
			for i in range(lj,len(M)):
				k=M[i][o]
				for j in range(0,len(M[0])):
					if type(M[o][j]*k/M[o][o])!=add.Add and exp and mul.Mul and sin and cos and tan and cot and sec and csc and cot and asin and acos and atan and acot and asec and acsc and acot and 0.0 and sinh and cosh and tanh and coth and sech and csch and coth and asinh and acosh and atanh and acoth and asech and acshc and acoth and numbers.NaN and Pow:
						M[i][j]=M[i][j]-R(M[o][j]*k,M[o][o])
					else:
						M[i][j]=M[i][j]-M[o][j]*k/M[o][o]	
			lj+=1
		det=1
		for i in range(0,len(M)):
			det*=M[i][i]
		det*=ladb
		if type(det)==numbers.NaN:
			det=0
	except ZeroDivisionError:
		det=0
	renovar(D,M)
	return (det)
def cramer(M): #### Regla de cramer para solucionar sistemas de ecuaciones lineales con determinante distinto de cero
	for i in range(0,len(M)):
		for j in range(0,len(M[0])):
			if type(M[i][j])==int or type(M[i][j])==float:
				M[i][j]=R(M[i][j],1)
	def crear_matriz(i,j):  #i numero de filas, j numero de columnas
		A=[0]*int(i)
		for k in range(0,len(A)):
			A[k]=[0]*int(j)
		return A
	def cambio(M,b,j):  ##Esta definicion reemplaza la columna j-esima, empezando desde cero la numeracion, de la matriz M por el vector columna b
		for i in range(0,len(M)):
			M[i][j]=b[i]
		return M
	x=[]
	b=[]
	G=crear_matriz(len(M),len(M[0]))
	L=crear_matriz(len(M),len(M[0]))
	def renovar(M,G):    ## renovar G a partir de M es decir que son iguales esto se hace porque al usar cambio(G,b,i) la matriz G cambia
		for i in range(0,len(M)):
			for j in range(0,len(M[0])):
				G[i][j]=M[i][j]
		return G
	D=renovar(M,L)
	wl1=determinante(M)
	renovar(M,G)
	for i in range(0,len(M)):
		b.append(M[i][len(M)])
	for i in range(0,len(G)):
		s=(determinante(cambio(G,b,i))/wl1)
		x.append(s)
		renovar(M,G)
	wl2=determinante(M)
	for i in range(0,len(x)):
		if type(x[i])!=add.Add and exp and mul.Mul and sin and cos and tan and cot and sec and csc and cot and asin and acos and atan and acot and asec and acsc and acot and 0.0 and sinh and cosh and tanh and coth and sech and csch and coth and asinh and acosh and atanh and acoth and asech and acshc and acoth and Pow:
			x[i]=cancel(R(determinante(cambio(G,b,i)),wl2))
			renovar(M,G)	
	renovar(D,M)
	return x
def equal(M,G): ### Dada la matriz M igualar G a M, es decir que ambas son M, esto se hace para que al modificar M no se altere la matriz G 
	for i in range(0,len(M)):
		for j in range(0,len(M[0])):
			G[i][j]=M[i][j]
	return G
def equalv(A,B): ### Dado el vector A igualar B a A
	for i in range(0,len(B)):
		B[i]=A[i]
	return A
def c_r(M):   ##### convertir cada elemento de la matriz M en un racional
	for i in range(0,len(M)):
		for j in range(0,len(M[0])):
			if type(M[i][j])==int or type(M[i][j])==float:
				M[i][j]=R(M[i][j],1)
	return M
def comprobar(M,S):   ### comprobar las que las soluciones S de la matriz M son validas
	print 
	f=[]
	for i in range(0,len(M)):
		d=0	
		for j in range(0,len(M[0])-1):
			d+=M[i][j]*S[j]
		f.append(simplify(d))
	l=[]
	for i in range(0,len(f)):
		if M[i][len(M[i])-1]==f[i]:
			l.append(i)	
	if len(l)==len(S):
		print("El vector solucion es correcto.")
	else:
		print("El vector solucion no es correcto.")
	return ""
def transpuesta(G):
	M=[]
	for i in range(0,len(G[0])):
		b=[]
		for j in range(0,len(G)):
			b.append(G[j][i])
		M.append(b)
	return M
def remover(M,h,k): ### remover la fila h-esima y la columna k-esima de la matriz M empezando a enumerar desde cero
	G=[]
	for i in range(0,len(M)):
		b=[]
		for j in range(0,len(M[0])):
			if i!=h and j!=k:
			        b.append(M[i][j])
		G.append(b)
	G.remove(G[h])
	return G
def removerf(M,h): #### remover la fila h-esima de la matriz M empezando la numeracion desde cero
        G=[]
        for i in range(0,len(M)):
                b=[]
                for j in range(0,len(M[0])):
                        if i!=h:
                                b.append(M[i][j])
                G.append(b)
        G.remove(G[h])
        return G
def removerc(M,k): ##remover la columna k-esima de la matriz M empezando la numeracion desde cero
        G=[]
        for i in range(0,len(M)):
                b=[]
                for j in range(0,len(M[0])):
                        if j!=k:
                                b.append(M[i][j])
                G.append(b)
        return G	
def inversa(M):
	if determinante(M)!=0:
		if len(M[0])==len(M):
			G=crear_matriz(len(M),len(M[0]))
			det=determinante(M)
			for i in range(0,len(G)):
				for j in range(0,len(G[0])):
					if type(((-1)**(i+j))*determinante(remover(M,i,j))/det)!=add.Add and exp and mul.Mul and sin and cos and tan and cot and sec and csc and cot and asin and acos and atan and acot and asec and acsc and acot and 0.0 and sinh and cosh and tanh and coth and sech and csch and coth and asinh and acosh and atanh and acoth and asech and acshc and acoth and Pow:
						G[i][j]=((-1)**(i+j))*R(determinante(remover(M,i,j)),det)                  
					else:			
		                		G[i][j]=((-1)**(i+j))*determinante(remover(M,i,j))/det            
			L=transpuesta(G)
		else:
			G=crear_matriz(len(M),len(M[0])-1)
			det=determinante(M)
			for i in range(0,len(G)):
				for j in range(0,len(G[0])):
					if type(((-1)**(i+j))*determinante(remover(removerc(M,len(M[0])-1),i,j))/det)!=add.Add and Pow and exp and mul.Mul and sin and cos and tan and cot and sec and csc and cot and asin and acos and atan and acot and asec and acsc and acot and 0.0 and sinh and cosh and tanh and coth and sech and csch and coth and asinh and acosh and atanh and acoth and asech and acshc and acoth:
						G[i][j]=((-1)**(i+j))*R(determinante(remover(removerc(M,len(M[0])-1),i,j)),det)
					else:
						G[i][j]=((-1)**(i+j))*determinante(remover(removerc(M,len(M[0])-1),i,j))/det
			L=transpuesta(G)		
	else:
		print("La matriz es singular, por lo tanto no tiene inversa.")
		L=M
	return L
def simplificarm(M):  ## simplificar cada componente de la matriz M
	for i in range(0,len(M)):
	        for j in range(len(M[0])):
	                M[i][j]=simplify(M[i][j])
	return M
def i_n(f,xa,xb,t,k): ###### integral numerica por simpson con n intervalos pares, t el numero de decimales exactos y k el maximo de la funcion en valor absoluto en el intervalo xa,xb
	x=Symbol("x")
	funcion=f
	def num_int(e,a,b,k): #### e error de la integral, xa=a y xb=b, k maximo de la funcion en valor absoluto
	    n=(k*((b-a)**5)/(180.0*e))**(1.0/4.0)
	    if int(n)%2==0 and int(n)!=n:
	        n+=2
	    else:
	        n+=1
	    n=int(n)
	    return n
	e=10**(-t-1)
	n=num_int(e,xa,xb,k)
	xa=float(xa)
	xb=float(xb)
	dx=(xb-xa)/float(n)
	xdf=crear_vector(xa,xb,n+1)
	s=funcion.subs(x,xdf[0])+funcion.subs(x,xdf[len(xdf)-1])
	for i in range(1,len(xdf)-1):
	    if i%2==0:
	        s+=2.0*funcion.subs(x,xdf[i])
	    else:
	        s+=4.0*funcion.subs(x,xdf[i])
	s*=dx/3.0
	return s
def newton(f,x0,n): ###### raices de la funcion f por newton-raphson con x0 el punto inicial y n el numero de decimales exactos
	g=diff(f,x)	
	j=0
	tol=10**(-n-1)
	while j<100:
		k=float(x0)
		if g.subs(x,k)==0:
			print("El metodo falla tras",j+1,"iteraciones, redefina el punto inicial.")
			break
		x0=k-(f.subs(x,k)/g.subs(x,k))
		j+=1
		if abs(x0-k)<tol:
			r=x0.evalf()			
			break
	return float(r)
def laplaciano(f,h1,h2,h3,u1,u2,u3):  ## laplaciano en coordenadas generalizadas
	h=h1*h2*h3
	s=((1/h)*diff(h/(h1**2)*diff(f,u1),u1)+(1/h)*diff(h/(h2**2)*diff(f,u2),u2)+(1/h)*diff(h/(h3**2)*diff(f,u3),u3))
	return s
def divergencia(f,h1,h2,h3,u1,u2,u3): ## divergencia en coordenadas generalizadas
	h=h1*h2*h3
	s=(1/h)*(diff((h/h1)*f),u1)+(1/h)*(diff((h/h2)*f),u2)+(1/h)*(diff((h/h3)*f),u3)	
	return s
def rotacional(B,h1,h2,h3,u1,u2,u3): ## rotacional en coordenadas generalizadas
	h=h1*h2*h3
	u=[h1*(diff(B[2]*h3,u2)-diff(B[1]*h2,u3)),-h2*(diff(h3*B[2],u1)-diff(h1*B[0],u3)),h3*(diff(h2*B[1],u1)-diff(h1*B[0],u2))]
	return u
def modulo_vector(A):  ## magnitud de un vector
	s=0
	for i in range(0,len(A)):
		s+=A[i]**2
	return sqrt(s)	
def producto_punto(A,B): ## producto punto
	s=0
	for i in range(0,len(A)):
		s+=A[i]*B[i]
	return s
def angulo_vector(A,B): ### angulo entre dos vectores, resultado en grados
	d=producto_punto(A,B)
	mA=modulo_vector(A)
	mB=modulo_vector(B)
	g=mA*mB
	return (acos(float(d)/g)*180.0/pi).evalf()
def producto_cruz(A,B): ### producto cruz entre dos vectores
	u=[A[1]*B[2]-B[1]*A[2],-(A[0]*B[2]-A[2]*B[0]),A[0]*B[1]-B[0]*A[1]]
	return u
def campo_vectorial(fx,fy,fz,n1,n2,n3,xa,xb,ya,yb,za,zb): #### campo vectorial grafica
	xx=crear_vector(xa,xb,int(n1))
	yy=crear_vector(ya,yb,int(n2))
	zz=crear_vector(za,zb,int(n3))
	x1=[]
	y1=[]
	z1=[]
	x2=[]
	y2=[]
	z2=[]
	for i in range(0,len(xx)):
		for j in range(0,len(yy)):
			for k in range(0,len(zz)):
				x1.append(xx[i])
				y1.append(yy[j])
				z1.append(zz[k])
				x2.append(fx.evalf(subs={x:xx[i],y:yy[j],z:zz[k]}))
				y2.append(fy.evalf(subs={x:xx[i],y:yy[j],z:zz[k]}))	
				z2.append(fz.evalf(subs={x:xx[i],y:yy[j],z:zz[k]}))
	print(crear6(x1,y1,z1,x2,y2,z2))
	print("splot 'campo.dat' u 1:2:3:4:5:6 with vectors head size 0.5,20,50 filled lt 3")
	return ""
def simplificarv(A): ##simplificar las componentes del vector A
	for i in range(0,len(A)):
		A[i]=simplify(A[i])
	return A
def substituir(f,U): ### substituir las componentes del vector u en la funcion f, con f(u1,u2,...,un) y u=[f1,f2,...,fn] con fn(u1,u2,...,un), y la funcion f debe estar en terminos de u1,u2,un y cada elemento del vector U debe ser los que se quiere substituir en f, es decir u1 a U[0] u2 a U[1] etc, deben estar emparejados. 
	for i in range(0,len(U)):
		k=str(i+1)
		p="u"
		n=Symbol(p+k)
		f=f.subs(n,U[i])
	return f
def verticaln1(t,M,i): ####### mostrar en columna el vector t con la columna i de la matriz M
	for j in range(0,len(M)):
		print(t[j],M[j][i])	
	return ""
def verticaln2(t,M): ### mostrar el vector t con las primeras dos columnas de la matriz M
        for j in range(0,len(M)):
                print(t[j],M[j][0],M[j][1])
        return ""
def verticaln3(t,M): ### mostrar el vector t con las primeras tres columnas de la matriz M
        for j in range(0,len(M)):
                print(t[j],M[j][0],M[j][1],M[j][2])
        return ""
def verticaln4(t,M): ### mostrar el vector t con las primeras tres columnas de la matriz M
        for j in range(0,len(M)):
                print(t[j],M[j][0],M[j][1],M[j][2],M[j][3])
        return ""
def definirn(U): ##### definir len(U) funciones del vector U
	a="u1,"
	for j in range(1,len(U)):
		a+="u"+str(j+1)+","
	a+="u"+str(len(U)+1)
	for i in range(0,len(U)):
		print("def funcion"+str(i+1)+"("+a+"):")
		print("        f="+str(U[i]))
		print("        return f")
	return ""	
def Runge_kutta_sm(U,w,xa,xb,de,h): #### Codigo del metodo Runge Kutta Felhberg para solucionar sistemas de ecuaciones diferenciales ordinarias numericamente con U el vector de funciones igualadas du2(t)/dt,du3(t)/dt,...,dun(t)/dt y el vector w con las condiciones iniciales w2(xa),w3(xa),...,wn(xa) en el intervalo xa,xb con "de" la cantidad de decimales exactos, donde la matriz es mostrada verticalmente donde de izquierda a derecha en forma vertical se muestra las soluciones u1,u2(t),...,un(t), con u1 el tiempo, siempre ubicar u1 como la variable temporal y h el deltax, advertencia: poner las derivadas en orden en el vector U, es decir que las derivadas queden en orden creciente, al ubicarlas en el vector U.  
	m=len(U) ###numero de ecuaciones
	def definirn1(U):
		a="u1,"
		for j in range(1,len(U)):
			a+="u"+str(j+1)+","
		a+="u"+str(len(U)+1)
		for i in range(0,len(U)):
			print("        def funcion"+str(i+1)+"("+a+"):")
			print("                f="+str(U[i]))
			print("                return f")
		return ""
	print("from definiciones import crear_vector,crear_matriz,vertical2,minimo,Runge_kutta_sm,equalv")
	print("from math import *")
	print("xa="+str(xa))
	print( "xb="+str(xb))
	print("de="+str(de))
	print("h="+str(h))
	print("w="+str(w))
	print("def Runge_kutta_s2(w,xa,xb,de,h):")
	print("        m="+str(m))
	print("        xa=float(xa)")
	print("        xb=float(xb)")
	print("        npuntos=int(ceil((xb-xa)/h+1.0))")
	print("        vector_t=crear_vector(xa,xb,npuntos)")
	print("        h=vector_t[1]-vector_t[0]")
	print("        W1=crear_matriz(len(vector_t),m)")
	print("        w1=[]")
	print("        w2=[]")
	print("        w9=[]")
	print("        h_new=[]")
	print("        error=10**(-de-1)")
	print("        for i in range(0,len(w)):")
	print("                w1.append(float(w[i]))")
	print("                w2.append(float(w[i]))")
	print("                w9.append(float(w[i]))")
	print("                W1[0][i]=float(w[i])")
	print(definirn1(U))
	print('        for i in range(1,len(vector_t)):')
	######### k1
	a="		"
	b="vector_t[i-1],"
	for j in range(1,int(m)):
		b+="w1["+str(j-1)+"]"+","
	b+="w1["+str(m-1)+"]"
	for i in range(0,int(m)):
		y1=a+"k1"+str(i+1)+"="+"h*funcion"+str(i+1)+"("+b+")"
		print(y1)
	######### k2
	c="		"
	d="vector_t[i-1]+(h/4.0),"
	for j in range(1,int(m)):
		d+="w1["+str(j-1)+"]"+"+(1.0/4.0)*k1"+str(j)+","
	d+="w1["+str(m-1)+"]"+"+(1.0/4.0)*k1"+str(m)
	for i in range(0,int(m)):
		y2=c+"k2"+str(i+1)+"="+"h*funcion"+str(i+1)+"("+d+")"
		print(y2)
	######### k3
	e="		"
	f="vector_t[i-1]+(3.0*h/8.0),"
	for j in range(1,int(m)):
		f+="w1["+str(j-1)+"]"+"+(3.0/32.0)*k1"+str(j)+"+(9.0/32.0)*k2"+str(j)+","
	f+="w1["+str(m-1)+"]"+"+(3.0/32.0)*k1"+str(m)+"+(9.0/32.0)*k2"+str(m)
	for i in range(0,int(m)):
		y3=e+"k3"+str(i+1)+"="+"h*funcion"+str(i+1)+"("+f+")"
		print(y3)
	######## k4
	g="		"
	h="vector_t[i-1]+(12.0*h/13.0),"
	for j in range(1,int(m)):
		h+="w1["+str(j-1)+"]"+"+(1932.0/2197.0)*k1"+str(j)+"-(7200.0/2197.0)*k2"+str(j)+"+(7296.0/2197.0)*k3"+str(j)+","
	h+="w1["+str(m-1)+"]"+"+(1932.0/2197.0)*k1"+str(m)+"-(7200.0/2197.0)*k2"+str(m)+"+(7296.0/2197.0)*k3"+str(m)
	for i in range(0,int(m)):
		y4=g+"k4"+str(i+1)+"="+"h*funcion"+str(i+1)+"("+h+")"
		print(y4)
	####### k5
	k="		"
	l="vector_t[i-1]+h,"
	for j in range(1,int(m)):
		l+="w1["+str(j-1)+"]"+"+(439.0/216.0)*k1"+str(j)+"-8.0*k2"+str(j)+"+(3680.0/513.0)*k3"+str(j)+"-(845.0/4104.0)*k4"+str(j)+","
	l+="w1["+str(m-1)+"]"+"+(439.0/216.0)*k1"+str(m)+"-8.0*k2"+str(m)+"+(3680.0/513.0)*k3"+str(m)+"-(845.0/4104.0)*k4"+str(m)
	for i in range(0,int(m)):
		y5=k+"k5"+str(i+1)+"="+"h*funcion"+str(i+1)+"("+l+")"
		print(y5)
	####### k6
	q="		"
	w="vector_t[i-1]+(h/2.0),"
	for j in range(1,int(m)):
		w+="w1["+str(j-1)+"]"+"-(8.0/27.0)*k1"+str(j)+"+2.0*k2"+str(j)+"-(3544.0/2565.0)*k3"+str(j)+"+(1859.0/4104.0)*k4"+str(j)+"-(11.0/40.0)*k5"+str(j)+","
	w+="w1["+str(m-1)+"]"+"-(8.0/27.0)*k1"+str(m)+"+2.0*k2"+str(m)+"-(3544.0/2565.0)*k3"+str(m)+"+(1859.0/4104.0)*k4"+str(m)+"-(11.0/40.0)*k5"+str(m)
	for i in range(0,int(m)):
		y6=k+"k6"+str(i+1)+"="+"h*funcion"+str(i+1)+"("+w+")"
		print(y6)
	####### w
	for j in range(0,int(m)):
		y7="		w1["+str(j)+"]"+"="+"w1["+str(j)+"]"+"+(25.0/216.0)*k1"+str(j+1)+"+(1408.0/2565.0)*k3"+str(j+1)+"+(2197.0/4104.0)*k4"+str(j+1)+"-(1.0/5.0)*k5"+str(j+1)	
		print(y7)
		print("		W1[i]["+str(j)+"]"+"="+"w1["+str(j)+"]")
	for j in range(0,int(m)):
		y8="		w2["+str(j)+"]"+"="+"w2["+str(j)+"]"+"+(16.0/135.0)*k1"+str(j+1)+"+(6656.0/12825.0)*k3"+str(j+1)+"+(28561.0/56430.0)*k4"+str(j+1)+"-(9.0/50.0)*k5"+str(j+1)+"+(2.0/55.0)*k6"+str(j+1)
		print(y8)
		print("                if abs("+"w1["+str(j)+"]-"+"w2["+str(j)+"])!=0.0:")
		print("                        lo=(0.5*(h**5)*error/abs("+"w1["+str(j)+"]-"+"w2["+str(j)+"]"+"))**(1.0/4.0)")
		print("                        h_new.append(lo)")
	print("        equalv(w9,w)")
	print('        hkl=""')
	print("        for i in range(0,m+1):")
	print("                d=str(i+1)")
	print('                g="u"')
	print('                ghj=" "')
	print("                hkl+=g+d+ghj")
	print("        print hkl")
	print('        h=vector_t[1]-vector_t[0]')
	print('        if len(h_new)==0:')
	print("                h_new.append(h)")
	print("        return vector_t,W1,h,minimo(h_new)")
	print("F=Runge_kutta_s2(w,xa,xb,de,h)")
	print("vt=F[0]")
	print("H=F[1]")
	print("hn=F[2]")
	print("hmin=F[3]")
	print("print vertical2(vt,H)")
	print("print 'h=',hn")
	print("print 'hmin=',hmin")
	return ""
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
        v2=modulo_vector(v)**2
        f=multiplicarc(producto_punto(u,v)/v2,v)
        return f
def rotar(r,p,theta): ###rotar un angulo theta el vector r a lo largo de la recta p, en sentido antihorario si theta es positivo, con theta en radianes
        P=proyeccion(r,p)
        rmp=restav(r,P)
        rcp=producto_cruz(r,p)
        s1=sumav(P,multiplicarc(cos(theta),rmp))
        s2=multiplicarc(-sin(theta)/modulo_vector(p),rcp)
        return simplificarv(sumav(s1,s2))
def substituirm(M,c1,c2):  ### substituir la variable c1 de cada componente de la matriz M con c2
	C=crear_matriz(len(M),len(M[0]))
	for i in range(0,len(M)):
		for j in range(0,len(M[0])):
			if type(M[i][j])!=int and float:	
				C[i][j]=(M[i][j]).subs(c1,c2)
			else:
				C[i][j]=M[i][j]
	return C
def derivarm(M,c): ### derivar las componentes de la matriz M con respecto a c
        C=crear_matriz(len(M),len(M[0]))
        for i in range(0,len(M)):
                for j in range(0,len(M[0])):
        	        C[i][j]=diff(M[i][j],c)
        return C
def derivarv(A,c):  ### derivar las componentes del vector A con respecto a c
	B=[]
	for i in range(0,len(A)):
		B.append(diff(A[i],c))
	return B
def substituir_t(T,k):  #### substituir en la energia cinetica T(u1,u2,u3,..,un) las variables u2,u3,..,un por u2(u1),u3(u1),..,un(u1) con k=n el numero de variables incluyendo a u1.
        Tn=T
        for i in range(0,int(k)-1):
                w="u"+str(i+2)
                q=Symbol(w)
                Tn=Tn.subs(q,q(u1))

        return Tn
def rsubstituir_t(T,k): #### cambiar en la energia cinetica T(u1,u2(u1),u3(u1),..,un(u1)) por T(u1,u2,u3,..,un), con k=n el numero de variables incluyendo a u1.
        Tn=T
        for i in range(0,int(k)-1):
                w="u"+str(i+2)
                q=Symbol(w)
                Tn=Tn.subs(q(u1),q)

        return Tn
def interpolador_lagrange(xa,xb,xpuntos,ypuntos,ngrilla):  ### interpoladores de lagrange para los puntos xpuntos,ypuntos en el intervalo xa,xb con ngrilla la cantidad de puntos del polinomio interpolador
        def l_enesimo(x,t,k):  ## x=xpuntos,t variable independiente, k es el l-esimo termino
                l=1.0
                for i in range(0,len(xpuntos)):
                        if i!=k:
                                l*=(t-x[i])/(x[k]-x[i])
                return l
        def pol(x,y):  ##x el vector de puntos de x, y y la variable independiente
                p=0.0
                for i in range(0,len(x)):
                        p+=ypuntos[i]*l_enesimo(x,y,i) #p es el polinomio, y como el grado del polinomio es el numero de datos menos uno, y como i no toma len(x)
                return p
        xa1=xa
        deltax1=(xb-xa1)/(ngrilla-1.0)
        xpol=[xa1]
        ypol=[pol(xpuntos,xa1)]
        for i in range(0,int(ngrilla)-1):
                xa1+=deltax1
                xpol.append(xa1)
                ypol.append(pol(xpuntos,xa1))
        return xpol,ypol
def aproximacion_polinomios(x,y,grado): ### aproximacion de un conjunto de puntos por polinomios con x,y los puntos datos y 'grado' el grado del polinomio a calcular
	M=[0.0]*(int(grado)+1)     #creando la matriz M 
	for i in range(0,len(M)):
		M[i]=[0.0]*(int(grado)+2)
	for j in range(0,len(M)):   #los elementos de la matriz M sin incluir la ultima columna son M[j][k]=sumatoria(x**(j+k)) 
		for k in range(0,len(M[0])-1):
			lk=0.0
			for jl in range(0,len(x)):
				lk+=x[jl]**(j+k)
			M[j][k]=lk
	for i in range(0,int(grado)+1):  #los elementos de la matriz M donde solo modifica a la ultima columna son M[i][h]=sumatoria((x**i)*y)
		fyh=0.0
		for h in range(0,len(x)):
			fyh+=(x[h]**i)*y[h]
		M[i][len(M[0])-1]=fyh
	def solucionl(M,x,y): #muestra las soluciones de la matriz M por gaussjordan

		n=0
		while n<=(len(M)-1):  #reduciendo a cero los elementos diferentes la diagonal de la matriz M
			cambiar(M,n)
			for i in range(0,len(M)):
				gfj=M[i][n]
				for j in range(0,len(M[0])):
					if gfj!=0 and i!=n and M[n][n]!=0:
						M[i][j]=((M[i][j]*M[n][n])/gfj)-M[n][j]
			n+=1
		I=[]  #vector con elementos iguales al numero de la fila de la matriz dependiendo del caso
		xs=[] #vector con elementos iguales a las constantes del polinomio
		try:
			print("Las constantes del polinomio de grado",int(grado),"en orden ascendente","son:")
			print()
			for hj in range(0,len(M)):  #encontrando las soluciones de la matriz M 
				fgk=M[hj][len(M)]/M[hj][hj]
				hg="="
				if M[len(M)-1][len(M)-1]!=0:
					print("a"+str(hj)+hg,fgk)
					xs.append(fgk)
			def polinomial(x,t):    # esta definicion sirve para encontrar P(t), donde P es el polinomio encontrado, y x son las constantes del polinomio
				gj=x[0]
				for i in range(1,len(x)):
					gj+=x[i]*((t)**i)
				return gj
			xa=x[0]
			xb=x[len(x)-1]
			npuntos=100.0  #cantidad de puntos para la grilla x
			deltax=(xb-xa)/(npuntos-1.0)
			xgrilla=[xa]
			ygrilla=[]
			for bk in range(0,int(npuntos)-1):  #creando el vector de puntos de la grilla x
				xa+=deltax
				xgrilla.append(xa)
			for hj in range(0,int(npuntos)):  #creando el vector de puntos para la grilla y 
				l=polinomial(xs,xgrilla[hj])
				ygrilla.append(l)
			print()
			E=0.0
			for i in range(0,len(y)):  #encontrando el error
				E+=(y[i]-polinomial(xs,x[i]))**2.0   #error=sumatoria((yi-(P(xi)))**2.0), donde P es el polinomio encontrado  
			print("Error=",E)
			pyplot.plot(x,y,"*",xgrilla,ygrilla) #graficando los puntos y el polinomio
			pyplot.show()
		except ZeroDivisionError:
			for i in range(0,len(M)):
				for j in range(0,len(M[0])):
					if M[i][j]==0:
						I.append(i)
			k=True
			for i in range(I[0],len(I)):
				if I.count(i)==(len(M[0])-1):
					k=False
					break
			if k==True:
				print("El sistema de ecuaciones tiene infinitas soluciones")
			else:
				print("El sistema de ecuaciones no tiene solucion")
		return ""
	solucionl(M,x,y)
	return ""
def spline_cubic(x,y,npuntos,ngrilla): ### splines cubics en el intervalo xa,xb con una grilla de npuntos=len(x), npuntos es la dada, y ngrilla la cantidad de puntos que toma cada polinomio s k-esimopara cada par de puntos.
        def hj(x):   ## definicion que encuentra los hj=(x[i+1]-x[i])
                k=[]
                for i in range(0,int(npuntos)-1):
                        z=x[i+1]-x[i]
                        k.append(z)
                return k
        h=hj(x)  #vector hj
        A=[0.0]*(int(npuntos))   ## matriz A con el sistema de ecuaciones lineales que encuentran los cj
        for i in range(0,len(A)):
                A[i]=[0.0]*(int(npuntos)+1)
        A[0][0]=1.0        #primer elemento de la diagonal de la matriz A igual a 1 
        A[len(A)-1][len(A)-1]=1.0   #ultimo elemento de la diagonal de la matriz A igual a 1
        for i in range(0,len(A)):
                if i!=0 and i!=len(A)-1:
                        A[i][i]=2.0*(h[i-1]+h[i])   #reemplazando los elementos de la diagonal de la matriz A sin alterar el primero y el ultimo de esta diagonal
        for i in range(1,len(A)):       #reemplando los elementos que estan una posicion atras de cada elemento de la diagonal 
                if i!=len(A)-1:
                        A[i][i-1]=h[i-1]
        for i in range(1,len(A)-1):   #reemplazando los elementos que estan una posicion delante de cada elemento de la diagonal
                A[i][i+1]=h[i]
        for i in range(1,len(A)-1):
                        A[i][len(A[0])-1]=3.0*(((y[i+1]-y[i])/h[i])-((y[i]-y[i-1])/(h[i-1])))   #reemplazondo la ultima columna de la matriz A sin alterar el primer y ultimo elemento de esta colummna
        c=solucion(A)  ## vector con los cj
        d=[]          ## vector con los dj
        for i in range(0,int(npuntos)-1):  ## hallando los dj
                dj=(c[i+1]-c[i])/(3.0*h[i])
                d.append(dj)
        b=[]      ##vector con los bj
        for i in range(0,int(npuntos)-1):  ## vector con los bj
                bj=((y[i+1]-y[i])/h[i])-((2.0*c[i]+c[i+1])*h[i]/3.0)
                b.append(bj)
        def spline(y,b,c,d,k,x,t):  ## definicion que encuentra el polinomio s k-esimo, con variable independiente t
                ss=0.0
                ss+=y[k]+b[k]*(t-x[k])+c[k]*((t-x[k])**2.0)+d[k]*((t-x[k])**3.0)
                return ss
        xgrilla=[]   #vector x del polinomio s k-esimo
        ygrilla=[]   #vector y del polinomio s k-esimo
        for k in range(0,len(x)-1): ## hallando los valor de los "x" y "y" del polinomio s k-esimo
                deltasplin=abs((x[k+1]-x[k])/(ngrilla-1.0))
                z=x[k]
                y1=spline(y,b,c,d,k,x,z)
                xgrilla.append(z)
                ygrilla.append(y1)
                for i in range(0,int(ngrilla)-1):
                        z+=deltasplin
                        xgrilla.append(z)
                        y1=spline(y,b,c,d,k,x,z)
                        ygrilla.append(y1)
        return xgrilla,ygrilla
def W(f1,f2,a,b):
	return (f1.subs(xi,a))*((diff(f2)).subs(xi,b))-(f2.subs(xi,b))*((diff(f1)).subs(xi,a))
### funcion s
def sgn(x): # funcion signo
	s=0
	if x>0:
		s=1			
	if x<0:
		s=-1
	return s	
def s(x): #x es un vector de enteros
	i=0
	k=len(x)
	s=1
	while i<k-1:
		for j in range(i+1,k):
			s*=sgn(x[j]-x[i])
			if s==0:
				i=k
				break
		i=i+1
	return s
def ccv(a): ### convertit una cadena de numeros a vector donde todos los numeros estan separados por espacios   
        x=[]
        a=a.strip()
        b=""
        for i in a:
                try:
                        b+=i
                        if str(i)!="." and str(i)!="-":
                                int(i)
                except ValueError:
                        try:
                                x.append(float(b))
                                b=""
                        except ValueError:
                                b=""
        x.append(float(b))
        return x
def matrixfile(arc): ###  pasar los datos de arc (un archivo donde estan los datos en colummnas) un una matrix donde las lineas son las filas de la matrix M
        file=open(arc,"r+")
        lines=file.readlines()
        M=[]
        for ii in lines:
                try:
                        M.append(ccv(ii))
                except ValueError:
                        pass

        file.close()
        return M
def table_latex(M,titulo,enc):  ### convertir la matrix M en una tabla escrita en codigo latex, enc es un vector de los nombres de cada columna, m es la matriz de datos y titulo es el nombre de la tabla
        print()
        print("\\begin{table}[H]")
        print("\caption{"+titulo+"}")
        print("\centering")
        print("\\begin{tabular}{"+"|c"*len(M[0])+"|}")
        print("\hline")
        e=""
        for ii in range(len(enc)-1):
                e+=enc[ii]+" & "
        e+=enc[len(enc)-1]+" \\\\"
        print(e)
        print("\hline")
        for kk in range(len(M)):
                q=""
                for ll in range(len(M[0])-1):
                        q+=str(M[kk][ll])+" & "
                q+=str(M[kk][len(M[0])-1])+" \\\\"
                print(q)
                print("\hline")
        print("\end{tabular}")
        print("\end{table}")
        return ""
#xi=Symbol("xi")
#a,b,f1,f2,p=symbols("a b f1 f2 p")
#a=0
#b=pi
#f1=exp(-xi)
#f2=exp(-2*xi)
#p=exp(3*xi)
#g=p*cos(2*xi)
#det=W(f1(xi),f2(xi),xi,xi)*(W(f1(xi),f2(xi),a,b)+W(f1(xi),f2(xi),b,a)-W(f1(xi),f2(xi),a,a)-W(f1(xi),f2(xi),b,b))
#pdet=p(xi)*det
#A=(-1/pdet)*(f2(xi)*(W(f1(xi),f2(xi),b,b)-W(f1(xi),f2(xi),b,a))-f1(xi)*W(f2(xi),f2(xi),a,b))
#B=(1/pdet)*(f1(xi)*(W(f1(xi),f2(xi),b,b)+W(f2(xi),f1(xi),b,a))+f2(xi)*W(f1(xi),f1(xi),a,b))
#C=(-1/pdet)*(-f2(xi)*(W(f1(xi),f2(xi),a,a)+W(f2(xi),f1(xi),b,a))-f1(xi)*W(f2(xi),f2(xi),a,b))
#D=(1/pdet)*(-f1(xi)*(W(f1(xi),f2(xi),a,a)-W(f1(xi),f2(xi),b,a))+f2(xi)*W(f1(xi),f1(xi),a,b))
##########
#N1=[f1.subs(xi,a),f2.subs(xi,a),-f1.subs(xi,b),-f2.subs(xi,b),0]
#N2=[diff(f1).subs(xi,a),diff(f2).subs(xi,a),-diff(f1).subs(xi,b),-diff(f2).subs(xi,b),0]
#N3=[f1,f2,-f1,-f2,0]
#N4=[-diff(f1),-diff(f2),diff(f1),diff(f2),1/p]
#M=[N1,N2,N3,N4]
#S=cramer(M)
#det=W(f1,f2,xi,xi)*(W(f1,f2,a,b)+W(f1,f2,b,a)-W(f1,f2,a,a)-W(f1,f2,b,b))
#pdet=p*det
#A=(-1/pdet)*(f2*(W(f1,f2,b,b)-W(f1,f2,b,a))-f1*W(f2,f2,a,b))
#B=(1/pdet)*(f1*(W(f1,f2,b,b)+W(f2,f1,b,a))+f2*W(f1,f1,a,b))
#C=(-1/pdet)*(-f2*(W(f1,f2,a,a)+W(f2,f1,b,a))-f1*W(f2,f2,a,b))
#D=(1/pdet)*(-f1*(W(f1,f2,a,a)-W(f1,f2,b,a))+f2*W(f1,f1,a,b))
#pprint(simplify(integrate(C*f1.subs(xi,x)*g+D*f2.subs(xi,x)*g,(xi,0,x))+integrate(A*f1.subs(xi,x)*g+B*f2.subs(xi,x)*g,(xi,x,pi))))
