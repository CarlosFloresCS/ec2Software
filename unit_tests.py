import unittest
from implementacion import *

class TestCalculadoraDistancia(unittest.TestCase):
    def test_distancia_entre_ciudades(self):
        csv_factory = CsvFactory()
        api_factory = ApiFactory()
        mock_factory = MockFactory()

        # Caso de éxito
        calculadora = CalculadoraDistancia(csv_factory)
        distancia = calculadora.obtener_distancia('Lima', 'Peru', 'Tokyo', 'Japan')
        self.assertAlmostEqual(distancia, 15492.70138, delta=1.0)

        # Caso extremo: una ciudad no existe
        calculadora = CalculadoraDistancia(api_factory)
        with self.assertRaises(CiudadNoEncontradaError):
            distancia = calculadora.obtener_distancia('Lima', 'Peru', 'Ciudad Inexistente', 'Pais Inexistente')

        # Caso extremo: misma ciudad dos veces
        calculadora = CalculadoraDistancia(mock_factory)
        distancia = calculadora.obtener_distancia('Lima', 'Peru', 'Lima', 'Peru')
        self.assertAlmostEqual(distancia, 0.0, delta=1.0)
    
    def test_ciudad_no_encontrada(self):
        with self.assertRaises(CiudadNoEncontradaError):
            factory = ApiFactory()
            factory.obtener_coordenadas('Ciudad Inexistente', 'Pais Inexistente')

if __name__ == '__main__':
    unittest.main()
