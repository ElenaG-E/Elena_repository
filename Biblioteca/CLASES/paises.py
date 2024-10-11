class Paises():
    def __init__(self, codigo_pais, codigo_iso3_pais, nombre_pais, gentilicio_pais):
        self.codigo_pais = codigo_pais
        self.codigo_iso3_pais = codigo_iso3_pais
        self.nombre_pais = nombre_pais
        self.gentilicio_pais = gentilicio_pais
    
    def obtener_detalles(self):
        """Devuelve los detalles del país."""
        return (f"Código: {self.codigo_pais}, ISO3: {self.codigo_iso3_pais}, "
                f"Nombre: {self.nombre_pais}, Gentilicio: {self.gentilicio_pais}")