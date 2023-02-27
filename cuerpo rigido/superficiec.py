#k=49 ##### numero de veces  que se repite en el vector x de la grilla
#set title "datos"
#set xlabel "Eje x"
#set ylabel "Eje y"
#set zlabel "F(x,y)"
#unset key
#do for [i=0:1:1] {
#    splot 'mathieu.dat' every ::0::k w l lt 3, \
#          'mathieu.dat' every ::k+1::2*k+1 w l lt 3, \
#          'mathieu.dat' every ::2*k+2::3*k+2 w l lt 3, \
#          'mathieu.dat' every ::3*k+3::4*k+3 w l lt 3, \
#          'mathieu.dat' every ::4*k+4::5*k+4 w l lt 3
#}
n=5 ## numero de de veces  que se repite en el vector x de la grilla
def codigo(n,l,name,name2): ## n numero de veces que se repite en el vector x, name el nombre del archivo.dat y name2 el nombre del archivo2.dat
	k=n-1	
	h=l-1
	print "set xlabel 'Eje x'"
	print "set ylabel 'Eje y'"
	print "set zlabel 'F(x,y)'"
	print "unset key"
	print "k="+str(k)+" ##### n numero de datos en el vector x de la grilla"
	print "h="+str(h)+" ##### h numero de datos en el vector x de la grilla"
	print "do for [i=0:1:1] {"	
	print "    splot '"+str(name)+"' every ::0::k w l lt 3, \\"
	print "          '"+str(name2)+"' every ::0::h w l lt 3, \\"
	for i in range(1,int(k)):
		print "          '"+str(name)+"'"+" every ::"+str(i)+"*k"+"+"+str(i)+"::"+str(i+1)+"*k"+"+"+str(i)+" w l lt 3, \\"
	print "          '"+str(name)+"'"+" every ::"+str(k)+"*k"+"+"+str(k)+"::"+str(k+1)+"*k"+"+"+str(k)+" w l lt 3, \\"
	for j in range(1,int(h)):
                print "          '"+str(name2)+"'"+" every ::"+str(j)+"*h"+"+"+str(j)+"::"+str(j+1)+"*h"+"+"+str(j)+" w l lt 3, \\"
        print "          '"+str(name2)+"'"+" every ::"+str(h)+"*h"+"+"+str(h)+"::"+str(h+1)+"*h"+"+"+str(h)+" w l lt 3"
	print "}"
	return ""
print codigo(80,80,"mathieu.dat","mathieu2.dat")
