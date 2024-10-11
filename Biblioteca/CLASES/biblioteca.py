from libro import libro

class Biblioteca:
    def __init__(self, id_biblio, nom_biblio, dir_biblio, tel_biblio):
        self.id_biblio = id_biblio
        self.nom_biblio = nom_biblio
        self.dir_biblio = dir_biblio
        self.tel_biblio = tel_biblio
        self.__libros = []
    
    def buscar_libro(self, isbn):
        for libro in self.__libros:
            if libro.isbn == isbn:
                return libro
            return None
    
    def prestar_libro(self, isbn):
        libro = self.buscar_libro(isbn)
        if libro:
            if not libro.prestado:
                libro.prestado = True
                print(f"El libro '{libro.titulo}' esta disponible")
            else:
                print(f"El libro '{libro.titulo}' no esta disponible")
        else:
            print("Libro no encontrado")

    def devolver_libro(self, isbn):
        libro = self.buscar_libro(isbn)
        if libro:
            if libro.prestado:
                libro.prestado = False
                print(f"El libro '{libro.titulo}' fue devuelto")
            else:
                print(f"El libro '{libro.titulo}' no esta devuelto")

        else:
            print("Libro no encontrado")
