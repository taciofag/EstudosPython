
def exibir_informacoes_do_computador():
    marca = input('Digite a marca do seu computador: ')
    memoria = input('Quantidade de memória ram: ')
    placa = input('placa de vídeo: ')

    print(f'Seu computador é da marca {marca}')
    print(f'Seu computador tem {memoria} GB de RAM')
    print(f'A sua placa de vídeo é {placa}')


exibir_informacoes_do_computador()

class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa = placa_de_video
    def ligar(self)


computador1 = Computador('Asus', '16', 'NVIDIA')
print(computador1.marca, computador1.memoria_ram, computador1.placa)