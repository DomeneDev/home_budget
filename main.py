"""
Fichero principal del programa
"""
from budget_logic import registrar_movimiento, obtener_balance, filtar_por_categoria, eliminar_movimiento


def ejecutar_budget():
    """
    Función principal del programa
    """
    # Lista para almacenar movimientos.
    movimientos = []
    # Bucle principal
    while True:
        # Mostramos menú
        print("+-------------------------------------+")
        print("| 🏠 Presupuesto Familiar             |")
        print("+-------------------------------------+")
        print("| 1 - Añadir movimiento               |")
        print("| 2 - Filtar gasto por categoria      |")
        print("| 3 - Obtener balance                 |")
        print("| 4 - Eliminar movimiento             |")
        print("| 5 - Salir                           |")
        print("+-------------------------------------+\n")
        # Almacenamos opción del usuario
        opcion = int(input("Seleccione una opción: "))
        # Evaluamos y realizamos operación
        match opcion:
            case 1:
                concepto = input("Intoruduzca concepto: ")
                categoria = input("Introduzca categoria: ")
                cantidad = float(input("Introduzca cantidad: "))
                registrar_movimiento(
                    movimientos, concepto, categoria, cantidad)
                print(f"✍ Movimiento {concepto} anotado.\n")
            case 2:
                categoria = input("Introduzca categoria a buscar: ")
                lista_filtrada = filtar_por_categoria(movimientos, categoria)
                print("------------------------------------------------------")
                print(f"Movimientos de la categoria: {categoria.title()}")
                print("------------------------------------------------------")
                if not movimientos:
                    print(" ❌ No hay movimientos que mostrar..")
                for movimiento in lista_filtrada:
                    print(f" 👉Movimiento ID: {movimiento['id']}")
                    print(f" - Concepto: {movimiento['concepto']}.")
                    print(f" - Categoria: {movimiento['categoria']}.")
                    print(f" - Cantidad: {movimiento['cantidad']}")
                    print("------------------------------------------------------")
                print("\n")
            case 3:
                balance_movimientos = obtener_balance(movimientos)
                if balance_movimientos >= 0:
                    print(f"💰 Balance Actual: {balance_movimientos} € 🟢\n")
                else:
                    print(f"💰 Balance Actual: {balance_movimientos} € 🔴\n")
            case 4:
                id_movimiento = int(
                    input("Introduzca el ID del movimiento a eliminar: "))
                if eliminar_movimiento(movimientos, id_movimiento):
                    print(" ❌ Movimiento eliminado...")
                else:
                    print(" 📛 Movimiento no encontrado....")
            case 5:
                print("🖐 Saliendo del programa....")
                break
            case _:
                print("📛 Opción no válida")


if __name__ == "__main__":
    ejecutar_budget()
