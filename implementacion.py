import requests
import csv
from math import radians, sin, cos, sqrt, atan2

class Coordenadas:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud

class CoordenadasFactory:
    def obtener_coordenadas(self, ciudad, pais):
        pass

class CsvFactory(CoordenadasFactory):
    def obtener_coordenadas(self, ciudad, pais):
        with open('worldcities.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['city_ascii'].lower() == ciudad.lower() and row['country'].lower() == pais.lower():
                    return Coordenadas(float(row['lat']), float(row['lng']))
        return None

class ApiFactory(CoordenadasFactory):
    def obtener_coordenadas(self, ciudad, pais):
        url = f'https://nominatim.openstreetmap.org/search?q={ciudad},{pais}&format=json'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if len(data) > 0:
                return Coordenadas(float(data[0]['lat']), float(data[0]['lon']))
        return None

class MockFactory(CoordenadasFactory):
    def obtener_coordenadas(self, ciudad, pais):
        return Coordenadas(0, 0)

class CalculadoraDistancia:
    def __init__(self, factory: CoordenadasFactory):
        self.factory = factory

    def obtener_distancia(self, ciudad1, pais1, ciudad2, pais2):
        coordenadas1 = self.factory.obtener_coordenadas(ciudad1, pais1)
        coordenadas2 = self.factory.obtener_coordenadas(ciudad2, pais2)
        if coordenadas1 is None or coordenadas2 is None:
            return None
        else:
            return self.calcular_distancia(coordenadas1, coordenadas2)

    def calcular_distancia(self, coordenadas1, coordenadas2):
        R = 6371  # Radio de la Tierra en km
        lat1, lon1 = radians(coordenadas1.latitud), radians(coordenadas1.longitud)
        lat2, lon2 = radians(coordenadas2.latitud), radians(coordenadas2.longitud)
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distancia = R * c
        return distancia