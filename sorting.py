import os
import sys
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm

comparacoes_selection_sort = trocas_selection_sort = 0
comparacoes_insertion_sort = trocas_insertion_sort = 0
comparacoes_quick_sort = trocas_quick_sort = 0
comparacoes_merge_sort = trocas_merge_sort = 0


def zera_contadores():
    global comparacoes_selection_sort, trocas_selection_sort
    global comparacoes_insertion_sort, trocas_insertion_sort
    global comparacoes_quick_sort, trocas_quick_sort
    global comparacoes_merge_sort, trocas_merge_sort

    comparacoes_selection_sort = trocas_selection_sort = 0
    comparacoes_insertion_sort = trocas_insertion_sort = 0
    comparacoes_quick_sort = trocas_quick_sort = 0
    comparacoes_merge_sort = trocas_merge_sort = 0

# selection sort
def selection_sort(vetor):
    global comparacoes_selection_sort, trocas_selection_sort
    comparacoes_selection_sort = trocas_selection_sort = 0
    for i in range(len(vetor)-1, 0, -1):
        posicao_maior = 0
        for j in range(1, i+1):
            comparacoes_selection_sort += 1
            if vetor[j] > vetor[posicao_maior]:
                posicao_maior = j
        if posicao_maior != i:
            trocas_selection_sort += 1
            aux = vetor[i]
            vetor[i] = vetor[posicao_maior]
            vetor[posicao_maior] = aux
    return vetor

# insertion sort
def insertion_sort(numbers):
    global comparacoes_insertion_sort, trocas_insertion_sort
    comparacoes_insertion_sort = trocas_insertion_sort = 0
    for i in range(1, len(numbers)):
        j = i
        while j > 0:
            comparacoes_insertion_sort += 1
            if numbers[j] < numbers[j - 1]:
                # swap
                numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
                trocas_insertion_sort += 1
            else:
                break
            j -= 1

    return numbers

# quick sort
def quick_sort(vetor):
    global comparacoes_quick_sort, trocas_quick_sort
    comparacoes_quick_sort = trocas_quick_sort = 0
    quick_sort_recursivo(vetor, 0, len(vetor) - 1)
    return vetor

def quick_sort_recursivo(vetor, inicio, fim):
    if inicio < fim:
        pivo = escolher_pivo(vetor, inicio, fim)
        p = particao(vetor, inicio, fim, pivo)
        quick_sort_recursivo(vetor, inicio, p - 1)
        quick_sort_recursivo(vetor, p + 1, fim)


def escolher_pivo(vetor, inicio, fim):
    # Seleciona o elemento do meio como pivô
    return (inicio + fim) // 2


def particao(vetor, inicio, fim, pivo):
    global comparacoes_quick_sort, trocas_quick_sort
    vetor[pivo], vetor[fim] = vetor[fim], vetor[pivo]
    pivo = vetor[fim]
    i = inicio
    for j in range(inicio, fim):
        comparacoes_quick_sort += 1
        if vetor[j] <= pivo:
            trocas_quick_sort += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]
            i += 1
    vetor[i], vetor[fim] = vetor[fim], vetor[i]
    return i

# merge sort
def merge_sort(arr):
    comparisons = 0  # Contagem de comparações
    inversions = 0  # Contagem de inversões

    if len(arr) <= 1:  # Caso base: array vazio ou com um único elemento
        return arr, comparisons, inversions

    mid = len(arr) // 2
    # Chamada recursiva para a metade esquerda
    left_half, left_comp, left_inv = merge_sort(arr[:mid])
    right_half, right_comp, right_inv = merge_sort(
        arr[mid:])  # Chamada recursiva para a metade direita

    # Atualiza a contagem de comparações com as contagens dos subarrays
    comparisons += left_comp + right_comp
    # Atualiza a contagem de inversões com as contagens dos subarrays
    inversions += left_inv + right_inv

    # Mescla os subarrays e conta as comparações e inversões resultantes
    merged, merge_comp, merge_inv = merge(left_half, right_half)

    # Atualiza a contagem de comparações com as comparações da mesclagem
    comparisons += merge_comp
    inversions += merge_inv  # Atualiza a contagem de inversões com as inversões da mesclagem

    # Retorna o vetor ordenado, juntamente com as contagens de comparações e inversões
    return merged, comparisons, inversions

