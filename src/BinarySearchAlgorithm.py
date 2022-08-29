lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


# Busqueda binary_search_algorithm de forma iterativo
def binary_search_algorithm(lista, data):
    bajo = 0
    alto = len(lista) - 1
    centro = (bajo + alto) // 2
    while bajo <= alto:
        if lista[centro] == data:
            return centro
        elif lista[centro] < data:
            bajo = centro + 1
        else:
            alto = centro + 1
        centro = (bajo + alto) // 2

    return -1


# Busqueda binary_search_algorithm_recursive de forma Recursiva

def binary_search_algorithm_recursive(lista, bajo, alto, data):
    if bajo > alto:  # caso base
        return -1
    centro = (bajo + alto) // 2
    if lista[centro] == data:
        return centro
    elif lista[centro] < data:
        return binary_search_algorithm_recursive(lista, centro + 1, alto, data)
    else:
        return binary_search_algorithm_recursive(lista, bajo, centro - 1, data)


print(binary_search_algorithm_recursive(lista, 0, len(lista) - 1, 13))
