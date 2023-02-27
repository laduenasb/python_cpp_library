#include "cstdlib" // libreria que contiene atoi convertir cadenas a int o float
#include "iostream"
#include "string"
#include "math.h"
#include "sstream" // librearia para convertir int a string
#include "vector"
#include "cstdio"
using namespace std;
int contar(float xi,vector <float> x){ // cantidad de veces que esta xi en el vector x
	int c=0;
	for(int i=0;i<x.size();i++){
		if(xi==x.at(i)){
			c++;
		}
	}
	return c;
}	
bool pertenece(float xi,vector <float> x){ // saber si xi pertenece al vector x
	bool f=0;
	for(int i=0;i<x.size();i++){
		if(xi==x.at(i)){
			f=1;
			break;
		}
	}
	return f;
}
void ordenar(vector <float> *a,vector <float> *b){ // cantidad de operaciones maxima para ordenar el vector "a" es len(a)*(len(a)-1.0)/2.0
	int kj=1;
	while(kj<=(*a).size()*((*a).size()-1)/2){
		for(int j=0;j<(*a).size()-1;j++){
			if((*a).at(j)>(*a).at(j+1)){ // cuando ordene los a, hara los mismos cambios al vector b
				float n=(*a).at(j);
				(*a).at(j)=(*a).at(j+1);
				(*a).at(j+1)=n;
				float l=(*b).at(j);
				(*b).at(j)=(*b).at(j+1);
                                (*b).at(j+1)=l;
				break;	
			}
		}
		kj++;
	}
}
void archivo(vector <float> x,vector <float> y,string nombre){ //guarda los elementos de los vectores x,y al archivo nombre en columnas
	ofstream fyle;
	fyle.open (nombre.c_str());
	fyle<<"#"<<nombre<<endl;
	for(int i=0;i<x.size();i++){
		fyle<<x.at(i)<<" "<<y.at(i)<<endl;
	}
	fyle.close();
}
float ctf(string cl){ // funcion que convierte cadena a float
	return atof(cl.c_str());
}
int cti(string cl){ // funcion que convierte cadena a int
        return atof(cl.c_str());
}
string ftc(float cl){ // funcion que convierte float a cadena
	stringstream convert;
	convert<<cl;
	return convert.str();
}
string itc(int cl){ // funcion que convierte int a cadena
        stringstream convert;
        convert<<cl;
        return convert.str();
}
int suma(vector<float>x,int l){ // sume las primeras l componentes del vector x
	int s=0;
	for(int i=0;i<l;i++){
	       s+=x.at(i);
	}
	return s;
}
float elemento(vector<float>x,vector<float>col,int i,int j){  // fila i. columna j con x todos los elementos de la matriz con sus columnas seguidas y col la cantidad de elementos de cada fila, la notacion empieza desde cero
	return x.at(suma(col,i)+j);
}
void equal(vector<float>*x,vector<float>y){ // igualar el vector x con el vector y, SUGERENCIA: USAR PUNTEROS
	for(int i=0;i<y.size();i++){
		(*x).push_back(y.at(i));
		
	}
}
int main(){
vector<float>jl;
vector<float>fg;
for(int q=0;q<=10;q++){
	jl.push_back(q+1);
}
equal(&fg,jl);
cout<<fg.at(5)<<endl;
vector<string>hola;
for(int g=0;g<10;g++){
	hola.push_back(itc(g+1));
}
for(int j=0;j<hola.size();j++){
	cout<<hola.at(j)<<endl;
}
return 0;
}