def merge(left, right):
    merged = []  # Vetor mesclado
    comparisons = 0  # Contagem de comparações
    inversions = 0  # Contagem de inversões

    i = j = 0
    while i < len(left) and j < len(right):
        comparisons += 1  # Incrementa a contagem de comparações

        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inversions += 1 
    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged, comparisons, inversions

def salvaDados(nomeArquivo, n, comparacoes, trocas):

    if not os.path.exists('dados'):
        os.makedirs('dados')

    if not os.path.exists('dados/'+nomeArquivo + '.csv'):
        dados = pd.DataFrame(columns=['n', 'comparacoes', 'trocas'])
        dados.to_csv('dados/'+nomeArquivo + '.csv', index=False)
    if not n in leDados(nomeArquivo)[0]:
        dados = pd.DataFrame([[n, comparacoes, trocas]], columns=[
                             'n', 'comparacoes', 'trocas'])
        dados.to_csv('dados/'+nomeArquivo + '.csv',
                     mode='a', header=False, index=False)
    else:
        print('O valor de n ja existe no arquivo')

def leDados(nomeArquivo):
    dados = pd.read_csv('dados/'+nomeArquivo + '.csv')
    n = dados['n'].tolist()
    comparacoes = dados['comparacoes'].tolist()
    trocas = dados['trocas'].tolist()
    return n, comparacoes, trocas

def criaVetorAleatorio(n):
    vetor = []
    for i in range(n):
        # ver funcionamento e colocar no relatorio2
        vetor.append(random.randint(0, 100))
    return vetor


def criaVetorOrdenado(n):
    vetor = []
    for i in range(n):
        vetor.append(i)
    return vetor


def criaVetorOrdenadoReverso(n):
    vetor = []
    for i in range(n):
        vetor.append(n-i)
    return vetor

# realiza os testes e salva os dados
def sorting_aleatorio(n):
    global comparacoes_selection_sort, trocas_selection_sort
    global comparacoes_insertion_sort, trocas_insertion_sort
    global comparacoes_quick_sort, trocas_quick_sort
    global comparacoes_merge_sort, trocas_merge_sort

    # aleatorio
    vetor_aleatorio = criaVetorAleatorio(n)

    # copia os vetores.
    vetorSelectionAleatorio = vetor_aleatorio.copy()
    vetorInsertionAleatorio = vetor_aleatorio.copy()
    vetorQuickAleatorio = vetor_aleatorio.copy()
    vetorMergeAleatorio = vetor_aleatorio.copy()

    # Aleatorio
    zera_contadores()
    vetorSelectionAleatorio = selection_sort(vetorSelectionAleatorio)
    vetorInsertionAleatorio = insertion_sort(vetorInsertionAleatorio)
    vetorQuickAleatorio = quick_sort(vetorQuickAleatorio)
    # vetorMergeAleatorio = merge_sort(vetorMergeAleatorio)
    vetorMergeAleatorio, comparacoes_merge_sort, trocas_merge_sort = merge_sort(
        vetorMergeAleatorio)

    salvaDados('selection_sort_aleatorio', n,
               comparacoes_selection_sort, trocas_selection_sort)
    salvaDados('insertion_sort_aleatorio', n,
               comparacoes_insertion_sort, trocas_insertion_sort)
    salvaDados('quick_sort_aleatorio', n,
               comparacoes_quick_sort, trocas_quick_sort)
    salvaDados('merge_sort_aleatorio', n,
               comparacoes_merge_sort, trocas_merge_sort)


def sorting_ordenado(n):
    global comparacoes_selection_sort, trocas_selection_sort
    global comparacoes_insertion_sort, trocas_insertion_sort
    global comparacoes_quick_sort, trocas_quick_sort
    global comparacoes_merge_sort, trocas_merge_sort

    comparacoes_selection_sort = trocas_selection_sort = 0
    comparacoes_insertion_sort = trocas_insertion_sort = 0
    comparacoes_quick_sort = trocas_quick_sort = 0
    comparacoes_merge_sort = trocas_merge_sort = 0

    # cria o vetor e copia ele para os outros vetores
    vetor_ordenado = criaVetorOrdenado(n)
    vetorSelectionOrdenado = vetor_ordenado.copy()
    vetorInsertionOrdenado = vetor_ordenado.copy()
    vetorQuickOrdenado = vetor_ordenado.copy()
    vetorMergeOrdenado = vetor_ordenado.copy()

    # Ordenado
    zera_contadores()
    vetorSelectionOrdenado = selection_sort(vetorSelectionOrdenado)
    vetorInsertionOrdenado = insertion_sort(vetorInsertionOrdenado)
    vetorQuickOrdenado = quick_sort(vetorQuickOrdenado)
    # vetorMergeOrdenado = merge_sort(vetorMergeOrdenado)
    vetorMergeOrdenado, comparacoes_merge_sort, trocas_merge_sort = merge_sort(
        vetorMergeOrdenado)

    salvaDados('selection_sort_ordenado', n,
               comparacoes_selection_sort, trocas_selection_sort)
    salvaDados('insertion_sort_ordenado', n,
               comparacoes_insertion_sort, trocas_insertion_sort)
    salvaDados('quick_sort_ordenado', n,
               comparacoes_quick_sort, trocas_quick_sort)
    salvaDados('merge_sort_ordenado', n,
               comparacoes_merge_sort, trocas_merge_sort)


