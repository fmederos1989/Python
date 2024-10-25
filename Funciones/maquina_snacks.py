print('*** Maquina de Snacks ***')

# Inicializamos el inventario
inventario = [
    {
        'id': 1,
        'nombre': 'Papitas',
        'precio': 50,
        'stock': 100
    },
    {
        'id': 2,
        'nombre': 'Chocolates',
        'precio': 75,
        'stock': 80
    },
    {
        'id': 3,
        'nombre': 'Gaseosa',
        'precio': 100,
        'stock': 60
    }
]

# Inicializamos la lista de compra equivalente a un carrito de compras en un e-commerce
lista_compra = []

def listar_snacks():
    print('\n*** Articulos disponibles ***')
    for snack in inventario:
        print(f'ID: {snack["id"]} -> {snack["nombre"]} - Precio: ${snack["precio"]} - Stock: {snack["stock"]}')

def comprar_snack():
    id_snack = int(input('Ingrese el ID del snack a comprar: '))
    for snack in inventario:
        if snack['id'] == id_snack:
            cantidad = int(input('Ingrese la cantidad a comprar: '))
            if snack['stock'] >= cantidad:
                snack['stock'] -= cantidad
                print(f'Compra exitosa! Se han agregado {cantidad} unidades de {snack["nombre"]} al carrito.')
                articulo_agregar = {
                    'id': snack['id'],
                    'nombre': snack['nombre'],
                    'precio': snack['precio'],
                    'cantidad': cantidad,
                    'subtotal': snack['precio'] * cantidad,
                }
                lista_compra.append(articulo_agregar)
                return
            elif snack['stock'] <= cantidad:
                print('No hay suficiente stock.')
                return
    print('ID de snack invalido.')
    return


def mostrar_ticket():
    if len(lista_compra) == 0:
        print('El carrito esta vacio.')
        return
    else:
        print('\n--- Ticket ---')
        for snack in lista_compra:
            print(f'{snack["nombre"]} - ${snack["precio"]} - {snack["cantidad"]} unidades - Subtotal: ${snack["subtotal"]}')
        print(f'Total: ${sum(snack["precio"] * snack["cantidad"] for snack in lista_compra)}')
        print('Gracias por su compra!')
        print('--- Fin Ticket ---')

if __name__ == "__main__":

    while True:
        print('\n--- Menu ---')
        print('1. Listar snacks')
        print('2. Comprar snack')
        print('3. Mostar Ticket')
        print('4. Compra Nueva')
        print('5. Salir')

        opcion = int(input('Ingrese la opcion: '))

        if opcion == 1:
            listar_snacks()
        elif opcion == 2:
            comprar_snack()
        elif opcion == 3:
            mostrar_ticket()
        elif opcion == 4:
            lista_compra.clear()
            print('Carrito vacio, compra nueva iniciada.')
        elif opcion == 5:
            print('Saliendo del programa...')
            break
        else:
            print('Opcion invalida.')