class Editorial:
    def __init__(self, id_editorial, nom_editorial, codigo_pais, telefono_contacto, correo_contacto):
        self.id_editorial = id_editorial
        self.nom_editorial = nom_editorial
        self.codigo_pais = codigo_pais
        self.telefono_contacto = telefono_contacto
        self.correo_contacto = correo_contacto
    
    def validar_correo(self):
        if "@" in self.__correo_contacto and "." in self.__correo_contacto.split("@")[-1]:
            return f"El correo '{self.__correo_contacto}' es valido"
        else:
            return f"El correo '{self.__correo_contacto}' es invalido"
    
    def cambiar_correo(self, nuevo_correo):
        self.nuevo_correo = nuevo_correo
        return self.validar_correo()
    