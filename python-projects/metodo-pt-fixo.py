import math

# Definindo a constante de erro
ERRO = 1e-05

# Função que representa g(x)
def valor_funcao(x):
    return (x ** 2 + 1) / 2.0

def printa_iteracao(n, chute, fxn, erro_relativo):
    # Formatação da saída
    output = f"{n:<10} | {chute:.6f} | {fxn:.6f} | {erro_relativo:.6f}"
    print(output)

# Chute inicial
chute = 0.5
erro_relativo = 1.0
n = 0

# Imprimir cabeçalho da tabela no console
print(f"{'Iteração':<10} | {'x_n':<10} | {'f(x_n)':<10} | {'ER_n':<10}")
print("-" * 50)

# Loop até a convergência
while erro_relativo > ERRO:
    fxn = valor_funcao(chute)

    # Imprimir iteração atual
    printa_iteracao(n, chute, fxn, erro_relativo)

    # Atualizar chute
    tmp = chute
    chute = fxn

    # Cálculo do erro relativo
    erro_relativo = abs(chute - tmp)

    n += 1

# Resultado final
print(f"\nRaiz aproximada = {chute:.6f}")
