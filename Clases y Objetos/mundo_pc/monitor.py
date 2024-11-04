class Monitor:
    contador_monitor = 0

    def __init__(self, marca, tamanio):
        Monitor.contador_monitor += 1
        self.id = Monitor.contador_monitor
        self.marca = marca
        self.tamanio = tamanio

    def __str__(self):
        return f'Monitor -> Id: {self.id} // Marca: {self.marca} // Tamaño: {self.tamanio}'

# Prueba de clase

if __name__ == '__main__':
    monitor1 = Monitor('Samsung', '27"')
    print(monitor1)
    monitor2 = Monitor('Dell', '24"')
    print(monitor2)