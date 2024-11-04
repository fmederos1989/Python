from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclado = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclado += 1
        self.id = Teclado.contador_teclado
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'Teclado -> Id: {self.id} // Marca: {self.marca} // Entrada: {self.tipo_entrada}'

# Prueba de clase

if __name__ == '__main__':
    teclado1 = Teclado('Logitech', 'USB')
    print(teclado1)
    teclado2 = Teclado('Razer', 'Bluetooth')
    print(teclado2)