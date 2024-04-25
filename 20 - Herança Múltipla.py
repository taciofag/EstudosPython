# Herança Múltipla
from abc import ABC, abstractmethod

class Monitor(ABC):

    @abstractmethod
    def aumentar_claridade(self, valor):
        pass

    @abstractmethod
    def diminuir_claridade(self, valor):
        pass

class MonitorFullHD(Monitor):

    def aumentar_claridade(self, valor):
        print(f'Aumentando claridade em {valor} níveis')

    def diminuir_claridade(self, valor):
        print(f'Diminuindo claridade em {valor} níveis')

monitor = MonitorFullHD()
monitor.aumentar_claridade(8)
monitor.diminuir_claridade(5)