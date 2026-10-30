from cafeteria.produtos_base.BebidaBase import BebidaBase

class cafe(BebidaBase):

    def descricao(self):
        return "Cafe 400ml"

    def custo(self):
        return 5

    def adocante(self):
        print("adocante")

    def adocar(self):
        print("Cafe adoçado")

    def esfriar(self):
        print("esfriar")

    def adicionar_espuma(self):
        print("adicionar_espuma")
