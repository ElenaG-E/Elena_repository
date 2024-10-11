import paises
import tipousuario
from rut_chile import rut_chile

class Usuario (paises, tipousuario):
    def __init__(self, rut_usuario, nom_usuario, email_usuario, tel_usuario, codigo_pais, habilitado, id_tipo, fecha_creacion):
        self.rut_usuario = rut_usuario
        self.nom_usuario = nom_usuario
        self.email_usuario = email_usuario
        self.tel_usuario = tel_usuario
        self.codigo_pais = codigo_pais
        self.habilitado = habilitado
        self.id_tipo = id_tipo
        self.fecha_creacion = fecha_creacion

    def validar_rut(self):
        return rut_chile.is_valid_rut(self.rut_usuario)
    
    def validar_email(self):
        if "@" in self.__email_usuario and "." in self.__email_usuario.split("@")[-1]:
            return f"El correo '{self.__email_usuario}' es valido"
        else:
            return f"El correo '{self.__email_usuario}' es invalido"
