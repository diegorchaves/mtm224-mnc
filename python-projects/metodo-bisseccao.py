import numpy as np

def printa_iteracao(n, a, chute, b, valor_funcao, erro):
    print(str(n) + " | a=" + str(a) + " | chute=", str(chute) + " | b=" + str(b) + " | valor_funcao=" + str(valor_funcao) + " | erro_rel=" + str(erro))

def f(x):
    return x ** 3 - 2 * x ** 2 - 4 * x + 4

# no intervalo [0, 1]
def calcula_ponto_central(a, b):
    return ((a + b) / 2)

n = 0
a = 0
b = 1
chute = calcula_ponto_central(a, b)
ERRO = 10e-6

print("n, a, chute, b, valor_funcao, erro_relativo" )
while abs(a - b) > ERRO:
    printa_iteracao(n, a, chute, b, f(chute), abs(a - b))
    n += 1
    chute = calcula_ponto_central(a, b)
    if f(chute) * f(a) < 0:
        b = chute
    elif f(chute) * f(b) < 0:
        a = chute
    elif f(chute) == 0:
        print(str(chute))

printa_iteracao(n, a, chute, b, f(chute), abs(a - b))

print("\n resultado = " + str(calcula_ponto_central(a, b)))