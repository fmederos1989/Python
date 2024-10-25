print('*** Alcance de variables ***')

contador_global = 0

def incrementar_contador():
    # declaramos una variable local
    contador_local = 0
    # usamos la variable global
    global contador_global
    # incrementamos la variable global
    contador_global += 1
    # incrementamos la variable local
    contador_local += 1

    print(f'Contador global: {contador_global}')
    print(f'Contador local: {contador_local}\n')

# llamamos a la función 3 veces
incrementar_contador()
incrementar_contador()
incrementar_contador()
