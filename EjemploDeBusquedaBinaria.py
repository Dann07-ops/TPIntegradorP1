def binary_search(lista, objetivo, inicio, fin ):
    if inicio > fin:
        return -1

    centro = (inicio + fin) // 2
    if lista[centro] == objetivo:
        return centro
    elif lista[centro] < objetivo:
        return binary_search(lista, objetivo, centro + 1, fin)
    else:
        return binary_search(lista, objetivo, inicio, centro - 1)
        

# Ejemplo de uso
lista = [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 15, 20, 27, 34, 39, 50]
numero_objetivo = 27
inicio_busqueda = 0
fin_busqueda = len(lista) - 1

resultado = binary_search(lista, numero_objetivo, inicio_busqueda, fin_busqueda)

if resultado != -1:
    print(f"El número {numero_objetivo} se encuentra en la posición {resultado}.")
else:
    print(f"El númeor {numero_objetivo} NO se encuentra en la lista.")