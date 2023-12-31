# -*- coding: utf-8 -*-
"""notebook

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19dPLywYNB47P0SCcjztPIDoJv8EGk3br
"""

import random
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm

def criarArrayAleatorio(n):
    array = []
    for i in range(n):
        array.append(random.randint(0, 100))
    return array

def criarArrayOrdenado(n):
    array = []
    for i in range(n):
        array.append(i)
    return array

def criarArrayOrdenadoReverso(n):
    array = []
    for i in range(n):
        array.append(n-i)
    return array

# de 10 a 1000, de 10 em 10
inicio = 10
fim = 1000 + inicio
passo = 10

"""## Bubble Sort"""

def bubble_sort(array):
    comparacoes = 0
    trocas = 0
    for i in range(len(array) - 1, 0, -1):
        troca_feita = False
        for j in range(i):
            comparacoes += 1
            if array[j] > array[j + 1]:
                trocas += 1
                array[j], array[j+1] = array[j+1], array[j] # realiza a troca
                troca_feita = True
        if not troca_feita:
            break
    return comparacoes, trocas

#
dados_bubble = {
        'n':[],
        'comparacoes_aleatorio':[],
        'comparacoes_ordenado':[],
        'comparacoes_reverso':[],
        'trocas_aleatorio':[],
        'trocas_ordenado':[],
        'trocas_reverso':[],
    }

df_bubble = pd.DataFrame(dados_bubble)

for index in range(inicio, fim, passo): # de 10 a 1000, de 10 em 10

    arrayAleatorio = criarArrayAleatorio(index)
    comparacoes_aleatorio, trocas_aleatorio = bubble_sort(arrayAleatorio)

    arrayOrdenado = criarArrayOrdenado(index)
    comparacoes_ordenado, trocas_ordenado = bubble_sort(arrayOrdenado)

    arrayReverso = criarArrayOrdenadoReverso(index)
    comparacoes_reverso, trocas_reverso = bubble_sort(arrayReverso)

    nova_linha = {
      'n':index,
      'comparacoes_aleatorio':comparacoes_aleatorio,
      'comparacoes_ordenado':comparacoes_ordenado,
      'comparacoes_reverso':comparacoes_reverso,
      'trocas_aleatorio':trocas_aleatorio,
      'trocas_ordenado':trocas_ordenado,
      'trocas_reverso':trocas_reverso,
    }

    nova_linha_df = pd.DataFrame([nova_linha])
    df_bubble = pd.concat([df_bubble, nova_linha_df], ignore_index=True)

df_bubble

"""## Selection Sort"""

def selection_sort(array):
    comparacoes = 0
    trocas = 0
    n = len(array)

    for i in range(n):
        posicao_menor = i

        for j in range(i + 1, n):
            comparacoes += 1
            if array[j] < array[posicao_menor]:
                posicao_menor = j

        if posicao_menor != i:
            trocas += 1
            array[i], array[posicao_menor] = array[posicao_menor], array[i]

    return comparacoes, trocas

dados_selection = {
        'n':[],
        'comparacoes_aleatorio':[],
        'comparacoes_ordenado':[],
        'comparacoes_reverso':[],
        'trocas_aleatorio':[],
        'trocas_ordenado':[],
        'trocas_reverso':[],
    }

df_selection = pd.DataFrame(dados_selection)


for index in range(inicio, fim, passo):

    vetorAleatorio = criarArrayAleatorio(index)
    comparacoes_aleatorio, trocas_aleatorio = selection_sort(vetorAleatorio)

    vetorOrdenado = criarArrayOrdenado(index)
    comparacoes_ordenado, trocas_ordenado = selection_sort(vetorOrdenado)

    vetorReverso = criarArrayOrdenadoReverso(index)
    comparacoes_reverso, trocas_reverso = selection_sort(vetorReverso)


    nova_linha = {
      'n':index,
      'comparacoes_aleatorio':comparacoes_aleatorio,
      'comparacoes_ordenado':comparacoes_ordenado,
      'comparacoes_reverso':comparacoes_reverso,
      'trocas_aleatorio':trocas_aleatorio,
      'trocas_ordenado':trocas_ordenado,
      'trocas_reverso':trocas_reverso,
    }

    nova_linha_df = pd.DataFrame([nova_linha])
    df_selection = pd.concat([df_selection, nova_linha_df], ignore_index=True)

