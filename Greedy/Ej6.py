# Las membresías al club de vino “Varietales de cuyo” son de 4 categorías: “Titanio”, “Oro”, “Plata” y “Básico”. Cada
# socio tiene una membresía. Por mes envían un pack de degustación que llaman “alfa”, “beta”, “gamma” y “epsilon”. Un
# socio “Titanio” sólo puede recibir un pack “alfa”, Un socio “Oro” puede recibir un pack “alfa” o “beta”, un socio
# “Plata” sólo puede recibir “alfa” o “gamma”. Finalmente un “Básico” puede recibir cualquier pack. Diseñar una estrategia
# greedy para resolver el siguiente problema: Sean Pa, Pb, Pg, Pd los packs disponibles de cada tipo y St, So, Sp, Sb los
# socios de cada categoría. Informar cómo se puede satisfacer la distribución de packs entre socios (o si no se puede
# satisfacer).

def distribucion_packs(Pa, Pb, Pg, Pd, St, So, Sp, Sb):
    sol = {}
    if Pa < St:
        return "No se puede satisfacer"
    sol["Titanio"] = []
    sol ["Titanio"].append((St, "alfa"))
    Pa -= St
    if Pa + Pb < So:
        return "No se puede satisfacer"
    sol["Oro"] = []
    if Pb > So:
        sol["Oro"].append((So, "beta"))
        Pb -= So
        So = 0
    else:
        sol["Oro"].append((Pb, "beta"))
        So -= Pb
        Pb = 0
    sol["Oro"].append((So, "alfa"))
    Pa -= So
    if Pa + Pg < Sp:
        return "No se puede satisfacer"
    sol["Plata"] = []
    if Pg > Sp:
        sol["Plata"].append((Sp, "gamma"))
        Pg -= Sp
        Sp = 0
    else:
        sol["Plata"].append((Pg, "gamma"))
        Sp -= Pg
        Pg = 0
    sol["Plata"].append((Sp, "alfa"))
    Pa -= Sp
    sol["Básico"] = []
    if Pa + Pb + Pg + Pd < Sb:
        return "No se puede satisfacer"
    if Pd > Sb:
        sol["Básico"].append((Sb, "epsilon"))
        Pd -= Sb
        Sb = 0
    else:
        sol["Básico"].append((Pd, "epsilon"))
        Sb -= Pd
        Pd = 0
    if Pb > Sb:
        sol["Básico"].append((Sb, "beta"))
        Pb -= Sb
        Sb = 0
    else:
        sol["Básico"].append((Pb, "beta"))
        Sb -= Pb
        Pb = 0
    if Pg > Sb:
        sol["Básico"].append((Sb, "gamma"))
        Pg -= Sb
        Sb = 0
    else:
        sol["Básico"].append((Pg, "gamma"))
        Sb -= Pg
        Pg = 0
    sol["Básico"].append((Sb, "alfa"))
    return sol

Pa = 10
Pb = 10
Pg = 10
Pd = 10
St = 1
So = 1
Sp = 1
Sb = 1
print(distribucion_packs(Pa, Pb, Pg, Pd, St, So, Sp, Sb))