from libro import Libro
from usuario import Usuario
from prestamo import Prestamo

#Lista de Libros
libro1 = Libro(1, "Cien Años de Soledad", "Gabriel García Márquez")
libro2 = Libro(2, "Don Quijote de la Mancha", "Miguel de Cervantes")
libro3 = Libro(3, "1984", "George Orwell")
libro4 = Libro(4, "Crimen y Castigo", "Fiódor Dostoyevski")
libro5 = Libro(5, "Matar a un Ruiseñor", "Harper Lee")
libro6 = Libro(6, "El Amor en los Tiempos del Cólera", "Gabriel García Márquez")
libro7 = Libro(7, "Rayuela", "Julio Cortázar")
libro8 = Libro(8, "Orgullo y Prejuicio", "Jane Austen")
libro9 = Libro(9, "La Odisea", "Homero")
libro10 = Libro(10, "El Gran Gatsby", "F. Scott Fitzgerald")

#Lista de Usuarios
Usuario(1, "Juan Pérez")
Usuario(2, "Juan Silva")
Usuario(3, "Carlos Mamani")
Usuario(4, "Diego Aedo")
Usuario(5, "Genesis Marcano")


def menu():
    while True:
        try:
            print("Bienvenido al sistema de administracion de biblioteca")
            print("Selecciona una de las opciones:")
            print("1. Solicitar prestamo de libros")
            opcion = input("Selecciona una opcion: ")
            
        except ValueError:
            print("Error: Entrada no válida. Por favor, ingrese un número para seleccionar una opción.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

menu()