df_selection

"""## Insertion Sort"""

def insertion_sort(array):
    comparacoes = 0
    trocas = 0

    for i in range(1, len(array)):
        j = i
        while j > 0:
            comparacoes += 1
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
                trocas += 1
            else:
                break
            j -= 1
    return comparacoes, trocas

dados_insertion = {
        'n':[],
        'comparacoes_aleatorio':[],
        'comparacoes_ordenado':[],
        'comparacoes_reverso':[],
        'trocas_aleatorio':[],
        'trocas_ordenado':[],
        'trocas_reverso':[],
    }

df_insertion = pd.DataFrame(dados_insertion)


for index in range(inicio, fim, passo): # de 10 a 1000, de 10 em 10

    vetorAleatorio = criarArrayAleatorio(index)
    comparacoes_aleatorio, trocas_aleatorio = insertion_sort(vetorAleatorio)

    vetorOrdenado = criarArrayOrdenado(index)
    comparacoes_ordenado, trocas_ordenado = insertion_sort(vetorOrdenado)

    vetorReverso = criarArrayOrdenadoReverso(index)
    comparacoes_reverso, trocas_reverso = insertion_sort(vetorReverso)


    nova_linha = {
      'n':index,
      'comparacoes_aleatorio':comparacoes_aleatorio,
      'comparacoes_ordenado':comparacoes_ordenado,
      'comparacoes_reverso':comparacoes_reverso,
      'trocas_aleatorio':trocas_aleatorio,
      'trocas_ordenado':trocas_ordenado,
      'trocas_reverso':trocas_reverso,
    }

    nova_linha_df = pd.DataFrame([nova_linha])
    df_insertion = pd.concat([df_insertion, nova_linha_df], ignore_index=True)

df_insertion

"""## Quick Sort"""

def quick_sort(array):
    comparacoes = 0
    trocas = 0

    def quick_sort_recursivo(array, inicio, fim):
        nonlocal comparacoes, trocas
        if inicio < fim:
            pivo = escolher_pivo(array, inicio, fim)
            p = particao(array, inicio, fim, pivo)
            quick_sort_recursivo(array, inicio, p - 1)
            quick_sort_recursivo(array, p + 1, fim)

    def escolher_pivo(array, inicio, fim):
        return (inicio + fim) // 2

    def particao(array, inicio, fim, pivo):
        nonlocal comparacoes, trocas
        array[pivo], array[fim] = array[fim], array[pivo]
        pivo = array[fim]
        i = inicio
        for j in range(inicio, fim):
            comparacoes += 1
            if array[j] <= pivo:
                array[i], array[j] = array[j], array[i]
                trocas += 1
                i += 1
        array[i], array[fim] = array[fim], array[i]
        return i

    quick_sort_recursivo(array, 0, len(array) - 1)

    return comparacoes, trocas

dados_quick = {
        'n':[],
        'comparacoes_aleatorio':[],
        'comparacoes_ordenado':[],
        'comparacoes_reverso':[],
        'trocas_aleatorio':[],
        'trocas_ordenado':[],
        'trocas_reverso':[],
    }

df_quick = pd.DataFrame(dados_quick)


