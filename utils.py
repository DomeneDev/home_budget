"""
Lógica de apoyo a main
"""


def mostrar_menu():
    """
    Función para mostrar el menú
    """
    print("+-------------------------------------+")
    print("| 🏠 Presupuesto Familiar             |")
    print("+-------------------------------------+")
    print("| 1 - Añadir movimiento               |")
    print("| 2 - Filtar gasto por categoria      |")
    print("| 3 - Obtener balance                 |")
    print("| 4 - Eliminar movimiento             |")
    print("| 5 - Salir                           |")
    print("+-------------------------------------+\n")


def validar_opcion(msg_input: str, msg_error: str) -> int:
    """
    Funcion para verificar opcion de entrada

    Args:
        msg_input (str): Mensaje de input
        msg_error (str): Mensaje de error

    Return:
        (int): opcion validada
    """
    while True:
        try:
            opcion = input(msg_input)
            opcion = int(opcion)
            break
        except ValueError:
            print(msg_error)
    return opcion


def leer_cadenas(msg_imput: str, msg_error: str) -> str:
    """
    Función para verifcar el texto en formato correcto.
    Sin espacios y que no sea una cadena vacía.

    Args:
        msg_imput (str): Mensaje de input.
        msg_error (str): mensaje de error.

    Returns:
        str: texto con formato correcto.
    """
    while True:
        texto = input(msg_imput).lower()
        try:
            if not texto.strip():
                raise ValueError(msg_error)
        except ValueError as e:
            print(f"❌ ERROR: {e}")
        else:
            break
    return texto


def validacion_dato(msg_input: str, msg_error_neg: str, msg_error: str, tipo_dato: type):
    """
    Funció para validar datos

    Args:
        msg_input (str): Mensaje de input
        msg_error_neg (str): Mensaje de error, precio negativo.
        msg_error (str): Mensaje de error generico
        tipo_dato (_type_): Tipo de dato esperado.

    Returns:
        float: Dato con formato correcto de moneda
    """
    while True:
        dato = input(msg_input)
        try:
            dato = tipo_dato(dato)
            if dato < 0:
                print(msg_error_neg)
                continue
            break
        except ValueError:
            print(f"❌ ERROR: {msg_error}")
    return dato


def mostrar_movimientos(movimientos_filtrados: list, categoria: str):
    """
    Función para mostrar movimiento por categoria.

    Args:
        categoria (str): Categoria del movimiento.
        movimientos_filtrados (list): Lista de movimientos.
    """
    print("------------------------------------------------------")
    print(f"Movimientos de la categoria: {categoria.title()}")
    print("------------------------------------------------------")
    if not movimientos_filtrados:
        print(" ❌ No hay movimientos_filtrados que mostrar..")
    for movimiento in movimientos_filtrados:
        print(f" 👉Movimiento ID: {movimiento['id']}")
        print(f" - Concepto: {movimiento['concepto']}.")
        print(f" - Categoria: {movimiento['categoria']}.")
        print(f" - Cantidad: {movimiento['cantidad']}")
        print("------------------------------------------------------")
        print("\n")


def mostrar_balance(balance: float):
    """
    Función para mostar balance

    Args:
        balance (float): Resultado del balance
    """
    if balance >= 0:
        print(f"💰 Balance Actual: {balance} € 🟢\n")
    else:
        print(f"💰 Balance Actual: {balance} € 🔴\n")
