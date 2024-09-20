#ifndef BISSECCAO_H
#define BISSECCAO_H

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct raiz 
{
    int n;
    float a;
    float b;
    float chute;
    float erroRelativo;
} Raiz;

Raiz *init(int a, int b);

float funcao(float x);

float calculaChute(float a, float b);

void printaIteracao(int n, float a, float chute,
                    float valorFuncao, float erroRelativo);

int convergiu(const float erroRelativo);

#endif