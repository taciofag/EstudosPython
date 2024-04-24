# Criar métodos Ligar, Desligar e exibir

class Computador:
    sistema_operacional = 'Windows 10' #quando há um padrão
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa = placa_de_video

    def ligar(self):
        print('Estou ligando o computador')

Computador.sistema_operacional = 'Mac OS'
# variável em marca
computador = Computador('Dell', '8GB', 'RX5800')
computador.marca = 'Asus'
print(computador.marca)
print(computador.sistema_operacional)
