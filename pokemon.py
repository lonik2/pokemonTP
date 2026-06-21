import json
import random
from clases import HashMap, HashSet


class Pokemon:
    def __init__ (self, id, nombre, tipo, poder_combate):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.poder_combate = poder_combate
    
    def __repr__(self):
        return f"{self.nombre} ({self.tipo}) ({self.poder_combate})"




Pokedex = HashMap()

try:
    with open("pokemones.json", "r", encoding="utf-8") as pokemones:
        lista_pokemones = json.load(pokemones)

    for p in lista_pokemones:
        datos_pokemon = Pokemon(p["id"], p["nombre"], p["tipo"], p["poder_combate"])
        clave = str(p["id"])
        Pokedex.agregar(clave, datos_pokemon)
except FileNotFoundError:
    print ("no se encontro el json con los datos")

Registro_medallas = HashSet()
 
try:
    with open("medallas.json", "r", encoding="utf-8") as medallas:
        lista_medallas = json.load(medallas)
 
        for m in lista_medallas[:2]:
            Registro_medallas.agregar(m["nombre"])
except FileNotFoundError:
    print("no se encontro el json con las medallas")

print ("-----POKEDEX NACIONAL-----")
Pokedex.mapa()
print()
print ("-----REGISTRO DE MEDALLAS-----")
Registro_medallas.mostrar_set()