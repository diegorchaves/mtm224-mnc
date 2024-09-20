# Método da bissecção para a obtenção de raízes de funções

Esse método utiliza o teorema de Bolzano para demonstrar que uma determinada função tem solução em um determinado intervalo [a, b]. Resumidamente, se tivermos que $f(a) * f(b) < 0$, então existe pelo menos uma raiz nesse intervalo.

Para determinarmos que existe uma e somente uma raiz, existem algumas alternativas. Uma delas é analisar o comportamento da derivada da função no intervalo $(a, b)$.
Assim, se $\forall x \in (a, b)$, $f'(x) < 0$ ou $f(x) > 0$, então a função é monótona nesse intervalo, ou seja, é crescente ou decrescente, sem mudar seu comportamento. Isso garante que ela tenha somente uma raiz no intervalo em questão.

Outra forma mais simples é simplesmente plotar o gráfico da função.