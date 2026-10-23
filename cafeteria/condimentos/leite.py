from cafeteria.condimentos.Adcionais import Adicionais


class leite(Adicionais):

    def descricao(self):
        return self.bebida.descricao() + ", leite"

    def custo(self):
        return self.bebida.custo() + 5