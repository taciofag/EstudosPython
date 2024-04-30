# Criar métodos Ligar, Desligar e exibir

class Computador:
    sistema_operacional = 'Windows 10'  # quando há um padrão

    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa = placa_de_video

    def exibir_dados_do_computador(self):
        print(self.marca, self.memoria_ram,
              self.placa, self.sistema_operacional)
    
    # cls é para passar a classe inteira como parâmetro
    @classmethod
    def computador_escritorio(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de Vídeo - Baixo Custo')


    @classmethod
    def computador_trabalho_pesado(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de Vídeo - Pesada')


Computador2 = Computador.computador_escritorio('8GB')


Computador3 = Computador.computador_trabalho_pesado('18GB')
Computador2.exibir_dados_do_computador()
print('###################')
Computador3.exibir_dados_do_computador()