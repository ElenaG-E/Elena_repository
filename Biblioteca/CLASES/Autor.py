import paises

class Autor():
    def __init__(self, id_autor, nombre_autor, nacionalidad, codigo_pais):
        self.id_autor = id_autor
        self.nombre_autor = nombre_autor
        self.nacionalidad = nacionalidad
        self.codigo_pais = codigo_pais

    def obtener_datos(self):
        return {
            "ID Autor": self.id_autor,
            "Nombre Autor": self.nombre_autor,
            "Nacionalidad": self.nacionalidad,
            "Codigo Pais": self.codigo_pais
             
        }

autor = Autor(1, "Gabriel García Márquez", "Colombiano", "COL")
print(autor.obtener_datos())  # Muestra los detalles en formato de diccionario
