/*  funcao x^2 + 2x + 1
    epsilon 1e-05
    chute inicial = 0.5 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>

#define ERRO 1e-05

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

float valorFuncao(float x)
{
    return ((pow(x, 2) + 1)/2.0);
}

int convergiu(float erroRelativo)
{
    return (erroRelativo < ERRO);
}

int main ()
{

    Raiz *raiz;
    raiz = init(0.5);
    float tmp;

    printf("n | chute | erroRel | g(x) | ERRO\n");

    while (!convergiu(raiz->erroRelativo))
    {
        tmp = raiz->chute;
        printf("%d %f %f %f %f\n", raiz->n, raiz->chute, raiz->erroRelativo,
                valorFuncao(raiz->chute), ERRO);

        raiz->n++;
        raiz->chute = valorFuncao(raiz->chute);
        raiz->erroRelativo = fabs(raiz->chute - tmp);
    }

    printf("resultado = %f", raiz->chute);
    
}