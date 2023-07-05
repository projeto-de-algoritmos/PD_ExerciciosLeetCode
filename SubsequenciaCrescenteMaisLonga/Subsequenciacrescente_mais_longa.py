from bisect import bisect_left
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        
        for num in nums:
            idx = bisect_left(dp, num)
            if idx == len(dp):
                dp.append(num)
            else:
                dp[idx] = num
        
        return len(dp)
    
"""
A estratégia que utilizamos foi armazenar as sequências 
rescentes encontradas até o momento na lista dp. Em cada 
iteração, o algoritmo usa busca binária para encontrar a 
posição correta de inserção do número na lista dp. 
Se a posição encontrada for igual ao comprimento de
dp, o número é adicionado ao final da lista, caso 
contrário, ele substitui o valor existente nessa 
posição. No final, o algoritmo retorna o comprimento 
de dp, representando a sequência crescente mais longa 
encontrada. Essa abordagem é eficiente e otimizada, 
permitindo encontrar o resultado desejado de forma rápida.
"""