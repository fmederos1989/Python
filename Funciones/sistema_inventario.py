print('*** Sistema de Inventario ***')

inventario = [
    {
        'id': 1,
        'nombre': 'Camisa',
        'precio': 100,
        'stock': 50
    },
    {
        'id': 2,
        'nombre': 'Pantalon',
        'precio': 200,
        'stock': 30
    }
]

def agregar_producto():
    nombre = input('Ingrese el nombre del producto: ')
    precio = float(input('Ingrese el precio del producto: '))
    stock = int(input('Ingrese el stock del producto: '))

    nuevo_producto = {
        'id': len(inventario) + 1,
        'nombre': nombre,
        'precio': precio,
        'stock': stock
    }

    inventario.append(nuevo_producto)
    print('Producto agregado con éxito.')


def listar_productos():
    print('\n*** Listado de Productos ***\n')
    for producto in inventario:
        print(f'ID: {producto["id"]}, Nombre: {producto["nombre"]}, Precio: ${producto["precio"]}, Stock: {producto["stock"]}')

def buscar_product(id):
    for producto in inventario:
        if producto['id'] == id:
            print(f'''Producto encontrado:
            ID: {producto["id"]}, Nombre: {producto["nombre"]}, Precio: ${producto["precio"]}, Stock: {producto["stock"]}''')
            return
        else:
            print('Producto no encontrado.')
            return

def eliminar_product():
    id_eliminar = int(input('Ingrese el ID del producto a eliminar: '))
    for i, producto in enumerate(inventario):
        if producto['id'] == id_eliminar:
            inventario.pop(i)
            print('Producto eliminado con éxito.')
            return
    print('Producto no encontrado.')
    return

opcion = None

while opcion != 5:
    print('\n--- Menú ---')
    print('1. Agregar producto')
    print('2. Listar productos')
    print('3. Buscar producto por id')
    print('4. Eliminar producto')
    print('5. Salir')

    opcion = int(input('Ingrese la opción: '))

    if opcion == 1:
        agregar_producto()
    elif opcion == 2:
        listar_productos()
    elif opcion == 3:
        id_buscar = int(input('Ingrese el ID del producto a buscar: '))
        buscar_product(id_buscar)
    elif opcion == 4:
        eliminar_product()
    elif opcion == 5:
        print('Saliendo del sistema...')
    else:
        print('Opción inválida.')
