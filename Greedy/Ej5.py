# Una carrera tipo “Ironman” es un triatlón compuesto por 3 instancias: natación (3,86 km de natación), ciclismo (180 km)
# y carrera a pie (42,2km). Para conocer al ganador se suman los tiempos realizados en cada una de las etapas. Tanto el
# ciclismo como la carrera a pie se puede realizar en simultáneo con todos los inscriptos. Pero, por una regulación se
# prohibió que más de 1 persona realice la etapa de nado en el lago en simultáneo. Se conoce el tiempo estimado de cada
# participante para cada evento. Proponga un orden de salida de tal forma de minimizar el tiempo total de toda la
# competencia.

def orden_salida_ironman(participantes):
    # Ordenar participantes por tiempo estimado en la etapa de natación
    participantes.sort(key=lambda x: x[0])

    # Devolver el orden de salida
    return [participante[1] for participante in participantes]

# Ejemplo de uso
participantes = [(30, "Juan"), (25, "María"), (35, "Pedro"), (27, "Laura")]
orden_salida = orden_salida_ironman(participantes)
print("Orden de salida para el Ironman:")
for i, participante in enumerate(orden_salida, start=1):
    print(f"{i}. {participante}")
