def printa_tabela_iteracoes(iteracoes):
    # Cabeçalho da tabela
    print(f"{'n':^10} | {'a_n':^10} | {'x_n':^10} | {'b_n':^10} | {'f(x_n)':^10} | {'ER_n':^10}")
    print("-" * 75)

    # Exibe cada linha de iteração
    for iteracao in iteracoes:
        n, a_n, x_n, b_n, f_x_n, erro_rel = iteracao
        print(f"{n:^10} | {a_n:^10.6f} | {x_n:^10.6f} | {b_n:^10.6f} | {f_x_n:^10.6f} | {erro_rel:^10.6f}")

def f(x):
    return x ** 3 - 2 * x ** 2 - 4 * x + 4

# Função para calcular o ponto central (média)
def calcula_ponto_central(a, b):
    return (a + b) / 2

n = 0
a = 0
b = 1
chute = calcula_ponto_central(a, b)
ERRO = 1e-6  # Precisão
iteracoes = []  # Lista para armazenar os valores de cada iteração

# Armazena a primeira linha (n=0)
iteracoes.append([n, a, chute, b, f(chute), abs(a - b)])

# Loop principal do método da bisseção
while abs(a - b) > ERRO:
    n += 1
    chute = calcula_ponto_central(a, b)

    # Verifica o sinal do produto para determinar a nova bisseção
    if f(chute) * f(a) < 0:
        b = chute
    else:
        a = chute

    # Cálculo do erro relativo
    erro_relativo = abs(a - b)
    
    # Armazena os valores da iteração atual
    iteracoes.append([n, a, chute, b, f(chute), erro_relativo])

    # Se f(chute) for exatamente 0, então a raiz foi encontrada
    if f(chute) == 0:
        break

# Exibe a tabela formatada de iterações
printa_tabela_iteracoes(iteracoes)

# Exibir o resultado final (aproximação da raiz)
print(f"\nRaiz aproximada: {calcula_ponto_central(a, b):.6f}")
