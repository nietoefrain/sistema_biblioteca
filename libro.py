class libro:    
    def __init__(self, titulo, autor, id):
        self.__titulo = titulo
        self.__autor = autor
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



    

