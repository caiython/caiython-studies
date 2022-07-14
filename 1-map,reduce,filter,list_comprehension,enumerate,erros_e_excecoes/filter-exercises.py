# -*- coding: utf-8 -*-
"""python3_exercicios_map,reduce,filter,list_comprehension,enumerate,erros_e_excecoes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O-FYxKnHXs0twF1pF4EE1LjJwYgpzuO6

# Função filter()
Lista de exercícios resolvidos voltados ao uso da função built-in **filter()** utilizando a Linguagem Python

1. Use filter() para imprimir apenas os nomes menores ou iguais a sete letras
"""

#Dados
lista_de_nomes = ["Adriana","Bernardo", "Bruno", "Carlos", "Felipe", "Flávia", "Luísa"]

#Resolução
list(filter(lambda name: len(name) <= 7, lista_de_nomes))

"""2. Usando a função filter(), filtre a lista para que apenas os números negativos sejam retornados"""

#Dados
lst1 = [12, -1, 9, 8, -0.5, -0.2, -100]

#Resolução
list(filter(lambda num: num < 0,lst1))

"""3. Usando a função filter(), filtre os números pares para que apenas os números ímpares sejam passados ​​para a nova lista."""

#Dados
lst1=[22, 100, 19, 13, 11, 1, 4, 66]

#Resolução
list(filter(lambda num: num % 2 != 0,lst1))

"""4. Usando as funções filter() e list() e o método .lower() filtre todas as vogais em uma determinada string."""

#Dados
str1 = "Winter Olympics in 2022 will take place in Beijing China"

#Resolução
list(filter(lambda char: char.lower() not in ['a','e','i','o','u'],str1))

"""5. Desta vez, usando as funções filter() e list() filtre todos os inteiros positivos na string."""

#Dados
str1 = "Winter Olympics in 2022 will take place in Beijing China"

#Resolução
list(filter(lambda char: char not in ['1','2','3','4','5','6','7','8','9','0'],str1))