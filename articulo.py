class Articulo:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion

    def toDBCollection(self):
        return{
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion
        }