def sorting_ordenado_reverso(n):
    # ordenado reverso
    vetor_ordenado_reverso = criaVetorOrdenadoReverso(n)

    vetorSelectionOrdenadoReverso = vetor_ordenado_reverso.copy()
    vetorInsertionOrdenadoReverso = vetor_ordenado_reverso.copy()
    vetorQuickOrdenadoReverso = vetor_ordenado_reverso.copy()
    vetorMergeOrdenadoReverso = vetor_ordenado_reverso.copy()
    # vetorMergeOrdenadoReverso, comparacoes_merge_sort, trocas_merge_sort = merge_sort(vetor_ordenado_reverso.copy())

    # Ordenado Reverso
    zera_contadores()
    vetorSelectionOrdenadoReverso = selection_sort(
        vetorSelectionOrdenadoReverso)
    vetorInsertionOrdenadoReverso = insertion_sort(
        vetorInsertionOrdenadoReverso)
    vetorQuickOrdenadoReverso = quick_sort(vetorQuickOrdenadoReverso)
    # vetorMergeOrdenadoReverso = merge_sort(vetorMergeOrdenadoReverso)
    vetorMergeOrdenadoReverso, comparacoes_merge_sort, trocas_merge_sort = merge_sort(
        vetorMergeOrdenadoReverso)

    salvaDados('selection_sort_ordenado_reverso', n,
               comparacoes_selection_sort, trocas_selection_sort)
    salvaDados('insertion_sort_ordenado_reverso', n,
               comparacoes_insertion_sort, trocas_insertion_sort)
    salvaDados('quick_sort_ordenado_reverso', n,
               comparacoes_quick_sort, trocas_quick_sort)
    salvaDados('merge_sort_ordenado_reverso', n,
               comparacoes_merge_sort, trocas_merge_sort)


