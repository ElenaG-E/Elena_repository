from datetime import datetime, timedelta
import usuario
import detallelibro

class Prestamo(detallelibro, usuario):
    def __init__(self, id_prestamo, isbn, rut_usuario, fec_prestamo, fec_devolucion, fec_devuelto, ejemplares_solicitados):
        detallelibro.__init__(self, isbn)  # Heredando ISBN de la clase detallelibro
        usuario.__init__(self, rut_usuario)  # Heredando usuario
        self.id_prestamo = id_prestamo
        self.fec_prestamo = fec_prestamo
        self.fec_devolucion = fec_devolucion
        self.fec_devuelto = fec_devuelto
        self.ejemplares_solicitados = ejemplares_solicitados

    def calcular_fechas_devolucion(self, dias_prestamo=7):
    
        if self.ejemplares_solicitados <= self.ejemplares_disponibles:
            print(f"Préstamo aceptado. Calculando fecha de devolución para {dias_prestamo} días hábiles...")
            
            # Establecer la fecha de préstamo como la actual si no está definida
            self.fec_prestamo = datetime.now() if not self.fec_prestamo else self.fec_prestamo
            
            # Inicializamos la fecha de devolución
            dias_agregados = 0
            fecha_calculada = self.fec_prestamo
            
            # Agregar solo días hábiles
            while dias_agregados < dias_prestamo:
                fecha_calculada += timedelta(days=1)
                if fecha_calculada.weekday() < 5:  # 0: Lunes, 4: Viernes (días hábiles)
                    dias_agregados += 1

            self.fec_devolucion = fecha_calculada
            print(f"Fecha de préstamo: {self.fec_prestamo.strftime('%Y-%m-%d')}")
            print(f"Fecha de devolución: {self.fec_devolucion.strftime('%Y-%m-%d')}")
        else:
            print(f"No hay suficientes ejemplares disponibles. Solicitaste {self.ejemplares_solicitados}, pero solo hay {self.ejemplares_disponibles} disponibles.")

    def actualizar_disponibilidad_prestamo(self):
        """
        Método para actualizar la disponibilidad de ejemplares tras realizar un préstamo.
        """
        if self.ejemplares_solicitados <= self.ejemplares_disponibles:
            self.ejemplares_disponibles -= self.ejemplares_solicitados
            print(f"Préstamo realizado. Ejemplares solicitados: {self.ejemplares_solicitados}. Ejemplares disponibles ahora: {self.ejemplares_disponibles}")
        else:
            print(f"No se pudo realizar el préstamo. Solo hay {self.ejemplares_disponibles} ejemplares disponibles.")

    def actualizar_disponibilidad_devolucion(self, ejemplares_devueltos):
        """
        Método para actualizar la disponibilidad de ejemplares tras la devolución.
        """
        if ejemplares_devueltos <= self.ejemplares_solicitados:
            self.ejemplares_disponibles += ejemplares_devueltos
            print(f"Devolución realizada. Ejemplares devueltos: {ejemplares_devueltos}. Ejemplares disponibles ahora: {self.ejemplares_disponibles}")
        else:
            print(f"No se puede devolver más de lo prestado. Se solicitaron {self.ejemplares_solicitados}, intentaste devolver {ejemplares_devueltos}.")