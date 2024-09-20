/*  epsilon = 10e-6
    x^3 - 2x^2 - 4x + 4
    possui 3 raízes no intervalo [-2, 3]
    tem que dividir nos intervalos [-2, -1], [0, 1] e [2, 3]

    1. intervalo que contém somente uma raiz
    2. calcula o ponto central
    3. comparação com as extremidades
    4. erro relativo
    */
#define ERRO 1e-6

#include "metodo-bisseccao.h"

int convergiu(const float erroRelativo)
{
    if(erroRelativo < ERRO) return 1;

    return 0;
}

void printaIteracao(int n, float a, float chute,
                    float valorFuncao, float erroRelativo)
{
    printf("%d %f %f %f %f\n", n, a, chute, valorFuncao, erroRelativo);
}

float funcao(float x)
{
    float y;
    y = pow(x, 3) - (2 * pow(x, 2)) - 4 * x + 4;
    return (float)y;
}

float calculaChute(float a, float b)
{
    return (a + b) / 2.0;
}

Raiz *init(int a, int b)
{
    Raiz *self;
    self = malloc(sizeof(*self));
    assert(self != NULL);

    self->n = 0;
    self->a = a;
    self->b = b;
    self->chute = calculaChute(a, b);
    self->erroRelativo = 1.0;
    return self;
}

int main()
{
    Raiz *raiz = init(0, 1);
    while(!convergiu(raiz->erroRelativo))
    {
        printaIteracao(raiz->n, raiz->a, raiz->chute, 
                    funcao(raiz->chute), raiz->erroRelativo);
        
        raiz->n++;

        if(funcao(raiz->chute) * funcao(raiz->a) < 0)
            raiz->b = raiz->chute;
        else if(funcao(raiz->chute) * funcao(raiz->b) < 0)
            raiz->a = raiz->chute;
        else if(funcao(raiz->chute) == 0)
        {
            printf("solucao = %f\n", raiz->chute);
            break;
        }
        raiz->chute = calculaChute(raiz->a, raiz->b);
        raiz->erroRelativo = fabs(raiz->b - raiz->a);
    }
    
    printaIteracao(raiz->n, raiz->a, raiz->chute, 
                    funcao(raiz->chute), raiz->erroRelativo);
    
    printf("solucao = %f\n", calculaChute(raiz->a, raiz->b));

    return 0;
}