import Tipo_categoria

class Categoria_libros(Tipo_categoria):
    def __init__(self, id_catlib, id_tipcat, cat_lib):
        super().__init__(id_tipcat)
        self.id_catlib = id_catlib
        self.cat_lib = cat_lib
    
    def obtener_detalles(self):
        """Devuelve los detalles completos de la categoría de libro."""
        detalles_tipo = super().__str__()  # Llamada al método de la clase padre
        detalles_categoria = (f"ID categoría: {self.id_catlib}, "
                              f"Nombre categoría: {self.cat_lib} ")
        return f"{detalles_categoria}\n{detalles_tipo}"
    