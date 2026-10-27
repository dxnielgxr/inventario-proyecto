inventario = {
    "manzanas": 50,
    "peras": 30,
    "uvas": 20
}

def pedir_cantidad(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print("La cantidad debe ser mayor que cero.")
                continue
            return valor
        except ValueError:
            print("Entrada no válida. Ingrese un número entero.")

while True:
    print("\n=== Inventario ===")
    print("1. Ver inventario")
    print("2. Agregar producto")
    print("3. Vender producto")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ").strip()

    if opcion == "1":
        if not inventario:
            print("El inventario está vacío.")
        else:
            for producto, cantidad in inventario.items():
                print(f"{producto}: {cantidad}")

    elif opcion == "2":
        producto = input("Ingrese el nombre del producto: ").strip().lower()
        if not producto:
            print("El nombre no puede estar vacío.")
            continue
        cantidad = pedir_cantidad("Ingrese la cantidad a agregar: ")
        inventario[producto] = inventario.get(producto, 0) + cantidad
        print(f"Ahora hay {inventario[producto]} de {producto}.")

    elif opcion == "3":
        producto = input("Ingrese el nombre del producto: ").strip().lower()
        if producto not in inventario:
            print("Ese producto no existe en el inventario.")
            continue
        cantidad = pedir_cantidad("Ingrese la cantidad a vender: ")
        if cantidad > inventario[producto]:
            print(f"Stock insuficiente. Solo quedan {inventario[producto]}.")
        else:
            inventario[producto] -= cantidad
            print(f"Venta realizada. Quedan {inventario[producto]} de {producto}.")

    elif opcion == "4":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Elija un número del 1 al 4.")