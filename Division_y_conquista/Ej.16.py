# Dentro de un país existen dos colonias subacuáticas cada una de ellas con “n” habitantes. Cada habitante tiene su
# documento de identidad único identificado por un número. Para una tarea especial se decidió seleccionar a aquella
# persona que vive en alguna de las colonias cuyo número de documento corresponda a la mediana de todos los números de
# documento presentes en ellas. Por una cuestión de protocolo no nos quieren dar los listados completos de documentos.
# Solo nos responden de cada colonia ante la consulta “Cual es el documento en la posición X de todos los habitantes de
# la isla ordenados de mayor a menor”. Utilizando esto, proponer un algoritmo utilizando división y conquista que
# resuelva el problema con la menor cantidad posibles de consultas. Analizar complejidad espacial y temporal.

def obtener_mediana(colonia1, colonia2, n):
    # Llamamos a la función auxiliar para buscar la mediana global
    return buscar_mediana(colonia1, colonia2, 0, n - 1, 0, n - 1)

def buscar_mediana(colonia1, colonia2, inicio1, fin1, inicio2, fin2):
    # Si solo hay un elemento en cada colonia, retornamos el menor de los dos
    if inicio1 == fin1 and inicio2 == fin2:
        return min(colonia1[inicio1], colonia2[inicio2])

    # Obtenemos las posiciones intermedias en ambas colonias
    medio1 = (inicio1 + fin1) // 2
    medio2 = (inicio2 + fin2) // 2

    # Obtenemos los documentos en las posiciones intermedias
    doc_medio1 = colonia1[medio1]
    doc_medio2 = colonia2[medio2]

    # Si el tamaño de la sublista es par, ajustamos medio2 para evitar tomar un elemento que no existe
    if (fin1 - inicio1 + 1) % 2 == 0:
        medio2 += 1

    # Si los documentos son iguales, hemos encontrado la mediana global
    if doc_medio1 == doc_medio2:
        return doc_medio1

    # Si el documento de la colonia 1 en la posición media es mayor, buscamos en la primera mitad de la colonia 1 y segunda mitad de la colonia 2
    elif doc_medio1 > doc_medio2:
        return buscar_mediana(colonia1, colonia2, inicio1, medio1, medio2, fin2)

    # Si el documento de la colonia 2 en la posición media es mayor, buscamos en la segunda mitad de la colonia 1 y primera mitad de la colonia 2
    else:
        return buscar_mediana(colonia1, colonia2, medio1, fin1, inicio2, medio2)

# Ejemplo de uso
colonia1 = [10, 20, 30, 40, 50]
colonia2 = [15, 25, 35, 45, 55]
n = len(colonia1)

# Se asume que los índices en las consultas comienzan desde 0
documento_mediana = obtener_mediana(colonia1, colonia2, n)
print("El documento de identidad de la mediana global es:", documento_mediana)
