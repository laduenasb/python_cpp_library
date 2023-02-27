###########factorizacion LU metodo 2
E1=[1.0,-1.0,2.0,-1.0,-8.0]
E2=[2.0,-2.0,3.0,-3.0,-20.0]
E3=[1.0,1.0,1.0,0.0,-2.0]
E4=[1.0,-1.0,4.0,3.0,4.0]
M=[E1,E2,E3,E4]
b=[-8.0,-20.0,-2.0,4.0]
L=[0.0]*len(M)
for asg in range(0,len(L)):
        L[asg]=[0.0]*len(M[0])
for dg in range(0,len(L)):
        L[dg][dg]=1.0
def cambiar(M,n):
        if M[n][n]==0:
                for i in range(n+1,len(M)):
                                if M[i][n]!=0:
                                        fd=M[n]
                                        M[n]=M[i]
                                        M[i]=fd
                                        break
        return M
def vertical(x):
        for i in range(0,len(x)-1):
                print x[i]
        return x[i+1]
def solucion(M):
        Y=[]
        for n in range(0,len(M)):
                cambiar(M,n)
                for i in range(0,len(M)):
                        gfj=M[i][n]
                        for j in range(0,len(M[0])):
                                if gfj!=0 and i!=n:
                                        M[i][j]=((M[i][j]*M[n][n])/gfj)-M[n][j]
        return M
print "A:"
print vertical(M)
print
print "b:"
print b
print
lj=1
for o in range(0,len(M)-1):
	if M[o][o]==0:
                for i in range(o+1,len(M)):
                                if M[i][o]!=0:
                                        fd=M[o]
                                        M[o]=M[i]
                                        M[i]=fd
					sdf=b[o]
					b[o]=b[i]
					b[i]=sdf
					if o!=0:
						for ghj in range(0,o):
							ljk=L[o][ghj]
							L[o][ghj]=L[i][ghj]
							L[i][ghj]=ljk	
                                        break
        for i in range(lj,len(M)):
                k=M[i][o]
		L[i][o]=M[i][o]/M[o][o]
                for j in range(0,len(M[0])):
                        M[i][j]=M[i][j]-(M[o][j]*k/M[o][o])
        lj+=1
print "U:"
print vertical(M)
print
print "L:"
print vertical(L)
print
for ksa in range(0,len(b)):
        L[ksa][len(M[0])-1]=b[ksa]
print vertical(L)
print
solucion(L)
Y=[]
for hj in range(0,len(L)):
        fgk=L[hj][len(L)]/L[hj][hj]
        Y.append(fgk)
print
for ksa in range(0,len(Y)):
        M[ksa][len(M[0])-1]=Y[ksa]
print vertical(M)
print
solucion(M)
x=[]
for hj in range(0,len(M)):
        fgk=M[hj][len(M)]/M[hj][hj]
        x.append(fgk)
print "Las soluciones al sistema de ecuaciones son:"
print 
print "x=",x
print 
