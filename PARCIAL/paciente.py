from inputs import *

class Paciente:
    """Clase Paciente la cual se utilizará para instanciar paciente en el módulo vidda"""
    def __init__(self, nombre, apellido, dni: int, edad, altura, peso, sangre):
        """constructor de Paciente

        Args:
            nombre (_type_): nombre del paciente
            apellido (_type_): apellido del paciente
            dni (int): dni, se pide que sea int porque en el caso de que el dni tenga menos de 8 caracteres, es necesario pasarlo a string y pasarlo por la función zfill(8) para que el dni siempre tenga 8 caracteres
            edad (_type_): edad del paciente
            altura (_type_): altura del paciente
            peso (_type_): peso del paciente
            sangre (_type_): grupo sanguíneo del paciente
        """
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.dni = str(dni).zfill(8)
        self.sangre = sangre

    def __str__(self):
        """Representa en forma de string la instancia de la clase Paciente"""
        return f'| {self.nombre} | {self.apellido} | {self.edad} años | {self.altura}cm | {self.peso}kg | {self.dni} | {self.sangre}'
    
    def clonar(self):
        """Utilizo esta función para guardar un paciente sin modificar (uso en main.py - linea 46)"""
        return Paciente(self.nombre, self.apellido, self.dni, self.edad, self.altura, self.peso, self.sangre)
    