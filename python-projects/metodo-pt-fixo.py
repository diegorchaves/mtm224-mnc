from fpdf import FPDF
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
    # Escreve no PDF
    pdf.cell(0, 10, output, ln=True)


# Chute inicial
chute = 0.5
erro_relativo = 1.0
n = 0

# Criando o PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, "Metodo Ponto Fixo, resolucao da funcao e^x - x - 2, intervalo [-2, -1]", ln=True)


# Adiciona cabeçalho da tabela ao PDF
pdf.cell(0, 10, "Iteração | x_n      | f(x_n)   | ER_n   ", ln=True)
pdf.cell(0, 10, "-" * 50, ln=True)

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
output = f"\nRaiz aproximada = {chute:.6f}"
print(output)

# Finaliza o PDF
pdf.cell(0, 10, output, ln=True)
pdf.output("output_iteracoes_pt_fixo.pdf")
