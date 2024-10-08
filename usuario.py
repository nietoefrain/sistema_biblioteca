from libro import Libro

class Usuario:
    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre
        self.__prestamos = []

    def solicitar_prestamo(self, libro):
        if libro.prestar():
            self.__prestamos.append(libro)
            return True
        return False

    def devolver_libro(self, libro):
        if libro in self.__prestamos:
            libro.devolver()
            self.__prestamos.remove(libro)
            return True
        return False

    def obtener_prestamos(self):
        return [libro.obtener_info() for libro in self.__prestamos]