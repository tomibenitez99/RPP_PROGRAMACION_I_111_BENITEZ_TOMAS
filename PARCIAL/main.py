from inputs import *
from vidda import *
from paciente import Paciente
from menus import *

def main():
    """Método en donde se instancia a la clase Vidda y se llama al menu principal con sus submenús correspondientes
    """
    vidda = Vidda()

    bandera_seguir = True

    while bandera_seguir:
        opcion = menu_principal()

        match opcion:
            case 1:
                paciente = ingresar_datos_paciente()
                vidda.alta(Paciente(paciente.nombre, paciente.apellido, paciente.dni, paciente.edad, paciente.altura, paciente.peso, paciente.sangre))

            case 2:
                dni = get_dni("Ingrese el DNI del paciente: ", "DNI ingresado inválido", 3)
                paciente = vidda.buscar_paciente_por_dni(dni)
                if paciente:
                    sub_opcion = menu_modificar()
                    try:
                        cambios = {}
                        match sub_opcion:
                            case 1:
                                cambios[1] = get_nombre("Ingrese el nuevo nombre: ", "Error.", 3)
                            case 2:
                                cambios[2] = get_nombre("Ingrese el nuevo apellido: ", "Error.", 3)
                            case 3:
                                cambios[3] = get_int("Ingrese la nueva edad: ", "Error", 1, 120, 3)
                            case 4:
                                cambios[4] = get_int("Ingrese la nueva altura en cm: ", "Error", 30, 230, 3)
                            case 5:
                                cambios[5] = get_float("Ingrese el nuevo peso en kg: ", "Error", 10, 300, 3)
                            case 6:
                                cambios[6] = get_string_sangre("Ingrese el nuevo grupo sanguíneo: ", "Error.", 3)
                            case 7:
                                print("Actualización cancelada.")
                                continue
                        
                        paciente_anterior = paciente.clonar()
                        paciente_actualizado = vidda.modificar(dni, cambios)
                        if paciente_actualizado:
                            print("Paciente actualizado exitosamente.")
                            print(f"Paciente anterior: {paciente_anterior}")
                            print(f"Paciente actualizado: {paciente_actualizado}")
                        else:
                            print("No se pudo actualizar el paciente.")
                    except:
                        print("¡¡¡Error!!!")
                else:
                    print("Paciente no encontrado.")

            case 3:
                dni = get_dni("Ingrese el DNI del paciente: ", "DNI ingresado inválido", 3)
                paciente = vidda.eliminar(dni)
                if paciente:
                    print("Persona eliminada correctamente")
                else:
                    print("Persona no encontrada")

            case 4:
                vidda.mostrar_todos()

            case 5:
                criterio = menu_ordenar_criterio()
                es_ascendente = menu_ordenar_ascendente()
                vidda.ordenar_pacientes(criterio, es_ascendente)
                vidda.mostrar_todos()

            case 6:
                dni = get_dni("Ingrese el DNI del paciente: ", "DNI ingresado inválido", 3)
                print(vidda.buscar_paciente_por_dni(dni))

            case 7:
                atributo = menu_promedio()
                print(f"Promedio: {vidda.calcular_promedio(atributo)}")

            case 8:
                dni = get_dni("Ingrese el DNI del paciente: ", "DNI ingresado inválido", 3)
                vidda.determinar_compatibilidad(dni)

            case 9:
                matriz_compatibilidad = crear_matriz(compatibilidad_sangre())
                mostrar_matriz(matriz_compatibilidad)

            case 10:
                print("Saliendo del programa...")
                seguir = input("¿Seguro que quiere salir? ")
                if seguir.lower() == "si":
                    vidda.guardar_pacientes() #guarda los pacientes antes de salir
                    bandera_seguir = False

            case _:
                print("Opción inválida. Por favor, seleccione una opción válida.\n")

main()