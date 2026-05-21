#include <stdio.h>

//cabecera de funcion en asm
extern int asm_calcular_gini(float valor);

// se accede a assembler a partir de c
int calcular_gini(float valor_gini) {
    int resultado = asm_calcular_gini(valor_gini);
    return resultado;
}