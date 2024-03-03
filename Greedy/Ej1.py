# Una ruta tiene un conjunto de bifurcaciones para acceder a diferentes pueblos. El listado (ordenado por nombre del pueblo)
# contiene el número de kilómetros donde está ubicada cada una. Se desea ubicar la menor cantidad de patrullas policiales
# (en las bifurcaciones) de tal forma que no haya bifurcaciones con vigilancia a más de 50 km. Proponer un algoritmo que
# lo resuelva. 

# Ejemplo (ciudad,Bifurcación): (Castelli, 185), (Gral Guido, 249), (Lezama 156), (Maipu, 270), (Sevigne, 194).
#	Si incluimos un patrullero en la bifurcación de Lezama, cubre además de esta a Castelli y Sevigne. Pero no Gral Guido
# y Maipú. Se necesitaría en ese caso, ubicar otro. Al agregar otro patrullero en Gral Guido, se cubren todas las ciudades
# restantes. Con 2 móviles policiales en bifurcaciones se cubren todas los accesos a todas las ciudades con distancia menor
# a 50km.

# La idea es recorrer las ciudades, y ver para cada ciudad X cuantas ciudades hay a menos de 50km. Le asignamos un patrullero
# a la ciudad con más ciudades a menos de 50km. Luego, eliminamos las ciudades que ya están cubiertas y repetimos el proceso
# hasta que no queden ciudades sin patrullero.

# O(n^2) en el peor caso, ya que para cada ciudad, recorremos todas las ciudades para ver cuantas están a menos de 50km.
# En el mejor caso, O(n) si todas las ciudades están a más de 50km de distancia.
def patrullas(cities):
    patrullas = []
    while len(cities) > 0:
        max = 0
        max_city = ""
        for city in cities:
            count = 0
            for c in cities:
                if abs(c - city) < 50:
                    count += 1
            if count > max:
                max = count
                max_city = city
        patrullas.append(max_city)
        cities = [c for c in cities if abs(c - max_city) >= 50]
    return patrullas

cities = [185, 249, 156, 270, 194]
print(patrullas(cities))