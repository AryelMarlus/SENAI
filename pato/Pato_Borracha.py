from voo.voar_no_way import voar_no_way


class Pato_Borracha:
    def __init__(self):
        self.Comportamento_Voo = voar_no_way()

    def voar(self) :
        self.Comportamento_Voo.voar()

    def mudar_modo_voo(self,Comportamento_Voo):
        self.Comportamento_Voo = Comportamento_Voo
