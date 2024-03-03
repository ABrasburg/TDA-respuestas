# Tenés una colección de n libros con diferentes espesores, que pueden estar entre 1 y n (valores no necesariamente
# enteros). Tu objetivo es guardar esos libros en la menor cantidad de cajas. Todas las cajas que disponés son de la
# misma capacidad L (se asegura que L ≥n). Obviamente, no podés partir un libro para que vaya en múltiples cajas,
# pero sí podés poner múltiples libros en una misma caja, siempre y cuando no superen esa capacidad L. Implementar un
# algoritmo Greedy que obtenga la mínima cantidad de cajas a utilizar. Indicar y justificar la complejidad del algoritmo
# implementado. Justificar por qué se trata de un algoritmo greedy (no dar una respuesta genérica, sino aplicada a tu
# algoritmo). ¿El algoritmo propuesto encuentra siempre la solución óptima? Justificar.

# Agarro el primer libro y lo meto en una caja, si el segundo libro entra en la caja, lo meto, sino, abro una nueva
# caja. Y el tercer libro pruebo directo en la caja que tengo abierta, y así sucesivamente.

def min_cajas(libros, L):
    cajas = 0
    i = 0
    while i < len(libros):
        caja = 0
        while i < len(libros) and caja + libros[i] <= L:
            caja += libros[i]
            i += 1
        cajas += 1
    return cajas

libros = [1, 2, 3, 4, 5]
L = 5
print(min_cajas(libros, L)) 