for index in range(inicio, fim, passo): # de 10 a 1000, de 10 em 10

    vetorAleatorio = criarArrayAleatorio(index)
    comparacoes_aleatorio, trocas_aleatorio = quick_sort(vetorAleatorio)

    vetorOrdenado = criarArrayOrdenado(index)
    comparacoes_ordenado, trocas_ordenado = quick_sort(vetorOrdenado)

    vetorReverso = criarArrayOrdenadoReverso(index)
    comparacoes_reverso, trocas_reverso = quick_sort(vetorReverso)

    nova_linha = {
      'n':index,
      'comparacoes_aleatorio':comparacoes_aleatorio,
      'comparacoes_ordenado':comparacoes_ordenado,
      'comparacoes_reverso':comparacoes_reverso,
      'trocas_aleatorio':trocas_aleatorio,
      'trocas_ordenado':trocas_ordenado,
      'trocas_reverso':trocas_reverso,
    }

    nova_linha_df = pd.DataFrame([nova_linha])
    df_quick = pd.concat([df_quick, nova_linha_df], ignore_index=True)

df_quick

"""## Gráficos

### Comparacoes
"""

plt.plot(df_bubble['n'], df_bubble['comparacoes_aleatorio'], label='Bubble Sort')
plt.plot(df_bubble['n'], df_selection['comparacoes_aleatorio'], label='Selection Sort')
plt.plot(df_bubble['n'], df_insertion['comparacoes_aleatorio'], label='Insertion Sort')
plt.plot(df_bubble['n'], df_quick['comparacoes_aleatorio'], label='Quick Sort')
plt.xlabel('Qntd. de elementos')
plt.ylabel('Comparacoes')
plt.title('Array Aleatório - Número de Comparações')
plt.legend()
plt.show()

plt.plot(df_bubble['n'], df_bubble['comparacoes_ordenado'], label='Bubble Sort')
plt.plot(df_bubble['n'], df_selection['comparacoes_ordenado'], label='Selection Sort')
plt.plot(df_bubble['n'], df_insertion['comparacoes_ordenado'], label='Insertion Sort')
plt.plot(df_bubble['n'], df_quick['comparacoes_ordenado'], label='Quick Sort')
plt.xlabel('Qntd. de elementos')
plt.ylabel('Comparacoes')
plt.title('Array Ordenado - Número de Comparações')
plt.legend()
plt.show()

plt.plot(df_bubble['n'], df_bubble['comparacoes_reverso'], label='Bubble Sort')
plt.plot(df_bubble['n'], df_selection['comparacoes_reverso'], label='Selection Sort')
plt.plot(df_bubble['n'], df_insertion['comparacoes_reverso'], label='Insertion Sort')
plt.plot(df_bubble['n'], df_quick['comparacoes_reverso'], label='Quick Sort')
plt.xlabel('Qntd. de elementos')
plt.ylabel('Comparacoes')
plt.title('Array Ordenado Reverso - Número de Comparações')
plt.legend()
plt.show()

plt.plot(df_bubble['n'], df_bubble['comparacoes_aleatorio'], label='Aleatorio')
plt.plot(df_bubble['n'], df_bubble['comparacoes_ordenado'], label='Ordenado')
plt.plot(df_bubble['n'], df_bubble['comparacoes_reverso'], label='Reverso')
plt.xlabel('Qntd. de elementos')
plt.ylabel('Comparacoes')
plt.title('Bubble Sort - Número de Comparações')
plt.legend()
plt.show()

plt.plot(df_selection['n'], df_selection['comparacoes_aleatorio'], label='Aleatorio')
plt.plot(df_selection['n'], df_selection['comparacoes_ordenado'], label='Ordenado')
plt.plot(df_selection['n'], df_selection['comparacoes_reverso'], label='Reverso')
plt.xlabel('Qntd. de elementos')
plt.ylabel('Comparacoes')
plt.title('Selection Sort - Número de Comparações')
plt.legend()
plt.show()

plt.plot(df_insertion['n'], df_insertion['comparacoes_aleatorio'], label='Aleatorio')
plt.plot(df_insertion['n'], df_insertion['comparacoes_ordenado'], label='Ordenado')
plt.plot(df_insertion['n'], df_insertion['comparacoes_reverso'], label='Reverso')
plt.xlabel('Qntd. de elementos')
plt.ylabel('Comparacoes')
plt.title('Insertion Sort - Número de Comparações')
plt.legend()
plt.show()

