from datetime import datetime
import paises

class Autor(paises):
    def __init__(self, id_autor, nom_autor, seudonimo_autor, cod_pais, fec_nac, fec_def, bio_autor):
        super().__init__(cod_pais)
        self.id_autor = id_autor
        self.nom_autor = nom_autor
        self.seudonimo_autor = seudonimo_autor
        self.cod_pais = cod_pais
        self.fec_nac = fec_nac
        self.fec_def = fec_def

    def control_fechas(self, fecha):
        fecha_datetime = datetime.strptime(fecha, '%d/%m/%Y')
        fecha_cadena = fecha_datetime.strftime('%Y-%m-%d')
        return fecha_cadena