print('*** Funcion Par ***')

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# LLamamos a la funcion
if __name__ == '__main__':
    numero = int(input('Proporcion un valor numerico: '))
    print(f'{numero} es par ? - {es_par(numero)}')