def graficos_comparacoes():
    # le os dados gerados
    # aleatorio
    selection_n_aleatorio, selection_comparacoes_aleatorio, selection_trocas_aleatorio = leDados(
        'selection_sort_aleatorio')
    insertion_n_aleatorio, insertion_comparacoes_aleatorio, insertion_trocas_aleatorio = leDados(
        'insertion_sort_aleatorio')
    quick_sort_n_aleatorio, quick_sort_comparacoes_aleatorio, quick_sort_trocas_aleatorio = leDados(
        'quick_sort_aleatorio')
    merge_sort_n_aleatorio, merge_sort_comparacoes_aleatorio, merge_sort_trocas_aleatorio = leDados(
        'merge_sort_aleatorio')

    # ordenado
    selection_n_ordenado, selection_comparacoes_ordenado, selection_trocas_ordenado = leDados(
        'selection_sort_ordenado')
    insertion_n_ordenado, insertion_comparacoes_ordenado, insertion_trocas_ordenado = leDados(
        'insertion_sort_ordenado')
    quick_sort_n_ordenado, quick_sort_comparacoes_ordenado, quick_sort_trocas_ordenado = leDados(
        'quick_sort_ordenado')
    merge_sort_n_ordenado, merge_sort_comparacoes_ordenado, merge_sort_trocas_ordenado = leDados(
        'merge_sort_ordenado')

    # ordenado reverso
    selection_n_ordenado_reverso, selection_comparacoes_ordenado_reverso, selection_trocas_ordenado_reverso = leDados(
        'selection_sort_ordenado_reverso')
    insertion_n_ordenado_reverso, insertion_comparacoes_ordenado_reverso, insertion_trocas_ordenado_reverso = leDados(
        'insertion_sort_ordenado_reverso')
    quick_sort_n_ordenado_reverso, quick_sort_comparacoes_ordenado_reverso, quick_sort_trocas_ordenado_reverso = leDados(
        'quick_sort_ordenado_reverso')
    merge_sort_n_ordenado_reverso, merge_sort_comparacoes_ordenado_reverso, merge_sort_trocas_ordenado_reverso = leDados(
        'merge_sort_ordenado_reverso')

    # graficos gerais
    plt.plot(selection_n_aleatorio, selection_comparacoes_aleatorio,
             label='Selection Sort')
    plt.plot(insertion_n_aleatorio, insertion_comparacoes_aleatorio,
             label='Insertion Sort')
    plt.plot(quick_sort_n_aleatorio, quick_sort_comparacoes_aleatorio,
             label='Quick Sort')
    plt.plot(merge_sort_n_aleatorio, merge_sort_comparacoes_aleatorio,
             label='Merge Sort')
    plt.xlabel('Qntd. de elementos')
    plt.ylabel('Comparacoes')
    plt.title('Vetor Aleatório - Número de Comparações')
    plt.legend()
    plt.show()

    plt.plot(selection_n_ordenado, selection_comparacoes_ordenado,
             label='Selection Sort')
    plt.plot(insertion_n_ordenado, insertion_comparacoes_ordenado,
             label='Insertion Sort')
    plt.plot(quick_sort_n_ordenado, quick_sort_comparacoes_ordenado,
             label='Quick Sort')
    plt.plot(merge_sort_n_ordenado, merge_sort_comparacoes_ordenado,
             label='Merge Sort')
    plt.xlabel('Qntd. de elementos')
    plt.ylabel('Comparacoes')
    plt.title('Vetor Ordenado - Número de Comparações')
    plt.legend()
    plt.show()

    plt.plot(selection_n_ordenado_reverso, selection_comparacoes_ordenado_reverso,
             label='Selection Sort')
    plt.plot(insertion_n_ordenado_reverso, insertion_comparacoes_ordenado_reverso,
             label='Insertion Sort')
    plt.plot(quick_sort_n_ordenado_reverso, quick_sort_comparacoes_ordenado_reverso,
             label='Quick Sort')
    plt.plot(merge_sort_n_ordenado_reverso, merge_sort_comparacoes_ordenado_reverso,
             label='Merge Sort')
    plt.xlabel('Qntd. de elementos')
    plt.ylabel('Comparacoes')
    plt.title('Vetor Ordenado (Decrescente) - Número de Comparações')
    plt.legend()
    plt.show()


    # graficos selection
    plt.plot(selection_n_aleatorio, selection_comparacoes_aleatorio,
             label='Aleatorio')
    plt.plot(selection_n_ordenado, selection_comparacoes_ordenado,
             label='Ordenado')
    plt.plot(selection_n_ordenado_reverso, selection_comparacoes_ordenado_reverso,
             label='Ordenado Reverso')
    plt.xlabel('Qntd. de elementos')
    plt.ylabel('Comparacoes')
    plt.title('Selection Sort - Número de Comparações')
    plt.legend()
    plt.show()

    # graficos insertion
    plt.plot(insertion_n_aleatorio, insertion_comparacoes_aleatorio,
             label='Aleatorio')
    plt.plot(insertion_n_ordenado, insertion_comparacoes_ordenado,
             label='Ordenado')
    plt.plot(insertion_n_ordenado_reverso, insertion_comparacoes_ordenado_reverso,
             label='Ordenado Reverso')
    plt.xlabel('Qntd. de elementos')
    plt.ylabel('Comparacoes')
    plt.title('Insertion Sort - Número de Comparações')
    plt.legend()
    plt.show()

    plt.plot(quick_sort_n_aleatorio, quick_sort_comparacoes_aleatorio,
             label='Aleatorio')
    plt.plot(quick_sort_n_ordenado, quick_sort_comparacoes_ordenado,
             label='Ordenado')
    plt.plot(quick_sort_n_ordenado_reverso, quick_sort_comparacoes_ordenado_reverso,
             label='Ordenado Reverso')
    plt.xlabel('Qntd. de elementos')
    plt.ylabel('Comparacoes')
    plt.title('Quick Sort - Número de Comparações')
    plt.legend()
    plt.show()

    plt.plot(merge_sort_n_aleatorio, merge_sort_comparacoes_aleatorio,
             label='Aleatorio')
    plt.plot(merge_sort_n_ordenado, merge_sort_comparacoes_ordenado,
             label='Ordenado')
    plt.plot(merge_sort_n_ordenado_reverso, merge_sort_comparacoes_ordenado_reverso,
             label='Ordenado Reverso')
    plt.xlabel('Qntd. de elementos')
    plt.ylabel('Comparacoes')
    plt.title('Merge Sort - Número de Comparações')
    plt.legend()
    plt.show()


