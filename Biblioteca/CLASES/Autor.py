class Autor():
    def __init__(self, id_autor, nombre_autor, nacionalidad, cod_pais):
        self.id_autor = id_autor
        self.nombre_autor = nombre_autor
        self.nacionalidad = nacionalidad
        self.cod_pais = cod_pais

    def obtener_datos(self):
        return {
            "ID Autor": self.id_autor,
            "Nombre Autor": self.nombre_autor,
            "Nacionalidad": self.nacionalidad,
            "Codigo Pais": self.cod_pais
             
        }

autor = Autor(1, "Gabriel García Márquez", "Colombiano", "COL")
print(autor.obtener_datos())  # Muestra los detalles en formato de diccionario
