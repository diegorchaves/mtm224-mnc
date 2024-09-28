import math

# Definindo a constante de erro
ERRO = 1e-05

# Define a funcao: e^x - x - 2
def valor_funcao(x):
    return math.exp(x) - x - 2
# Define a derivada da funcao
def valor_derivada(x):
    return math.exp(x) - 1

def printa_iteracao(n, x, fxn, f1xn, erro_relativo):
    # Formatação da saída, com ER_n como "-" se n == 0
    if n == 0:
        output = f"{n:<10} | {x:.6f} | {fxn:.6f} | {f1xn:.6f} | -"
    else:
        output = f"{n:<10} | {x:.6f} | {fxn:.6f} | {f1xn:.6f} | {erro_relativo:.6f}"
    
    print(output)

# x inicial (chute)
x = 0.5
erro_relativo = 1.0
n = 0

# Imprimir cabeçalho da tabela no console
print(f"{'Iteração':<10} | {'x_n':<10} | {'f(x_n)':<10} | {'f\'(x_n)':<10} | {'ER_n':<10}")
print("-" * 65)

# Loop do método de Newton-Raphson
while erro_relativo > ERRO:
    fxn = valor_funcao(x)
    f1xn = valor_derivada(x)

    # Imprimir iteração atual
    printa_iteracao(n, x, fxn, f1xn, erro_relativo)

    # Atualizar x usando a fórmula do método de Newton-Raphson
    x -= fxn / f1xn

    # Calcular o erro relativo (pode ser a diferença absoluta do x anterior)
    erro_relativo = abs(fxn)  # O erro pode ser o valor absoluto da função em x

    n += 1

# Resultado final
print(f"\nRaiz aproximada = {x:.6f}")
