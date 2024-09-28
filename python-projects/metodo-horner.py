def horner_with_tables(coefs, x0, tol=1e-6, max_iter=10):
    n = len(coefs) - 1
    tables_b = []  # Tabela 1: Coeficientes b_i,n
    tables_c = []  # Tabela 2: Coeficientes c_i,n
    tables_x = []  # Tabela 3: Estimativas de x_n e ER_n

    x_n = x0
    for iter_num in range(max_iter):
        # Inicializa os coeficientes b e c
        b = [0] * (n + 1)
        c = [0] * n

        # Avaliação do polinômio e da derivada pelo Método de Horner
        b[n] = coefs[n]
        for i in range(n - 1, -1, -1):
            b[i] = coefs[i] + x_n * b[i + 1]
        
        c[n - 1] = n * coefs[n]
        for i in range(n - 2, -1, -1):
            c[i] = (i + 1) * coefs[i + 1] + x_n * c[i + 1]

        # Adiciona os coeficientes b e c nas tabelas
        tables_b.append([iter_num] + b)
        tables_c.append([iter_num] + c)

        # Nova estimativa de x_n
        x_new = x_n - b[0] / c[0]

        # Cálculo do erro relativo
        if x_new != 0:
            ER_n = abs((x_new - x_n) / x_new)
        else:
            ER_n = 0

        # Adiciona a estimativa e o erro relativo na tabela
        tables_x.append([iter_num, x_n, ER_n])

        # Atualiza x_n para a próxima iteração
        if ER_n < tol:
            x_n = x_new
            break
        x_n = x_new

    # Impressão das tabelas
    print("\nTabela 1: Coeficientes b_i,n da função P_N(x_n)")
    print("Iteração | b3,n  | b2,n  | b1,n  | b0,n")
    for row in tables_b:
        print(f"{row[0]:8d} | {row[1]:6.4f} | {row[2]:6.4f} | {row[3]:6.4f} | {row[4]:6.4f}")

    print("\nTabela 2: Coeficientes c_i,n da função P'_N(x_n)")
    print("Iteração | c3,n  | c2,n  | c1,n")
    for row in tables_c:
        print(f"{row[0]:8d} | {row[1]:6.4f} | {row[2]:6.4f} | {row[3]:6.4f}")

    print("\nTabela 3: Estimativas de x_n e erro relativo ER_n")
    print("Iteração | x_n    | ER_n")
    for row in tables_x:
        print(f"{row[0]:8d} | {row[1]:6.6f} | {row[2]:6.6f}")

    # Impressão da raiz estimada
    print(f"\nRaiz estimada: x = {x_n:.6f}")

# Exemplo de uso:
coefs = [4, -4, -2, 1]  # Coeficientes do polinômio x^3 - 2x^2 - 4x + 4 - devem ser postos ao contrario na lista
x0 = 0.5  # Chute inicial
horner_with_tables(coefs, x0)
