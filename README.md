# Inventario en Python

Programa de consola para gestionar el inventario de una tienda desde un menú numerado. Usa un bucle `while` para mantener el programa activo hasta que el usuario elija salir, y `try/except` para validar los datos sin que el programa se cierre.

## Características

- Ver todos los productos con su cantidad en stock
- Agregar productos nuevos o sumar stock a uno existente
- Vender productos con control de stock:
  - Avisa si el producto no existe
  - Avisa si no hay stock suficiente e indica cuánto queda
- Los nombres no distinguen mayúsculas ni espacios extra (`Manzanas` y `manzanas` son el mismo producto)
- Función `pedir_cantidad` que valida las cantidades:
  - Rechaza texto que no sea un número entero (`ValueError`)
  - Rechaza ceros y valores negativos
  - Vuelve a pedir solo el dato inválido, sin reiniciar el programa
- Confirmaciones al agregar y vender
- Aviso cuando se elige una opción que no existe

## Inventario inicial

El programa arranca con estos productos:

| Producto | Cantidad |
|---|---|
| manzanas | 50 |
| peras | 30 |
| uvas | 20 |

Puedes modificarlos al inicio del código, en el diccionario `inventario`.

## Requisitos

- Python 3.8 o superior

## Cómo ejecutarlo

1. Clona el repositorio:

   ```bash
   git clone https://github.com/dxnielgxr/inventario-proyecto.git
   cd nombre-del-repo
   ```

2. Ejecuta el programa:

   ```bash
   python inventario.py
   ```

## Ejemplo de uso

```
=== Inventario ===
1. Ver inventario
2. Agregar producto
3. Vender producto
4. Salir
Seleccione una opción (1-4): 3
Ingrese el nombre del producto: kiwis
Ese producto no existe en el inventario.

=== Inventario ===
1. Ver inventario
2. Agregar producto
3. Vender producto
4. Salir
Seleccione una opción (1-4): 3
Ingrese el nombre del producto: Manzanas
Ingrese la cantidad a vender: abc
Entrada no válida. Ingrese un número entero.
Ingrese la cantidad a vender: 60
Stock insuficiente. Solo quedan 50.

=== Inventario ===
1. Ver inventario
2. Agregar producto
3. Vender producto
4. Salir
Seleccione una opción (1-4): 3
Ingrese el nombre del producto: manzanas
Ingrese la cantidad a vender: 10
Venta realizada. Quedan 40 de manzanas.

=== Inventario ===
1. Ver inventario
2. Agregar producto
3. Vender producto
4. Salir
Seleccione una opción (1-4): 4
Saliendo del programa.
```

## Limitaciones

El inventario se guarda solo en memoria, por lo que los cambios se pierden al cerrar el programa.

## Mejoras futuras

- Guardar el inventario en un archivo `json` para que persista
- Eliminar automáticamente los productos que lleguen a cero
- Agregar precios y calcular el total de ventas

## Conceptos que practica

- Diccionarios y el método `.get()`
- Funciones y validación de entradas
- Bucles `while` con `break` y `continue`
- Manejo de excepciones con `try` y `except`
- Condicionales `if`, `elif` y `else`
- Métodos de texto: `.strip()` y `.lower()`

## Autor

dxnielgxr