# [Pontuação Máxima Palavras Formadas por Letras](https://leetcode.com/problems/maximum-score-words-formed-by-letters/)

**Nível: Difícil**

Dada uma lista de `words`, lista de `letters` únicas (pode estar repetindo) e `score` de cada caractere.

Retorna a pontuação máxima de **qualquer** conjunto válido de palavras formado usando as letras fornecidas (`word[i]` não podem ser usadas duas ou mais vezes).

Não é necessário usar todos os caracteres nas `letters` e cada letra só pode ser usada uma vez. A pontuação das letras `'a', 'b', 'c', ... , 'z'` é dada por `score[0]`, `score[1]`, ... , `score[25]` respectivamente.


**Exemplo 1:**

``` bash
Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
Output: 23
Explicação: Score a=1, c=9, d=5, g=3, o=2
Dadas as letras, podemos formar as palavras "dad" (5+1+5) e "good" (3+2+2+5) com uma pontuação de 23. As 
palavras "dad" e "dog" obtêm apenas uma pontuação de 21.
```

**Exemplo 2:**

``` bash
Input: words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
Output: 27
Explicação: Score a=4, b=4, c=4, x=5, z=10
Dadas as letras, podemos formar as palavras "ax" (4+5) , "bx" (4+5) e "cx" (4+5) com pontuação 27. 
A palavra "xxxz" recebe apenas 25 pontos.
```

**Exemplo 3:**

``` bash
Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
Output: 0
Explicação: Letra "e" só pode ser usado uma vez.
```