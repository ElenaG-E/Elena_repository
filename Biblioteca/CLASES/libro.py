import autor
import isbnlib  

class libro:
    def __init__(self, titulo, isbn, id_autor):
        super().__init__(id_autor)
        self.titulo = titulo  # Atributo título
        self.isbn = isbn  # Atributo ISBN
        self.id_autor = id_autor  # Atributo para almacenar el ID del autor

    def validar_isbn(self):
        """Valida si el isbn es correcto (10 o 13 dígitos)."""
        return isbnlib.is_isbn10(self.isbn) or isbnlib.is_isbn13(self.isbn)
    
# Solicitar el isbn al usuario
isbn = input("Ingresa número isbn: ")
libro = libro("Ejemplo de Título", isbn, 1)  # Instanciar el libro
valido = libro.validar_isbn()  # Validar el isbn

# Imprimir el resultado de la validación
print(f"El isbn es {'válido' if valido else 'inválido'}")

