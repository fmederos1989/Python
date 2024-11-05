try:
    archivo = open('prueba.txt', 'w', encoding='utf-8')
    archivo.write('Agregando informacion al archivo\n')
    archivo.write('Agregando mas informacion\n')
    archivo.write('Saliendo...')
except Exception as e:
    print(e)
finally:
    archivo.close()
    print('Archivo creado y cerrado correctamente.')