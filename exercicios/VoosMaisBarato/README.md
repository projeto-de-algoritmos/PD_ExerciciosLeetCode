# [Voos mais Baratos Dentro de K Paradas](https://leetcode.com/problems/cheapest-flights-within-k-stops/description/)

**Nível: Médio**

Existem `n` cidades conectadas por um certo número de voos. Você recebe uma matriz chamada `flights`, onde `flights[i] = [from_i, to_i, price_i]` indica que há um voo da cidade `from_i` para a cidade `to_i` com custo `price_i`.

Você também recebe três números inteiros: `src`, `dst` e `k`. Retorne o preço mais barato para ir de `src` para `dst` com no máximo `k` paradas. Se não houver uma rota possível, retorne `-1`.


**Exemplo 1:**

![Exemplo1](https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-3drawio.png)

``` bash
Entrada: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Saída: 700
Explicação:
O grafo é mostrado acima.
O caminho ótimo com no máximo 1 parada da cidade 0 para a cidade 
3 é marcado em vermelho e tem custo 100 + 600 = 700.
Observe que o caminho através das cidades [0,1,2,3] 
é mais barato, mas é inválido porque usa 2 paradas.
```

**Exemplo 2:**

![Exemplo2](https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-1drawio.png)

``` bash
Entrada: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Saída: 200
Explicação:
O grafo é mostrado acima.
O caminho ótimo com no máximo 1 parada da cidade 0 para a cidade 2 é marcado em vermelho e 
tem custo 100 + 100 = 200.
```

**Exemplo 3:**

![Exemplo3](https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-2drawio.png)

``` bash
Entrada: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Saída: 500
Explicação:
O grafo é mostrado acima.
O caminho ótimo sem paradas da cidade 0 para a cidade 2 é marcado em vermelho e tem custo 500.
```