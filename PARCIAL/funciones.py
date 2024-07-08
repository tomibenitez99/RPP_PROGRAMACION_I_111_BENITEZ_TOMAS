from inputs import *
from paciente import Paciente

def ingresar_datos_paciente():
        """Función que utilizo para pedir al usuario que ingrese los datos del paciente

        Returns:
            devuelvo un objeto Paciente 
        """

        nombre = get_nombre("Ingrese el nombre del paciente: ", "Error. Nombre ingresado inválido.", 3)
        apellido = get_nombre("Ingrese el apellido del paciente: ", "Error. Apellido ingresado inválido.", 3)
        dni = get_dni("Ingrese el DNI del paciente: ", "Error. DNI ingresado inválido", 3)
        edad = get_int("Ingrese la edad del paciente: ", "Error. Edad ingresada inválida", 1, 120, 3)
        altura = get_int("Ingrese la altura en cm del paciente: ", "Error. Altura ingresada inválida", 30, 230, 3)
        peso = get_float("Ingrese el peso en kg del paciente: ", "Error. Peso ingresado inválido", 10, 300, 3)
        sangre = get_string_sangre("Ingrese el grupo sanguíneo del paciente: ", "Error. Grupo sanguíneo ingresado inválido", 3)
        return Paciente(nombre, apellido, dni, int(edad), int(altura), float(peso), sangre)

def swap(a, b):
        """Función que utilizo para el método de ordenamiento "Bubblesort"

        Args:
            recibo a y b

        Returns:
            los devuelvo al revés (b y a)
        """
        return b, a 

def compatibilidad_sangre() -> dict:
    diccionario = {
        "A+": {"recibir": ["O+", "O-", "A+", "A-"], "donar": ["A+", "AB+"]},
        "A-": {"recibir": ["O-", "A-"], "donar": ["A+", "A-", "AB+", "AB-"]},
        "B+": {"recibir": ["B+", "B-", "O+", "O-"], "donar": ["B+", "AB+"]},
        "B-": {"recibir": ["O-", "B-"], "donar": ["B+", "B-", "AB+", "AB-"]},
        "AB+": {"recibir": ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"], "donar": ["AB+", "AB-"]},
        "AB-": {"recibir": ["A-", "AB-", "B-", "O-"], "donar": ["AB-", "AB+"]},
        "O+": {"recibir": ["O+", "O-"], "donar": ["A+", "AB+", "B+", "O+"]},
        "O-": {"recibir": ["O-"], "donar": ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]}
    }

    return diccionario

def contar_donar(tipo_sangre, compatibilidad: dict):
    return len(compatibilidad[tipo_sangre]["donar"])

def contar_recibir(tipo_sangre, compatibilidad: dict):
    return len(compatibilidad[tipo_sangre]["recibir"])

def crear_matriz(compatibilidad: dict):
    tipos_sangre = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    matriz = [[0]*3 for _ in range(len(tipos_sangre))]
    

    for i in range(len(tipos_sangre)): #len(matriz) = filas
          tipo_sangre = tipos_sangre[i]
          matriz[i][0] = tipo_sangre
          matriz[i][1] = contar_donar(tipo_sangre, compatibilidad)
          matriz[i][2] = contar_recibir(tipo_sangre, compatibilidad)       

    return matriz

def mostrar_matriz(matriz):
    for i in range(len(matriz)): #len(matriz) = filas
        for j in range(len(matriz[0])): #len(matriz[0]) = columnas
            print(f"{matriz[i][j]:5}", end = " ") #:5 JUSTIFICACIÓN para que se vea más prolija la matriz. 5 a cuántos caracteres me va a ubicar cada elemento
        print("")