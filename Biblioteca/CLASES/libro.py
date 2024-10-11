import isbnlib

class Libro():
    def __init__(self, titulo, isbn, id_autor):
        self.titulo = titulo
        self.isbn = isbn
        self.id_autor = id_autor

    def validar_isbn(self):
        return isbnlib.is_isbn10(self.isbn) or isbnlib.is_isbn13(self.isbn)
    
isbn = input("Ingresa número ISBN: ")
libro = Libro("Ejemplo de Título", isbn, 1)
valido = libro.validar_isbn()
print(f"El ISBN es {'válido' if valido else 'inválido'}")
