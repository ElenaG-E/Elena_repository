import libro
import editorial

class Detalle_libro(libro, editorial):
    def __init__(self, id_detalle, isbn, fec_edicion, id_editorial, paginas, id_catlib, id_cantidad, disponibles):
        self.id_detalle = id_detalle
        self.isbn = isbn
        self.fec_edicion = fec_edicion
        self.id_editorial = id_editorial
        self.paginas = paginas
        self.id_catlib = id_catlib
        self.id_cantidad = id_cantidad
        self.disponibles = disponibles

    def gestionar_ejemplares(self, accion, cantidad):
        """
        Método para gestionar la cantidad de ejemplares de un libro.
        Acciones posibles: "retirar", "devolver", "añadir".
        """
        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0.")
            return

        if accion == "retirar":
            if cantidad <= self.ejemplares_disponibles:
                self.ejemplares_disponibles -= cantidad
                print(f"Se han retirado {cantidad} ejemplar(es). Ejemplares disponibles ahora: {self.ejemplares_disponibles}")
            else:
                print(f"No es posible retirar {cantidad} ejemplar(es). Solo hay {self.ejemplares_disponibles} disponibles.")
        
        elif accion == "devolver":
            if self.ejemplares_disponibles + cantidad <= self.cantidad_ejemplares:
                self.ejemplares_disponibles += cantidad
                print(f"Se han devuelto {cantidad} ejemplar(es). Ejemplares disponibles ahora: {self.ejemplares_disponibles}")
            else:
                print(f"No se puede devolver más de lo que tenemos. Ejemplares disponibles: {self.ejemplares_disponibles}, Total permitidos: {self.cantidad_ejemplares}")
        
        elif accion == "añadir":
            self.cantidad_ejemplares += cantidad
            self.ejemplares_disponibles += cantidad
            print(f"Se han añadido {cantidad} ejemplar(es). Ahora hay {self.cantidad_ejemplares} en total y {self.ejemplares_disponibles} disponibles.")
        
        else:
            print(f"Acción '{accion}' no reconocida. Utilice 'retirar', 'devolver' o 'añadir'.")
