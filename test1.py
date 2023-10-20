from implementacion import *

ciudades = [
    ('Lima', 'Peru'),
    ('Tokyo', 'Japan'),
    ('New York', 'United States'),
    ('Paris', 'France'),
    ('Sydney', 'Australia')
]

csv_factory = CsvFactory()
api_factory = ApiFactory()
mock_factory = MockFactory()

for ciudad1, pais1 in ciudades:
    for ciudad2, pais2 in ciudades:
        calculadora = CalculadoraDistancia(csv_factory)
        distancia = calculadora.obtener_distancia(ciudad1, pais1, ciudad2, pais2)
        print(f'Distancia entre {ciudad1} y {ciudad2} (CSV): {distancia} km')

        calculadora = CalculadoraDistancia(api_factory)
        distancia = calculadora.obtener_distancia(ciudad1, pais1, ciudad2, pais2)
        print(f'Distancia entre {ciudad1} y {ciudad2} (API): {distancia} km')

        calculadora = CalculadoraDistancia(mock_factory)
        distancia = calculadora.obtener_distancia(ciudad1, pais1, ciudad2, pais2)
        print(f'Distancia entre {ciudad1} y {ciudad2} (Mock): {distancia} km')
