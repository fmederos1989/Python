from BD_Mysql.app_zona_fit.cliente import Cliente
from clienteDAO import ClienteDao

print(' Sistema de Clientes Zona Fit '.center(50, '*'))

while True:
    try:
        print('''\nMenú principal:
1. Listar Clientes
2. Agregar Cliente
3. Modificar Cliente
4. Eliminar Cliente
5. Salir''')

        opcion = int(input('Ingrese una opción: '))

        if opcion == 1:
            print('\nListado de clientes:')
            clientes = ClienteDao.listarClientes()
            for cliente in clientes:
                print(cliente)

        elif opcion == 2:
            nombre = input('Ingrese el nombre del cliente: ')
            apellido = input('Ingrese el apellido del cliente: ')
            membresia = input('Numero de membresia: ')
            clienteNuevo = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
            ClienteDao.agregarCliente(clienteNuevo)
            print(f'Cliente {clienteNuevo.nombre} {clienteNuevo.apellido} agregado correctamente con membresia {membresia}.')

        elif opcion == 3:
            id_cliente = input('Proporcione el id del cliente a modificar: ')
            nombre = input('Ingrese el nuevo nombre del cliente: ')
            apellido = input('Ingrese el nuevo apellido del cliente: ')
            membresia = input('Ingrese el nuevo número de membresia: ')
            clienteActualizar = Cliente(id_cliente, nombre, apellido, membresia)
            ClienteDao.actualizarCliente(clienteActualizar)
            print(f'Cliente {clienteActualizar} modificado correctamente.')

        elif opcion == 4:
            cliente_eliminar = input('Proporcione el id del cliente a eliminar: ')
            ClienteDao.eliminarCliente(cliente_eliminar)
            print(f'Cliente {cliente_eliminar} eliminado correctamente.')

        elif opcion == 5:
            print('Saliendo del sistema...')
            break
        else:
            print('Opción inválida.')

    except Exception as e:
        print(f'Error: {e}')
