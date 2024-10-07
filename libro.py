class libro:    
    def __init__(self, titulo, autor, id):
        self.__titulo = titulo
        self.__autor = autor
        self.__id = id
        self.__prestado = False