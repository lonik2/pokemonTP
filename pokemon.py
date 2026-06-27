import json
import random
from clases import HashMap, HashSet, Nodo, ListaEnlazada


class Pokemon:
    def __init__ (self, id, nombre, tipo, poder_combate):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.poder_combate = poder_combate
    
    def __repr__(self):
        return f"{self.nombre} ({self.tipo}) ({self.poder_combate})"

Pokedex = HashMap()
Registro_medallas = HashSet()
equipo = []
pc = ListaEnlazada()

try:
    with open("pokemones.json", "r", encoding="utf-8") as pokemones:
        lista_pokemones = json.load(pokemones)

    for p in lista_pokemones:
        datos_pokemon = Pokemon(p["id"], p["nombre"], p["tipo"], p["poder_combate"])
        clave = str(p["id"])
        Pokedex.agregar(clave, datos_pokemon)
except FileNotFoundError:
    print ("no se encontro el json con los datos")
 
try:
    with open("medallas.json", "r", encoding="utf-8") as medallas:
        lista_medallas = json.load(medallas)
 
        for m in lista_medallas[:2]:
            Registro_medallas.agregar(m["nombre"])
except FileNotFoundError:
    print("no se encontro el json con las medallas")

def capturar_pokemon(pokedex, equipo, pc):
    disponibles = [bucket[1] for bucket in pokedex.buckets if bucket is not None]
    pokemon = random.choice(disponibles)
    print(f"Un {pokemon.nombre} salvaje ha aparecido")
    print(f"{pokemon.nombre} atrapado exitosamente")
    if len(equipo) < 6:
        equipo.append (pokemon)
        print (f"{pokemon} agregado al equipo")
    else:
        pc.agregar(pokemon)
        print(f"{pokemon} guardado en la pc")
    return pokemon


print ("-----POKEDEX NACIONAL-----")
Pokedex.mapa()
print()
print ("-----REGISTRO DE MEDALLAS-----")
Registro_medallas.mostrar_set()