import json
from clases import HashMap


class Pokemon:
    def __init__ (self, id, nombre, tipo, poder_combate):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.poder_combate = poder_combate


Pokedex = HashMap()

Pokedex.agregar ()