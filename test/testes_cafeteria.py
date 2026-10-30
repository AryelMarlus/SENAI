import unittest
import unittest.mock as mock

from cafeteria.condimentos.leite import leite
from cafeteria.produtos_base.cafe import cafe

class TestCafeteria(unittest.TestCase):
    def test_cafeteria_interacao(self):
        cafe_personalizado = cafe()

        cafe_personalizado = leite(cafe_personalizado)
        cafe_personalizado = leite(cafe_personalizado)
        cafe_personalizado = leite(cafe_personalizado)

        self.assertEqual(cafe_personalizado.custo(), 26)

    @mock('webcam')
    def reconhecer_cafe_por_imagem_integracao_externa(self):
        simular_cafe_simples = mock
        simular_cafe_simples.retornar = {[10,30,100]}






