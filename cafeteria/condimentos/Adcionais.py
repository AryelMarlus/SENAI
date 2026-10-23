from abc import ABC, abstractmethod

from cafeteria.produtos_base.BebidaBase import BebidaBase


class Adicionais(BebidaBase, ABC):

    @abstractmethod
    def descricao(self):
        pass

    @abstractmethod
    def custo(self):
        pass

    def __init__(self, bebida):
        self.bebida = bebida