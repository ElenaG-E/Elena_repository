class Tipo_Categoria():
    def __init__(self, id_tipcat, nom_tipcat):
        self.id_tipcat = id_tipcat
        self.nom_tipcat = nom_tipcat

    def __str__(self):
        """Representación en cadena del tipo de categoría."""
        return f"Tipo de categoría: {self.nom_tipcat} (ID: {self.id_tipcat})"

    def obtener_detalles(self):
        """Devuelve los detalles del tipo de categoría."""
        return f"ID: {self.id_tipcat}, Nombre: {self.nom_tipcat}"
