from fpdf import FPDF

ERRO = 1e-06
n = 0

def f(x):
    return x ** 3 - 2 * x ** 2 - 4 * x + 4

def printa_iteracao(n, xn, fxn, erro_relativo):
    # Formatação da saída
    if n == 0:
        output = f"{n:<10} | {xn:.6f} | {fxn:.6f} | -"
    else:
        output = f"{n:<10} | {xn:.6f} | {fxn:.6f} | {erro_relativo:.6f}"

    print(output)

    # Escreve no PDF
    pdf.cell(0, 10, output, ln=True)

# Criando o PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, "Metodo da Secante, resolucao da funcao x^3 - 2x^2 - 4x + 4, intervalo [-2, -1]", ln=True)

# Adiciona cabeçalho da tabela ao PDF
pdf.cell(0, 10, "Iteração | x_n      | f(x_n)   | ER_n     ", ln=True)
pdf.cell(0, 10, "-" * 50, ln=True)

# Imprimir cabeçalho da tabela no console
print(f"{'Iteração':<10} | {'x_n':<10} | {'f(x_n)':<10} | {'ER_n':<10}")
print("-" * 50)

chute_inicial_1 = -2.0
chute_inicial_2 = -1.0

valores_x = [chute_inicial_1, chute_inicial_2]

erro_relativo = 1.0

while erro_relativo > ERRO:
    xn = valores_x[-1]
    fxn = f(xn)
    xn1 = valores_x[-2]
    fxn1 = f(xn1)

    # Chamada da função para printar a iteração
    printa_iteracao(n, xn, fxn, erro_relativo)
    n += 1

    chute = xn - (fxn * ((xn - xn1) / (fxn - fxn1)))
    valores_x.append(chute)

    # Cálculo do erro relativo
    erro_relativo = abs(valores_x[-1] - valores_x[-2])

# Finaliza o PDF
pdf.cell(0, 10, f"Raiz aproximada = {valores_x[-1]:.6f}", ln=True)
print(f"Raiz aproximada = {valores_x[-1]:.6f}")

pdf.output("output_iteracoes_secante.pdf")
