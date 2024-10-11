import isbnlib #Descargue e importe esta librería de python.
import autor

class Libro():
    def __init__(self, titulo, isbn, id_autor):
        super().__init__(id_autor) #Porque la clase libro es una herencia de la clase autor.
        self.titulo = titulo #atributo.
        self.isbn = isbn #atributo.

    def validar_isbn(self): #Método que cree para validar el isbn.
        return isbnlib.is_isbn10(self.isbn) or isbnlib.is_isbn13(self.isbn)
    
isbn = input("Ingresa número ISBN: ")
libro = Libro("Ejemplo de Título", isbn, 1)
valido = libro.validar_isbn()
print(f"El ISBN es {'válido' if valido else 'inválido'}")
