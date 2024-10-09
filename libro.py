class Libro:
    def __init__(self, id, titulo, autor):
        self.__id = id
        self.__titulo = titulo
        self.__autor = autor
<<<<<<< HEAD
        self.__id = id
        self.__prestado = False

    def prestar(self):
        if not self.__prestado:
            self.__prestado = True
            return True
        return False
    
    def devolver(self):
        self.__prestado = False

class Usuario:
    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre

class Prestamo:
    def __init__(self):
        self.__prestamos = {}

    def solicitar_prestamo(self, libro, usuario):
        if libro in self.__prestamos:
            libro.devolver()
            del self.__prestamos [libro]            



    

=======
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
>>>>>>> dev
