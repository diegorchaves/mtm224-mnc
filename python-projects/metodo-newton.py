from fpdf import FPDF
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
    # Escreve no PDF
    pdf.cell(0, 10, output, ln=True)

# x inicial (chute)
x = 0.5
erro_relativo = 1.0
n = 0

# Criando o PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, "Metodo de Newton, resolucao da funcao e^x - x - 2, intervalo [-2, -1]", ln=True)

# Adiciona cabeçalho da tabela ao PDF
pdf.cell(0, 10, "Iteração | x_n      | f(x_n)   | f'(x_n)    | ER_n   ", ln=True)
pdf.cell(0, 10, "-" * 50, ln=True)

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
output = f"\nRaiz aproximada = {x:.6f}"
print(output)

# Finaliza o PDF
pdf.cell(0, 10, output, ln=True)
pdf.output("output_iteracoes_newton.pdf")