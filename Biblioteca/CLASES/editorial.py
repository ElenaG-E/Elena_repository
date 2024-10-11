import paises

class Editorial:
    def __init__(self, id_editorial, nom_editorial, codigo_pais, telefono_contacto, email_contacto):
        self.id_editorial = id_editorial
        self.nom_editorial = nom_editorial
        super().__init__(codigo_pais)
        self.telefono_contacto = telefono_contacto
        self.email_contacto = email_contacto
    
    def validar_email(self):
        if "@" in self.__email_contacto and "." in self.__email_contacto.split("@")[-1]:
            return f"El correo '{self.__email_contacto}' es valido"
        else:
            return f"El correo '{self.__email_contacto}' es invalido"
    
    