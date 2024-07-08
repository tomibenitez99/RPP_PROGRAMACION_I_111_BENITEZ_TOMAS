import validate
import sys

def read_number_aux(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int, isFloat:bool) -> float|int|None:
    """Función que utilizo para pedir un número sea entero o flotante

    Args:
        mensaje (str): el mensaje que le pide al usuario que ingrese el número
        mensaje_error (str): un mensaje de error por si ingresa un número fuera de lo validado
        minimo (float): un mínimo para validar
        maximo (float): un máximo para validar
        reintentos (int): cantidad de intentos que va a tener el usuario de ingresar el dato en caso de fallo
        isFloat (bool): pregunto si es flotante para saber si es entero o flotante

    Returns:
        float|int|None: devuelvo el número, entero, flotante o none dependiendo el caso que sea cada uno
    """
    while reintentos > 0:
        try:
            if isFloat:
                numero = float(input(mensaje))
            else: 
                numero = int(input(mensaje))
            
            if validate.validate_number(numero, minimo, maximo):
                return numero
            else:
                print(mensaje_error)
        except ValueError:
            print(mensaje_error)
        reintentos -= 1

    print("Se agotaron los intentos")
    sys.exit()

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int|None:
    """Llamo a la función read_numer_aux() para que el usuario ingrese su número, pero yo quiero que en este caso sea un entero

    Args:
    Casi los mismos que la función read_number_aux, sin el isFloat. Esto se lo preguntaré en lo que me devuelve la función

    Returns:
        devuelvo un entero, en el parámetro isFloat, le pido que sea False para que justamente, sea un entero
    """
    return read_number_aux(mensaje, mensaje_error, minimo, maximo, reintentos, False)

def get_float(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> float|None:
    """IGUAL a get_int, pero con el isFloat en True
    """
    return read_number_aux(mensaje, mensaje_error, minimo, maximo, reintentos, True)

def get_dni(mensaje: str, mensaje_error: str, reintentos: int) -> int:
    """Igual al get_int y al get_float, pero con un mínimo y máximo dados por la función y no por el usuario
    """
    return read_number_aux(mensaje, mensaje_error, 4000000, 99999999, reintentos, False)

def get_nombre(mensaje: str, mensaje_error: str, reintentos: int) -> str|None:
    """Función que utilizo para pedir un nombre o apellido
    Utilizo, la validación de validar_nombre_apellido() y al texto validado lo paso por la función .capitalize() para que palabra del texto que devuelve empiece con mayus

    Args:
        mensaje (str): mensaje que pide al usuario el ingreso de un nombre o apellido
        reintentos (int): cantidad de intentos

    Returns:
        str|None: devuelve el string ingresado por el usuario
    """
    #manejo de intentos
    while reintentos > 0:
        try:
            texto = input(mensaje)
            if validate.validar_nombre_apellido(texto):
                texto = texto.capitalize()
                return texto
            else:
                print(mensaje_error)
        except ValueError:
            print(mensaje_error)
        reintentos -= 1

    print("Se agotaron los intentos")
    sys.exit()

def get_string_sangre(mensaje: str, mensaje_error: str, reintentos: int) -> str|None:
    """lo mismo que get_nombre pero con validar_sangre, y un .upper() para que me devuelva todo en mayus
    """
    while reintentos > 0:
        try:
            texto = input(mensaje)
            if validate.validar_sangre(texto):
                texto = texto.upper()
                return texto
            else:
                print(mensaje_error)
        except ValueError:
            print(mensaje_error)
        reintentos -= 1

    print("Se agotaron los intentos")
    sys.exit()