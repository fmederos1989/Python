from usuario_dao import UsuarioDAO
from usuario import Usuario

print(' Sistema de gestion de usuarios '.center(50, '-'))

while True:
    print('''
    Menu Principal:
    1. Listar usuarios
    2. Agregar usuario
    3. Editar usuario
    4. Eliminar usuario
    5. Salir
    ''')

    try:
        opcion = int(input('Ingrese una opcion: '))

        if opcion == 1:
            print('Listado de usuarios:')
            for usuario in UsuarioDAO.seleccionar():
                print(usuario)
        elif opcion == 2:
            username = input('Proporcionar username: ')
            password = input('Ingresar password: ')
            usuario_nuevo = Usuario(username=username, password=password)
            UsuarioDAO.insertar(usuario_nuevo)
            print('Usuario agregado correctamente.')
        elif opcion == 3:
            usuario_id = int(input('Ingrese el ID del usuario a editar: '))
            username = input('Ingresar nuevo username: ')
            password = input('Ingresar nuevo password: ')
            usuario_a_editar = Usuario(id_usuario=usuario_id, username=username, password=password)
            UsuarioDAO.actualizar(usuario_a_editar)
            print('Usuario editado correctamente.')
        elif opcion == 4:
            usuario_eliminar = int(input('Ingrese el ID del usuario a eliminar: '))
            print('Esta seguro de eliminar el usuario?')
            confirmar = input('Ingrese "s" para confirmar: ').lower()
            if confirmar =='s':
                UsuarioDAO.eliminar(usuario_eliminar)
                print('Usuario eliminado correctamente.')
            else:
                print('Acción cancelada.')
        elif opcion == 5:
            print('Saliendo del sistema...')
            break
        else:
            print('Option invalida.')
    except Exception as e:
        print('Error:', e)

