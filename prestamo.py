from usuario import Usuario
from libro import Libro

class Prestamo:
    def __init__(self, usuario, libro, fecha):
        self.__usuario = usuario
        self.__libro = libro
        self.__fecha = fecha

    def obtener_detalle(self):
        return f"Usuario: {self.__usuario._Usuario__nombre}, Libro: {self.__libro.obtener_info()}, Fecha: {self.__fecha}"

