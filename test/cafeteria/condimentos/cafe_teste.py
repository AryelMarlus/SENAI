import unittest
from io import StringIO
from contextlib import redirect_stdout

from cafeteria.produtos_base.cafe import cafe

class TestCafe(unittest.TestCase):

    def setUp(self):
        self.cafe = cafe()


    def test_descricao(self):
        self.assertEqual(
            self.cafe.descricao(),
            "Cafe 400ml"
        )

    def test_custo(self):
        self.assertEqual(
            self.cafe.custo(),
            5
        )

    def test_adocante(self):
        with redirect_stdout(StringIO()) as saida:
            self.cafe.adocante()

        self.assertEqual(
            saida.getvalue(),
            "adocante\n"
        )

    def test_adocar(self):
        with redirect_stdout(StringIO()) as saida:
            self.cafe.adocar()

        self.assertEqual(
            saida.getvalue(),
            "Cafe adoçado\n"
        )

    def test_esfriar(self):
        with redirect_stdout(StringIO()) as saida:
            self.cafe.esfriar()

        self.assertEqual(
            saida.getvalue(),
            "esfriar\n"
        )


if __name__ == "__main__":
    unittest.main()
