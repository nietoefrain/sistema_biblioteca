class Libro:    
    def __init__(self, titulo, autor, id):
        self.__titulo = titulo
        self.__autor = autor
        self.__id = id
        self.__prestado = False

    def prestar(self):
        if not self.__prestado:
            self.__prestado = True
            return False
        
