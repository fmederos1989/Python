from manejo_archivo import ManejoArchivos

#! con with cierra el archivo atomaticamente
# # with open('prueba.txt', 'r', encoding='utf8') as archivo:
#     print(archivo.read())

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())