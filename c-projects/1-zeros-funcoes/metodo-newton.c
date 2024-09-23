/*  funcao e^x - x - 2
    epsilon 1e-05
    chute inicial = 0.5 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>


#define ERRO 1e-05

float valorFuncao(float chute)
{
    return exp(chute) - chute - 2;
}

float valorDerivada(float chute)
{
    return exp(chute) - 1;
}

typedef struct raiz
{
    int n;
    float erroRelativo;
    float chute;
} Raiz;

Raiz *init(float chute)
{
    Raiz *self;
    self = malloc(sizeof(*self));
    assert(self != NULL);

    self->n = 0;
    self->chute = chute;
    self->erroRelativo = 1.0;

    return self;
}

int convergiu(float erroRelativo)
{
    return(erroRelativo < ERRO);
}

float calculaChute(float chute)
{
    return (chute - (valorFuncao(chute))/valorDerivada(chute));
}

int main()
{
    Raiz *raiz = init(0.5);
    float tmp;

    printf("n | chute | erroRel | f(x) | f1(x) | ERRO\n");

    while(!convergiu(raiz->erroRelativo))
    {
        tmp = raiz->chute;
        printf("%d %f %f %f %f %f\n", raiz->n, raiz->chute, raiz->erroRelativo,
                valorFuncao(raiz->chute), valorDerivada(raiz->chute), ERRO);

        raiz->n++;
        raiz->chute = calculaChute(raiz->chute);
        raiz->erroRelativo = fabs(tmp - raiz->chute);
    }

    printf("resultado = %f", raiz->chute);
    
}