def graficos_trocas():
    # le os dados gerados
    # aleatorio
    selection_n_aleatorio, selection_comparacoes_aleatorio, selection_trocas_aleatorio = leDados(
        'selection_sort_aleatorio')
    insertion_n_aleatorio, insertion_comparacoes_aleatorio, insertion_trocas_aleatorio = leDados(
        'insertion_sort_aleatorio')
    quick_sort_n_aleatorio, quick_sort_comparacoes_aleatorio, quick_sort_trocas_aleatorio = leDados(
        'quick_sort_aleatorio')
    merge_sort_n_aleatorio, merge_sort_comparacoes_aleatorio, merge_sort_trocas_aleatorio = leDados(
        'merge_sort_aleatorio')

    # ordenado
    selection_n_ordenado, selection_comparacoes_ordenado, selection_trocas_ordenado = leDados(
        'selection_sort_ordenado')
    insertion_n_ordenado, insertion_comparacoes_ordenado, insertion_trocas_ordenado = leDados(
        'insertion_sort_ordenado')
    quick_sort_n_ordenado, quick_sort_comparacoes_ordenado, quick_sort_trocas_ordenado = leDados(
        'quick_sort_ordenado')
    merge_sort_n_ordenado, merge_sort_comparacoes_ordenado, merge_sort_trocas_ordenado = leDados(
        'merge_sort_ordenado')

    # ordenado reverso
    selection_n_ordenado_reverso, selection_comparacoes_ordenado_reverso, selection_trocas_ordenado_reverso = leDados(
        'selection_sort_ordenado_reverso')
    insertion_n_ordenado_reverso, insertion_comparacoes_ordenado_reverso, insertion_trocas_ordenado_reverso = leDados(
        'insertion_sort_ordenado_reverso')
    quick_sort_n_ordenado_reverso, quick_sort_comparacoes_ordenado_reverso, quick_sort_trocas_ordenado_reverso = leDados(
        'quick_sort_ordenado_reverso')
    merge_sort_n_ordenado_reverso, merge_sort_comparacoes_ordenado_reverso, merge_sort_trocas_ordenado_reverso = leDados(
        'merge_sort_ordenado_reverso')

    # aleatorio
    plt.plot(selection_n_aleatorio, selection_trocas_aleatorio,
             label='Selection Sort')
    plt.plot(insertion_n_aleatorio, insertion_trocas_aleatorio,
             label='Insertion Sort')
    plt.plot(quick_sort_n_aleatorio, quick_sort_trocas_aleatorio,
             label='Quick Sort')
    plt.plot(merge_sort_n_aleatorio, merge_sort_trocas_aleatorio,
             label='Merge Sort (inversoes)')

    plt.xlabel('Qntd. de elementos')
    plt.ylabel('Trocas')
    plt.title('Vetor Aleatório - Número de Trocas')
    plt.legend()
    plt.show()

    # ordenado
    plt.plot(selection_n_ordenado, selection_trocas_ordenado,
             label='Selection Sort')
    plt.plot(insertion_n_ordenado, insertion_trocas_ordenado,
             label='Insertion Sort')
    plt.plot(quick_sort_n_ordenado, quick_sort_trocas_ordenado,
             label='Quick Sort')
    plt.plot(merge_sort_n_ordenado, merge_sort_trocas_ordenado,
             label='Merge Sort (inversoes)')

    plt.xlabel('Qntd. de elementos')
    plt.ylabel('Trocas')
    plt.title('Vetor Ordenado - Número de Trocas')
    plt.legend()
    plt.show()

    # ordenado reverso
    plt.plot(selection_n_ordenado_reverso, selection_trocas_ordenado_reverso,
             label='Selection Sort')
    plt.plot(insertion_n_ordenado_reverso, insertion_trocas_ordenado_reverso,
             label='Insertion Sort')
    plt.plot(quick_sort_n_ordenado_reverso, quick_sort_trocas_ordenado_reverso,
             label='Quick Sort')
    plt.plot(merge_sort_n_ordenado_reverso, merge_sort_trocas_ordenado_reverso,
             label='Merge Sort (inversoes)')

    plt.xlabel('Qntd. de elementos')
    plt.ylabel('Trocas')
    plt.title('Vetor Ordenado (Decrescente) - Número de Trocas')
    plt.legend()
    plt.show()

    # selection
    plt.plot(selection_n_aleatorio, selection_trocas_aleatorio,
             label='Aleatorio')
    plt.plot(selection_n_ordenado, selection_trocas_ordenado,
             label='Ordenado')
    plt.plot(selection_n_ordenado_reverso, selection_trocas_ordenado_reverso,
             label='Ordenado Reverso')

    plt.xlabel('Qntd. de elementos')
    plt.ylabel('Trocas')
    plt.title('Selection Sort - Número de Trocas')
    plt.legend()
    plt.show()

    # insertion
    plt.plot(insertion_n_aleatorio, insertion_trocas_aleatorio,
             label='Aleatorio')
    plt.plot(insertion_n_ordenado, insertion_trocas_ordenado,
             label='Ordenado')
    plt.plot(insertion_n_ordenado_reverso, insertion_trocas_ordenado_reverso,
             label='Ordenado Reverso')

    plt.xlabel('Qntd. de elementos')
    plt.ylabel('Trocas')
    plt.title('Insertion Sort - Número de Trocas')
    plt.legend()
    plt.show()

    # quick
    plt.plot(quick_sort_n_aleatorio, quick_sort_trocas_aleatorio,
             label='Aleatorio')
    plt.plot(quick_sort_n_ordenado, quick_sort_trocas_ordenado,
             label='Ordenado')
    plt.plot(quick_sort_n_ordenado_reverso, quick_sort_trocas_ordenado_reverso,
             label='Ordenado Reverso')

    plt.xlabel('Qntd. de elementos')
    plt.ylabel('Trocas')
    plt.title('Quick Sort - Número de Trocas')
    plt.legend()
    plt.show()

    # merge
    plt.plot(merge_sort_n_aleatorio, merge_sort_trocas_aleatorio,
             label='Aleatorio')
    plt.plot(merge_sort_n_ordenado, merge_sort_trocas_ordenado,
             label='Ordenado')
    plt.plot(merge_sort_n_ordenado_reverso, merge_sort_trocas_ordenado_reverso,
             label='Ordenado Reverso')

    plt.xlabel('Qntd. de elementos')
    plt.ylabel('Trocas')
    plt.title('Merge Sort - Número de Inversoes')
    plt.legend()
    plt.show()

    # outros graficos

