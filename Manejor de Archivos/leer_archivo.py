archivo = open('prueba.txt', 'r', encoding='utf8')
#print(archivo.read())

#! Leer algunos caracteres
# print(archivo.read(5))
# print(archivo.read(10))

#! Leer linea completa
# print(archivo.readline())
# print(archivo.readline())

#! Iterar cada una de las lineas
# for linea in archivo:
#     print(linea)

#! Leer todas las lineas
#print(archivo.readlines())
#print(archivo.readlines()[2])

#! Abrimos un nuevo archivo
#! a - anexar informacion
archivo2 = open('copia.txt', 'a', encoding='utf-8')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()
print('Terminamos el proceso')