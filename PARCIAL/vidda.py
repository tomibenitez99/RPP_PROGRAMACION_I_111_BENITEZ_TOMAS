from inputs import *
from paciente import *
from funciones import *

class Vidda:
    """clase Vidda en la cual estarán casi todas las operaciones a realizar"""
    def __init__(self, archivo_csv="pacientes.csv"):
        """constructor de la clase Vidda.
        Cuenta con un acumulador de id para que sea autoincrementable y una lista vacía de pacientes donde se cargarán los pacientes ingresados
        """
        self.pacientes = [] #lista donde se van a ir agregando los pacientes
        self.next_id = 1 #contador de id
        self.archivo_csv = archivo_csv #archivo csv donde se agregaran los pacientes
        self.cargar_pacientes()

    def cargar_pacientes(self):
        "Cargar pacientes desde un archivo CSV"
        try:
            with open(r"PARCIAL\pacientes.csv", mode="r", newline="") as archivo:
                for linea in archivo:
                    fila = linea.strip().split(",")
                    if fila:
                        nombre, apellido, dni, edad, altura, peso, sangre = fila
                        paciente = Paciente(nombre, apellido, dni, int(edad), int(altura), float(peso), sangre)
                        paciente.id = self.next_id
                        self.pacientes.append(paciente)
                        self.next_id += 1
        except FileNotFoundError:
            print(f"Archivo {self.archivo_csv} no encontrado. Se inicia una lista vacía de pacientes")

    def guardar_pacientes(self):
        """Guardar pacientes en un archivo CSV"""
        with open(r"PARCIAL\pacientes.csv", mode = "w", newline = "") as archivo:
            for paciente in self.pacientes:
                archivo.write(f"{paciente.nombre},{paciente.apellido},{paciente.dni},{paciente.edad},{paciente.altura},{paciente.peso},{paciente.sangre}\n")

    def alta(self, paciente: Paciente):
        """Dar de Alta

        Args:
            paciente (Paciente): recibe como parámetro a paciente de tipo Paciente

        Returns:
            paciente: y lo devuelve
        """
        paciente.id = self.next_id #le asigna el id
        self.pacientes.append(paciente) #y agrega al paciente a la lista self.pacientes
        self.next_id += 1 #cada vez que le doy de alta a un paciente el id se autoincrementa en 1
        return paciente
    
    def identificar_paciente(self, dni) -> Paciente|None:
        """Función utilizada para identificar a un paciente

        Args:
            dni (_type_): se los identifica por dni que se le pide ingresar al usuario

        Returns:
            Paciente|None: y devuelve al paciente y si no lo encuentra, devuelve None
        """
        for paciente in self.pacientes:
            if int(paciente.dni) == int(dni):
                return paciente
        return None

    def eliminar(self, dni):
        """Función utilizada para eliminar a un paciente
        Args:
            dni (_type_): se los identifica por dni que se le pide ingresar al usuario

        Returns:
            _type_: al igual que identificar_paciente, si lo encuentra, devuelve al paciente y lo elimina, sino devuelve None
        """
        paciente = self.identificar_paciente(dni)
        if paciente:
            self.pacientes.remove(paciente)
            return paciente
        return None

    def modificar(self, dni, cambios) -> Paciente|None: 
        """Función utilizada para modificar a un paciente

        Args:
            dni (_type_): se busca al paciente por dni (que lo ingresa el usuario)
            cambios (_type_): el cambio hecho se guarda en un diccionario en el módulo main

        Returns:
            Paciente|None: si encuentra al paciente lo devuelve, sino devuelve None
        """
        paciente = self.identificar_paciente(dni)

        if paciente:
            for campo, valor in cambios.items():
                if campo == 1:
                    paciente.nombre = valor
                elif campo == 2:
                    paciente.apellido = valor
                elif campo == 3:
                    paciente.edad = valor
                elif campo == 4:
                    paciente.altura = valor
                elif campo == 5:
                    paciente.peso = valor
                elif campo == 6:
                    paciente.sangre = valor
                else:
                    print(f"Cambio no válido.")
            return paciente
        return None

    def mostrar_todos(self):
        """Función utilizada para mostrar la lista de pacientes con el formato pedido en la consigna
        """
        print("********************************************************************")
        print("| Nombre | Apellido | Edad | Altura | Peso | DNI | Grupo sanguíneo |")
        for paciente in self.pacientes:
            print(paciente)
        print("********************************************************************")
     
    def ordenar_pacientes(self, criterio: int, ascendente: bool):
        """Función para ordenar a los pacientes según un criterio

        Args:
            criterio (int): se pide al usuario mediante un menú que elija, el criterio con el cual quiere ordenar a los pacientes.
            ascendente (bool): depende si ascendente es True or False los ordenará de manera ascendente o descendente
        """
        #función anidada
        def obtener_valor(paciente):
            """función dentro ordenar pacientes para pedir el valor del criterio

            devuelve el nombre, apellido, altura o grupo sanguíneo del paciente, dependiendo que opción ingrese el usuario en el menú
            """
            if criterio == 1:
                return paciente.nombre 
            elif criterio == 2:
                return paciente.apellido
            elif criterio == 3:
                return paciente.altura
            elif criterio == 4:
                return paciente.sangre
            else:
                print(f"Criterio de ordenación no válido: {criterio}")
            
            
        """Bubblesort"""
        for i in range(len(self.pacientes)):
            for j in range(0, len(self.pacientes)-i-1):
                if ascendente:
                    if obtener_valor(self.pacientes[j]) > obtener_valor(self.pacientes[j + 1]):
                        self.pacientes[j], self.pacientes[j + 1] = swap(self.pacientes[j], self.pacientes[j + 1])
                else:
                    if obtener_valor(self.pacientes[j]) < obtener_valor(self.pacientes[j + 1]):
                        self.pacientes[j], self.pacientes[j + 1] = swap(self.pacientes[j], self.pacientes[j + 1])

        return self.pacientes

    def buscar_paciente_por_dni(self, dni) -> Paciente|None:
        """Función para buscar a un paciente por dni

        Args:
            dni (_type_): se le pide al usuario que ingrese el dni del paciente a buscar

        Returns:
            Paciente|None: devuelve al paciente o None en caso de no encontrarlo
        """
        return self.identificar_paciente(dni)
    
    def calcular_promedio(self, atributo):
        """Función para calcular promedio, con una estructura similar a la función ordenar_pacientes

        Args:
            atributo (_type_): el atributo se obtendrá mediante la función obtener_atributo
        """
        def obtener_atributo(paciente):
            """función dentro de calcular promedio para obtener el valor del atributo

            devuelve la edad, la altura o el peso, dependiendo la opción que ingrese el usuario en el menú
            """
            if atributo == 1:
                return paciente.edad
            elif atributo == 2:
                return paciente.altura
            elif atributo == 3:
                return paciente.peso
            else:
                print(f"Atributo de ordenación no válido: {atributo}")

        """Se hace la operación del promedio con un total que acumulará los valores del atributo del paciente y un contador que contará la cantidad de pacientes que se promediarán"""
        total = 0 #acumulador
        contador = 0
        for p in self.pacientes:
            total += obtener_atributo(p)
            contador += 1

        if contador > 0:
            return total / contador
        else:
            return 0
        
    def determinar_compatibilidad(self, dni):
        """Función que determina qué grupo sanguíneo puede recibir de o donar a qué otro grupo sanguíneo

        Args:
            dni (_type_): se le pide al usuario ingresar un dni para determinar qué otros pacientes le pueden donar sangre
        """
        paciente = self.identificar_paciente(dni)
        if not paciente:
            print("Paciente no encontrado.")
            return
        
        diccionario = compatibilidad_sangre()

        puede_recibir_de = diccionario[paciente.sangre]["recibir"]

        donantes = [] #se crea una lista vacía para agregarle los 3 primeros donantes que pueden donarle al paciente del dni ingresado
        for p in self.pacientes:
            if p.sangre in puede_recibir_de and p != paciente:
                donantes.append(p)
                if len(donantes) == 3: #si la longitud de la lista es = a 3, se termina la iteración y no se agrega a nadie más
                    break

        if donantes:
            print("Primeros 3 donantes compatibles: ")
            for d in donantes:
                print(f"{d.apellido}, {d.nombre} - Grupo sanguíneo: {d.sangre}")
            
        else:
            print("No se encontraron donantes compatibles")