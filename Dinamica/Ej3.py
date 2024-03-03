# El dueño de una empresa desea organizar una fiesta de la misma. Cómo quiere que la fiesta sea lo más tranquila posible,
# no quiere que asistan un empleado y su jefe directo, pero tampoco quiere que se salteen más de 1 nivel jerárquico.
# Charles le pidió a su encargado que le ponga un rating de convivencia (Ri) a cada empleado y con dicha información más
# un organigrama de la compañía, le pidió a un especialista en informática que diseñe un algoritmo para obtener el listado
# de los empleados que deberá invitar a la fiesta. Teniendo en cuenta que: Ri > 0, que Charles no cuenta para el armado
# del algoritmo y que la estructura jerárquica es en forma de árbol. Se pide resolver mediante programación dinámica.

# El problema se puede resolver con programación dinámica. La idea es recorrer el árbol jerárquico de la empresa y en cada
# nodo, calcular el máximo rating de convivencia que se puede obtener si se invita a los empleados que se encuentran en
# ese subárbol. Para esto, se debe calcular el máximo rating de convivencia que se puede obtener si se invita al nodo
# actual y el máximo rating de convivencia que se puede obtener si no se invita al nodo actual. Luego, se debe tomar el
# máximo de estos dos valores y devolverlo. La solución al problema será el máximo rating de convivencia que se puede
# obtener si se invita al nodo raíz del árbol.

def max_rating(root):
    '''Calcula el máximo rating de convivencia que se puede obtener si se invita al nodo root'''
    if root is None:
        return 0
    # Si el nodo actual es una hoja, el máximo rating de convivencia que se puede obtener es el rating del nodo
    if len(root.children) == 0:
        return root.rating
    # Calculo el máximo rating de convivencia que se puede obtener si se invita al nodo actual
    invite = root.rating
    for child in root.children:
        invite += max_rating(child.children[0])
    # Calculo el máximo rating de convivencia que se puede obtener si no se invita al nodo actual
    not_invite = 0
    for child in root.children:
        not_invite += max_rating(child)
    # Devuelvo el máximo entre invite y not_invite
    return max(invite, not_invite)
