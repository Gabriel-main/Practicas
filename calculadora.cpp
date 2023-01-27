#include <iostream>
#include <string>

using namespace std;


int suma(int Numero1, int Numero2){
    return Numero1 + Numero2;
}
int resta(int Numero1, int Numero2){
    return Numero1 - Numero2;
}
int multiplicacion(int Numero1, int Numero2){
    return Numero1 * Numero2;
}
float division(float Numero1, float Numero2){
    return Numero1 / Numero2;
}


int main(){

    cout<<"CALCULADORA BASICA\n------------\n";
    
    float valor1, valor2;
    string operando;

    while(true){
        cin>>valor1;
        cin>>operando;
        cin>>valor2;

        cout<<""<<endl;

        if(operando == "+"){
            cout<<suma(valor1,valor2)<<endl;
        }
        else if(operando == "-"){
            cout<<resta(valor1,valor2)<<endl;
        }
        else if(operando == "x"){
            cout<<multiplicacion(valor1,valor2)<<endl;
        }
        else if(operando == "/"){
            cout<<division(valor1,valor2)<<endl;
        }
        else{
            cout<<"Error...\nEscoger bien el operando."<<endl;
            break;
        }
        cout<<""<<endl;
    }
    return 0;
}