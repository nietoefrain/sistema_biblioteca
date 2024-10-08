class Libro:
    def __init__(self, id, titulo, autor):
        self.__id = id
        self.__titulo = titulo
        self.__autor = autor
        self.__disponible = True

    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            return True
        return False

    def devolver(self):
        self.__disponible = True

    def esta_disponible(self):
        return self.__disponible

    def obtener_info(self):
        return f"ID: {self.__id}, Título: {self.__titulo}, Autor: {self.__autor}"