from fpdf import FPDF

ERRO = 1e-06
n = 0

def f(x):
    return x ** 3 - 2 * x ** 2 - 4 * x + 4

def printa_iteracao(n, xn, fxn, erro_relativo):
    if n == 0:
        #print(f"n = {n} | xn = {xn} | f(xn) = {fxn} | ERn = -")
        output = f"n = {n} | xn = {xn:.6f} | f(xn) = {fxn:.6f} | ERn = -"
    else:
        #print(f"n = {n} | xn = {xn} | f(xn) = {fxn} | ERn = {erro_relativo}")
        output = f"n = {n} | xn = {xn:.6f} | f(xn) = {fxn:.6f} | ERn = {erro_relativo:.6f}"

    print(output)

    pdf.cell(0, 10, output, ln=True)

# precisamos de dois chutes iniciais

# Criando o PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, "Metodo da Secante, resolucao da funcao x^3 - 2x^2 - 4x + 4, intervalo [-2, -1]", ln=True)

chute_inicial_1 = -2.0
chute_inicial_2 = -1.0

valores_x = []

valores_x.append(chute_inicial_1)
valores_x.append(chute_inicial_2)

erro_relativo = 1.0

while erro_relativo > ERRO:

    xn = valores_x[-1]
    fxn = f(xn)
    xn1 = valores_x[-2]
    fxn1 = f(xn1)

    printa_iteracao(n, xn, fxn, erro_relativo)
    n += 1

    chute = xn - (fxn * ((xn - xn1) / (fxn - fxn1)))
    valores_x.append(chute)

    erro_relativo = abs(valores_x[-1] - valores_x[-2])

#print(f"raiz aproximada = {valores_x[-1]}")

# Finaliza o PDF
pdf.cell(0, 10, f"Raiz aproximada = {valores_x[-1]:.6f}", ln=True)
print(f"Raiz aproximada = {valores_x[-1]:.6f}")

pdf.output("output_iteracoes_secante.pdf")