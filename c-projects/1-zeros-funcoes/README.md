# Método da bissecção para a obtenção de raízes de funções

## Determinando a existência de raízes

Esse método utiliza o teorema de Bolzano para demonstrar que uma determinada função tem solução em um determinado intervalo **[a, b]**. Resumidamente, se tivermos que $f(a) * f(b) < 0$, então existe pelo menos uma raiz nesse intervalo.

Para determinarmos que existe uma e somente uma raiz, existem algumas alternativas. Uma delas é analisar o comportamento da derivada da função no intervalo $(a, b)$.
Assim, se $\forall x \in (a, b)$, $f'(x) < 0$ ou $f(x) > 0$, então a função é monótona nesse intervalo, ou seja, é crescente ou decrescente, sem mudar seu comportamento. Isso garante que ela tenha somente uma raiz no intervalo em questão.

Outra forma mais simples é simplesmente plotar o gráfico da função.

## Calculando as raízes aproximadas

O método da bissecção em si é usado para obter-se a raiz aproximada de uma função em determinado intervalo **[a, b]**. Ele funciona da seguinte forma, inicialmente calculamos o primeiro chute fazendo $\frac{a+b}{2}$. 

Testa-se se $f(chute) = 0$, caso isso aconteça encontramos a raiz da função. 

O cenário mais comum é não encontrarmos a raiz exata, então analisamos o sinal de $f(a) * f(chute)$. Se $f(a) * f(chute) < 0$, significa que $a$ e $chute$ encontram-se em polos opostos do eixo x, ou seja, a raiz deve estar entre esses dois valores. Então fazemos $b = chute$ e continuamos o algoritmo.

Agora, se obtivermos o resultado $f(a) * f(chute) > 0$, significa que $a$ e $chute$ encontram-se no mesmo polo do eixo x, então devemos fazer $a = chute$ e continuar o algoritmo.

A condição de parada pode ser determinada de diversas formas, nessa implementação utilizamos um ERRO no valor de $10^{-6}$. Enquanto o erro relativo dado por $|a-b| > ERRO$ mantém-se a execução do algoritmo.

Com um ERRO de $10^{-6}$, teremos uma aproximação de raiz com 5 dígitos significativos corretos.