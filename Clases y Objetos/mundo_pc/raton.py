from dispositivo_entrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones += 1
        self.id = Raton.contador_ratones
        # self.marca = marca
        # self.tipo_entrada = tipo_entrada
        super().__init__(marca, tipo_entrada)   #Utiliza el constructor del padre heredando

    def __str__(self):
        return f'Raton -> Id: {self.id} // Marca: {self.marca} // Entrada: {self.tipo_entrada}'

# Prueba de la clase

if __name__ == '__main__':
    raton1 = Raton('Logitech', 'USB')
    print(raton1)
    raton2 = Raton('Razer', 'Bluetooth')
    print(raton2)


