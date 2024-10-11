from datetime import datetime
import paises

class autor(paises):
    def __init__(self, id_autor, nom_autor, seud_autor, cod_pais, fec_nac, fec_def):
        super().__init__(cod_pais)
        self.id_autor = id_autor
        self.nom_autor = nom_autor
        self.seud_autor = seud_autor
        self.cod_pais = cod_pais
        self.fec_nac = fec_nac
        self.fec_def = fec_def
    
    def control_de_fechas(fecha):
        fecha_datetime = datetime.strptime(fecha, "%d/%m/%Y")
        fecha_string = fecha_datetime.strftime("%Y-%m-%d")
        return fecha_string