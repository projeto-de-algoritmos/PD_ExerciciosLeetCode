from collections import Counter
from typing import List

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # Conta o número de ocorrências de cada letra nas letras fornecidas
        letter_count = Counter(letters)
        # Mapeia cada letra ao seu respectivo score
        score_map = {chr(ord('a') + i): score[i] for i in range(26)}
        # Variável para armazenar o máximo score encontrado
        max_score = 0

        def get_word_score(word, score_map):
            # Calcula o score de uma palavra com base no score_map
            return sum(score_map[ch] for ch in word)

        def backtrack(words, curr_word_idx, curr_score, letter_count):
            nonlocal max_score
            if curr_word_idx >= len(words):
                # Se todas as palavras foram consideradas, atualiza o máximo score encontrado
                max_score = max(max_score, curr_score)
                return

            curr_word = words[curr_word_idx]
            word_count = Counter(curr_word)

            if all(word_count[ch] <= letter_count[ch] for ch in curr_word):
                # Se as letras necessárias para formar a palavra estão disponíveis, faz uma chamada recursiva
                # incluindo a palavra no score atual e atualizando as contagens de letras
                backtrack(words, curr_word_idx + 1, curr_score + get_word_score(curr_word, score_map),
                          letter_count - word_count)

            # Faz uma chamada recursiva sem incluir a palavra no score atual
            backtrack(words, curr_word_idx + 1, curr_score, letter_count)

        # Inicia o backtracking com índice 0, score 0 e contagem de letras inicial
        backtrack(words, 0, 0, letter_count)
        # Retorna o máximo score encontrado
        return max_score
