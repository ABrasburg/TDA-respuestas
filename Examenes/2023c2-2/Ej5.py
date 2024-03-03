# Tenemos una ruta recta muy larga, de K kilómetros, sobre la cual hay casas dispersas. En dichas casas vive gente que
# usa mucho sus celulares. El intendente a cargo la ruta debe renovar por completo el sistema de antenas, teniendo que
# construir sobre la ruta nuevas antenas. Cada antena tiene un rango de cobertura de R kilómetros (valor constante
# conocido). Implementar un algoritmo Greedy que reciba las ubicaciones de las casas (número de kilómetro sobre esta
# ruta) y devuelva los kilómetros sobre los que debemos construir las antenas para que todas las casas tengan cobertura,
# y se construya para esto la menor cantidad de antenas posibles. Indicar y justificar la complejidad del algoritmo
# implementado. Justificar por qué se trata de un algoritmo greedy

def antenas(casas, r):
    casas.sort()
    antenas = []
    i = 0
    while i < len(casas):
        antena = casas[i] + r
        while i < len(casas) and casas[i] <= antena:
            i += 1
        antenas.append(antena)
    return antenas

