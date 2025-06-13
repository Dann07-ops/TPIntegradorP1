#Caso practico de Ordenamiento por burbuja
def insertion_sort(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        index = i 
        while index > 0 and lista[index - 1] > actual:
            lista[index] = lista[index - 1]
            index = index - 1
        lista[index] = actual

    return lista

lista_desordenada = [39, 45, 32, 4, 2, 85, 43, 7, 18, 16, 5, 67, 32]
lista_ordenada = insertion_sort(lista_desordenada)
print(lista_ordenada) # output: [2, 4, 5, 7, 16, 18, 32, 32, 39, 43, 45, 67, 85]