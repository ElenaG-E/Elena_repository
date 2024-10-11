from paises import codigo_pais

class Autor():
    def __init__(self, id_autor, nombre_autor, nacionalidad, codigo_pais):
        super().__init__(codigo_pais) 
        self.id_autor = id_autor
        self.nombre_autor = nombre_autor
        self.nacionalidad = nacionalidad
        

    def obtener_datos(self):
        return {
            "ID Autor": self.id_autor,
            "Nombre Autor": self.nombre_autor,
            "Nacionalidad": self.nacionalidad,
            "Codigo Pais": self.codigo_pais
        }
