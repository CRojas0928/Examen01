class Conjuntos:
    #creacion de los vectores para el conjunto1 y conjunto2

    conjunto1 = ['a', 'b', 'c', 'd', 'e']
    conjunto2 = ['i', 'o','a','e']

    #se enlistan para comparar si es una union o una interseccion

    union = list(set(conjunto1) | set(conjunto2))
    interseccion = list(set(conjunto1) & set(conjunto2))

    #impresion de la union y la interseccion
    print("Unión de los conjuntos:", union)
    print("Intersección de los conjuntos:", interseccion)

