#módulo utilizado para llamar a los menús y submenos en el módulo main
from inputs import *

def menu_principal():
    print("Menú Principal:")
    print("1. Dar de alta.")
    print("2. Modificar.")
    print("3. Eliminar.")
    print("4. Mostrar todos.")
    print("5. Ordenar pacientes")
    print("6. Buscar paciente por DNI")
    print("7. Calcular promedio")
    print("8. Determinar compatibilidad")
    print("9. Cuadro: donar y recibir")
    print("10. Salir")
    return get_int("Ingrese su elección: ", "Error", 1, 10, 3)

def menu_modificar():
    print("\nSeleccione el campo a actualizar:")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Edad")
    print("4. Altura")
    print("5. Peso")
    print("6. Grupo Sanguíneo")
    return get_int("Ingrese su elección: ", "Error", 1, 6, 3)

def menu_ordenar_criterio():
    print("\nSeleccione el criterio de ordenación:")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Altura")
    print("4. Grupo Sanguíneo")
    return get_int("Ingrese su elección: ", "Error", 1, 4, 3)

def menu_ordenar_ascendente():
    print("\nSeleccione de qué manera quiere ordenarlo:")
    print("1. Ascendente")
    print("2. Descendente (opción por default)")
    eleccion = get_int("Ingrese su elección: ", "Error", 1, 2, 3)
    if eleccion == 1:
        return True
    else:
       return False

def menu_promedio():
    print("\nSeleccione el atributo para calcular el promedio:")
    print("1. Edad")
    print("2. Altura")
    print("3. Peso")
    return get_int("Ingrese su elección: ", "Error", 1, 3, 3)