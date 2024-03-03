# Un conjunto de “n” personas votó de forma anónima entre un conjunto de “o” opciones (con o<<n). El resultado de la
# votación lo tenemos en un vector de n posiciones ordenado por opción seleccionada. Queremos determinar cuántos
# votos tuvo cada una de las opciones. Podemos hacerlo simplemente recorriendo el vector en O(n). Sin embargo,
# utilizando división y conquista se puede lograr en un tiempo inferior. Presentar y analizar una solución utilizando
# división y conquista que logre lo solicitado.

def contar_votos(votos, opciones): # O(o log n) y como o<<n => O(log n)
    conteo = {}
    inicio = 0
    
    for opcion in opciones:
        fin = buscar_fin(opcion, votos, inicio)
        cantidad_votos = fin - inicio
        if cantidad_votos > 0:
            conteo[opcion] = cantidad_votos
        inicio = fin
        
    return conteo

def buscar_fin(opcion, votos, inicio): # O(log n)
    # Realizamos una búsqueda binaria para encontrar el final de la opción en los votos
    izquierda = inicio
    derecha = len(votos) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if votos[medio] == opcion:
            izquierda = medio + 1
        elif votos[medio] < opcion:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return izquierda

# Ejemplo de uso
votos = ['a', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'd']
opciones = sorted(set(votos))  # Obtener las opciones únicas ordenadas
conteo = contar_votos(votos, opciones)
print("Conteo de votos para cada opción:", conteo)