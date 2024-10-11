from autor import autor
import isbnlib  

class libro:
    def __init__(self, titulo, isbn, id_autor):
        super().__init__(id_autor)
        self.titulo = titulo  # Atributo título
        self.isbn = isbn  # Atributo ISBN
        self.id_autor = id_autor  # Atributo para almacenar el ID del autor

    def validar_isbn(self):
        """Valida si el ISBN es correcto (10 o 13 dígitos)."""
        return isbnlib.is_isbn10(self.isbn) or isbnlib.is_isbn13(self.isbn)
    
    from libro import libro
import isbnlib

# Solicitar el ISBN al usuario
isbn = input("Ingresa número ISBN: ")
libro = libro("Ejemplo de Título", isbn, 1)  # Instanciar el libro
valido = libro.validar_isbn()  # Validar el ISBN

# Imprimir el resultado de la validación
print(f"El ISBN es {'válido' if valido else 'inválido'}")

