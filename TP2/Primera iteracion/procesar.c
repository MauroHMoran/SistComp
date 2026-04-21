#include <stdio.h>

// se recibe un float y devuelve un entero
int calcular_gini(float valor_gini) {
    
    // casteo
    int valor_entero = (int)valor_gini;
    
    // se suma 1
    int resultado = valor_entero + 1;
    
    return resultado;
}