plt.plot(df_quick['n'], df_quick['comparacoes_aleatorio'], label='Aleatorio')
plt.plot(df_quick['n'], df_quick['comparacoes_ordenado'], label='Ordenado')
plt.plot(df_quick['n'], df_quick['comparacoes_reverso'], label='Reverso')
plt.xlabel('Qntd. de elementos')
plt.ylabel('Comparacoes')
plt.title('Quick Sort - Número de Comparações')
plt.legend()
plt.show()

"""### Trocas"""

plt.plot(df_bubble['n'], df_bubble['trocas_aleatorio'], label='Bubble Sort')
plt.plot(df_bubble['n'], df_selection['trocas_aleatorio'], label='Selection Sort')
plt.plot(df_bubble['n'], df_insertion['trocas_aleatorio'], label='Insertion Sort')
plt.plot(df_bubble['n'], df_quick['trocas_aleatorio'], label='Quick Sort')
plt.xlabel('Qntd. de elementos')
plt.ylabel('Trocas')
plt.title('Array Aleatório - Número de Trocas')
plt.legend()
plt.show()

plt.plot(df_bubble['n'], df_bubble['trocas_ordenado'], label='Bubble Sort')
plt.plot(df_bubble['n'], df_selection['trocas_ordenado'], label='Selection Sort')
plt.plot(df_bubble['n'], df_insertion['trocas_ordenado'], label='Insertion Sort')
plt.plot(df_bubble['n'], df_quick['trocas_ordenado'], label='Quick Sort')
plt.xlabel('Qntd. de elementos')
plt.ylabel('Trocas')
plt.title('Array Ordenado - Número de Trocas')
plt.legend()
plt.show()

plt.plot(df_bubble['n'], df_bubble['trocas_reverso'], label='Bubble Sort')
plt.plot(df_bubble['n'], df_selection['trocas_reverso'], label='Selection Sort')
plt.plot(df_bubble['n'], df_insertion['trocas_reverso'], label='Insertion Sort')
plt.plot(df_bubble['n'], df_quick['trocas_reverso'], label='Quick Sort')
plt.xlabel('Qntd. de elementos')
plt.ylabel('Trocas')
plt.title('Array Reverso - Número de Trocas')
plt.legend()
plt.show()

plt.plot(df_bubble['n'], df_bubble['trocas_aleatorio'], label='Aleatorio')
plt.plot(df_bubble['n'], df_bubble['trocas_ordenado'], label='Ordenado')
plt.plot(df_bubble['n'], df_bubble['trocas_reverso'], label='Reverso')
plt.xlabel('Qntd. de elementos')
plt.ylabel('Trocas')
plt.title('Bubble Sort - Número de Trocas')
plt.legend()
plt.show()

plt.plot(df_selection['n'], df_selection['trocas_aleatorio'], label='Aleatorio')
plt.plot(df_selection['n'], df_selection['trocas_ordenado'], label='Ordenado')
plt.plot(df_selection['n'], df_selection['trocas_reverso'], label='Reverso')
plt.xlabel('Qntd. de elementos')
plt.ylabel('Trocas')
plt.title('Selection Sort - Número de Trocas')
plt.legend()
plt.show()

plt.plot(df_insertion['n'], df_insertion['trocas_aleatorio'], label='Aleatorio')
plt.plot(df_insertion['n'], df_insertion['trocas_ordenado'], label='Ordenado')
plt.plot(df_insertion['n'], df_insertion['trocas_reverso'], label='Reverso')
plt.xlabel('Qntd. de elementos')
plt.ylabel('Trocas')
plt.title('Insertion Sort - Número de Trocas')
plt.legend()
plt.show()

plt.plot(df_quick['n'], df_quick['trocas_aleatorio'], label='Aleatorio')
plt.plot(df_quick['n'], df_quick['trocas_ordenado'], label='Ordenado')
plt.plot(df_quick['n'], df_quick['trocas_reverso'], label='Reverso')
plt.xlabel('Qntd. de elementos')
plt.ylabel('Trocas')
plt.title('Quick Sort - Número de Trocas')
plt.legend()
plt.show()