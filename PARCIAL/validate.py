def validate_number(numero: int|float, minimo: int, maximo: int) -> bool:
    """Valido el número

    Args:
        numero (int | float): recibo un número (que lo va a ingresar el usuario)
        minimo (int): le doy un mínimo 
        maximo (int): y un máximo

    Returns:
        bool: devuelve True or False dependiendo si está dentro del rango mínimo - máximo,
    """
    return numero >= minimo and numero <= maximo

def validar_nombre_apellido(texto:str) -> bool:
    """Valido el nombre o apellido

    Args:
        texto (str): recibo el input ingresado por el usuario por parametro

    Returns:
        bool: devuelve True si todas las condiciones se cumplen (isalpha, len<=20, validar_cadena_letras)
    """
    return (len(texto) <= 20) and validar_cadena_letras(texto)
    
def validate_int(numero: int, minimo: int, maximo: int) -> bool:
    #lo mismo que validate_number, pero solo con ints
    return numero >= minimo and numero <= maximo

def validate_float(numero: float, minimo: int, maximo: int) -> bool:
    #lo mismo que validate_int, pero con floats
    return numero >= minimo and numero <= maximo

def validar_sangre(sangre:str) -> bool:
    #Creo un diccionario con las variantes válidas
    tipos_de_sangre = {
        "A+": True,
        "A-": True,
        "AB+": True,
        "AB-": True,
        "B+": True,
        "B-": True,
        "O+": True,
        "O-": True
    }
    sangre = sangre.upper()
    #Verifico
    return tipos_de_sangre.get(sangre, False)

def es_letra_ascii(un_caracter) -> bool:
    """valido si una letra es ascii

    Args:
        un_caracter (_type_): recibo el caracter que quiero validar

    Returns:
        bool: devuelve true or false dependiendo si la letra está dentro de la colección validos
    """
    es_valido = False #bandera
    validos = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" #colección que contiene como elementos las letras del abecedario en mayus y minus
    for i in range(len(validos)):
        if un_caracter == validos[i]:
            es_valido = True
            break

    return es_valido

def validar_cadena_letras(texto:str) -> bool:
    """esta función utiliza la función es_letra_ascii() para que valide todas las letras de una cadena.
    Si hay una letra que no esté dentro de la colección dada en la función es_letra_ascii ya devuelve False, y si todas son validadas de manera positiva, devuelve false
    """
    es_valido = True
    for letra in texto:
        if not es_letra_ascii(letra):
            return False

    return es_valido