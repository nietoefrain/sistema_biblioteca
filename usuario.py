from libro import Libro
class Usuario:
    def __init__(self, nombre, id):
        self.__nombre = nombre
        self.__id = id
        self.__libroPrestado = []
        
    def librodefsolicitar_prestamo(self, libro):
        if not libro.esta_prestado():
            libro.prestar()  # Cambia el estado del libro a prestado
            self.__libros_prestados.append(libro)  # Añade el libro a la lista de libros prestadosreturnf'El usuario "{self.__nombre}" ha tomado prestado el libro "{libro.detalles()["Titulo"]}".'else:
            returnf'El libro "{libro.detalles()["Titulo"]}" ya está prestado y no puede ser tomado por "{self.__nombre}".'
  
  
    # def prestamo(self, libro):
    #     if not libroPrestado 
    #     Libro.prestado()