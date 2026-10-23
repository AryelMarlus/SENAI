from voo import Comportamento_Voo

class Pato:
    def __init__(self, Comportamento_Voo):
        self.comportamento_voo = Comportamento_Voo

    def voar(self):
        self.comportamento_voo.voar()

    def mudar_modo_voo(self, Comportamento_Voo):
        self.comportamento_voo = Comportamento_Voo
