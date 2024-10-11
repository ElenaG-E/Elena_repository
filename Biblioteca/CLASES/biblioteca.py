from libro import libro, isbn, 

class Biblioteca():
    def __init__(self, id_biblio, nom_biblio, dir_biblio, tel_biblio):
        self.id_biblio = id_biblio
        self.nom_biblio = nom_biblio
        self.dir_biblio = dir_biblio
        self.tel_biblio = tel_biblio
        self.libros = []
        
    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_libro(self, identificar):
         for libro in self.libros:
            if libro.isbn == identificar:
                return libro
            return None

    def prestar_libro(self):
       libro = self.buscar_libro(isbn)
       if libro:
           if libro.disponible:
               libro.disponible = False
               return f"El libro '{libro, titulo}' ha sido prestado"

    def devolver_libro(self):
        pass