def grafico_3d():
    selection_n_aleatorio, selection_comparacoes_aleatorio, selection_trocas_aleatorio = leDados(
        'selection_sort_aleatorio')
    insertion_n_aleatorio, insertion_comparacoes_aleatorio, insertion_trocas_aleatorio = leDados(
        'insertion_sort_aleatorio')
    quick_sort_n_aleatorio, quick_sort_comparacoes_aleatorio, quick_sort_trocas_aleatorio = leDados(
        'quick_sort_aleatorio')
    merge_sort_n_aleatorio, merge_sort_comparacoes_aleatorio, merge_sort_trocas_aleatorio = leDados(
        'merge_sort_aleatorio')

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(selection_n_aleatorio, selection_comparacoes_aleatorio,
               selection_trocas_aleatorio, c='r', marker='o')
    ax.scatter(insertion_n_aleatorio, insertion_comparacoes_aleatorio,
               insertion_trocas_aleatorio, c='b', marker='o')
    ax.scatter(quick_sort_n_aleatorio, quick_sort_comparacoes_aleatorio,
               quick_sort_trocas_aleatorio, c='g', marker='o')
    ax.scatter(merge_sort_n_aleatorio, merge_sort_comparacoes_aleatorio,
               merge_sort_trocas_aleatorio, c='y', marker='o')
    ax.set_title('Comparacoes e Trocas - Aleatorio')
    ax.set_xlabel('N')
    ax.set_ylabel('Comparacoes')
    ax.set_zlabel('Trocas')

    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    ax.xaxis.labelpad = 15
    ax.yaxis.labelpad = 15
    ax.zaxis.labelpad = 15

    ax.legend(['Selection Sort', 'Insertion Sort', 'Quick Sort', 'Merge Sort'])

    plt.show()

#gera as listas
def sort(n):
    sorting_aleatorio(n)
    sorting_ordenado(n)
    sorting_ordenado_reverso(n)


for index in range(10, 1010, 10):
  sort(index)

graficos_comparacoes()
graficos_trocas()
grafico_3d()
