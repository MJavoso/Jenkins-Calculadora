import unittest
from calculadora import Calculadora


class TestCalculadora(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass')
    
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        self.calc = Calculadora()
        print('setUp')
    
    def tearDown(self):
        print('tearDown')
    
    def test_sumar_dos_mas_dos(self):
        # AAA

        # Arrange
        # Act
        resultado = self.calc.sumar(2, 2)
        # Assert
        self.assertEqual(4, resultado)
    
    def test_cinco_mas_tres(self):
        resultado = self.calc.sumar(5, 3)
        self.assertEqual(8, resultado)
    
    def test_sumar_string_falla(self):
        resultado = self.calc.sumar('f', 2)
        self.assertEqual('Sólo se admiten números', resultado)
    
    def test_sumar_string2_falla(self):
        resultado = self.calc.sumar(5, 'xd')
        self.assertEqual('Sólo se admiten números', resultado)
    
    def test_sumar_negativos_falla(self):
        resultado = self.calc.sumar(-4, 6)
        self.assertEqual('Solo se admiten números positivos', resultado)

    def test_sumar_negativos2_falla(self):
        resultado = self.calc.sumar(4, -6)
        self.assertEqual('Solo se admiten números positivos', resultado)

    def test_sumar_decimales_falla(self):
        resultado = self.calc.sumar(4.5, 6)
        self.assertEqual('Solo se admiten números enteros positivos', resultado)
    
    def test_sumar_decimales_falla(self):
        resultado = self.calc.sumar(4, 9.9)
        self.assertEqual('Solo se admiten números enteros positivos', resultado)
    
    def test_restar_ocho_menos_cinco(self):
        resultado = self.calc.restar(8, 5)
        self.assertEqual(3, resultado)

if __name__ == '__main__':
    unittest.main()
