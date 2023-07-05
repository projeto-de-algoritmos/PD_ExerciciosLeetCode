from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        distances = [INF] * n
        distances[src] = 0

        for _ in range(k + 1):
            prevDistances = list(distances)

            for flight in flights:
                fromCity, toCity, price = flight
                distances[toCity] = min(distances[toCity], prevDistances[fromCity] + price)

        return distances[dst] if distances[dst] != INF else -1

"""
Neste código utilizamos Bellman-Ford, inicializamos as distâncias como 
infinito para todas as cidades, exceto a cidade 
de origem, que é definida como 0. Em seguida, 
iteramos k+1 vezes (incluindo 0) para relaxar as 
arestas do grafo. A lista distanciasAnteriores 
mantém as distâncias da iteração anterior para 
evitar atualizar as distâncias antes de serem usadas 
na iteração atual. Por fim, retornamos a distância 
até a cidade de destino dst, ou -1 se não houver 
uma rota válida.
"""