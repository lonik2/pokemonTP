import json
import random
import time
from clases import HashMap, HashSet, Nodo, ListaEnlazada, Queue, Stack


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
lista_lideres = []
equipo = []
pc = ListaEnlazada()
centro_pokemon = Queue()
transferencias = Stack()

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
        lista_lideres = json.load(medallas)
 
        for m in lista_lideres[:2]:
            Registro_medallas.agregar(m["medalla"])
except FileNotFoundError:
    print("no se encontro el json con las medallas")

def capturar_pokemon(pokedex, equipo, pc):
    disponibles = [bucket[1] for bucket in pokedex.buckets if bucket is not None]
    pokemon = random.choice(disponibles)
    print(f"Un {pokemon.nombre} salvaje ha aparecido")
    time.sleep (1)
    print(f"{pokemon.nombre} atrapado exitosamente")
    if len(equipo) < 6:
        equipo.append (pokemon)
        print (f"{pokemon} agregado al equipo")
    else:
        pc.agregar(pokemon)
        print(f"{pokemon} guardado en la pc")
    return pokemon

def curar (equipo, centro_pokemon):
    for p in equipo:
        centro_pokemon.push(p)
        print (f"{p} agregado al centro")
        time.sleep(1)    
    while not centro_pokemon.isEmpty():
        p = centro_pokemon.peek()
        print (f"curando {p}")
        time.sleep(1)
        centro_pokemon.pop()
        print (f"{p} curado")
        time.sleep(1)

def transferir_pokemon (pc, transferencias, pokemon):
    if pc.cabeza is None:
        print("no hay pokemones en la PC")
        return

    disponibles = []
    actual = pc.cabeza
    while actual is not None:
        disponibles.append(actual.valor)
        actual = actual.siguiente

    print("--- pokemones en la PC ---")
    for i, p in enumerate(disponibles, start=1):
        print(f"  {i}. {p}")

    eleccion = int(input("Elegí el número del pokemon que queres transferir: "))
    if eleccion < 1 or eleccion > len(disponibles):
        print("numero invalido")
        return

    pokemon = disponibles[eleccion - 1]
    pc.remover(pokemon)
    if transferencias.tamaño() >= 5:
        transferencias.stack.pop(0)
    transferencias.push(pokemon)
    print(f"{pokemon.nombre} fue transferido al profesor Oak")


def deshacer_transferencia(pc, transferencias):
    if transferencias.isEmpty():
        print("No hay transferencias para deshacer")
        return
    pokemon = transferencias.pop()
    pc.agregar(pokemon)
    print(f"{pokemon.nombre} volvio a la PC")

def desafiar_lider(lista_lideres, registro_medallas):
    if not lista_lideres:
        print("No hay lideres.")
        return
 
    print("--- lideres de gimnasio ---")
    for i, lider in enumerate(lista_lideres, start=1):
        tiene = registro_medallas.contiene(lider["lider"])
        if tiene:
            estado = "(vencido)"
        else:
            estado = "(por vencer)"
        print(f"  {i}. {estado} {lider["lider"]} - {lider["medalla"]}")
 
    eleccion = int(input("Elegi el numero del lider que queres desafiar: "))
    if eleccion < 1 or eleccion > len(lista_lideres):
        print("numero invalido")
        return
 
    lider = lista_lideres[eleccion - 1]
    print(f"\nPeleando con {lider["lider"]}")
    time.sleep(2)
    gano = random.random() < 0.5
    if gano:
        print(f"Ganaste contra {lider["lider"]}!")
        agregada = registro_medallas.agregar(lider["medalla"])
        if agregada:
            print(f"Obtuviste la {lider["medalla"]}")
        else:
            print(f"Ya tenias la {lider["medalla"]}")
    else:
        print(f"Perdiste contra {lider["lider"]}")
 
def ver_registro(lista_lideres, registro_medallas):
    obtenidas = sum(1 for l in lista_lideres if registro_medallas.contiene(l["medalla"]))
    print(f"Medallas: {obtenidas}/{len(lista_lideres)}")
    for lider in lista_lideres:
        marca = "[X]" if registro_medallas.contiene(lider["medalla"]) else "[ ]"
        print(f"  {marca} {lider["medalla"]} - {lider["lider"]}")

def ver_pc(pc):
    if pc.cabeza is None:
        print("La PC esta vacia")
        return
    print("---PC---")
    actual = pc.cabeza
    contador = 1
    while actual is not None:
        print(f"{contador}. {actual.valor}")
        actual = actual.siguiente
        contador += 1

def ordenar_pc(pc):
    if pc.cabeza is None:
        print("La PC esta vacia")
        return

    copia = []
    actual = pc.cabeza
    while actual is not None:
        copia.append(actual.valor)
        actual = actual.siguiente
 
    print("--- Ordenar PC ---")
    print("  1. Alfabeticamente")
    print("  2. Por tipo")
    print("  3. Competitiva")
    print("  4. Cancelar")
    opcion = int(input("Elegí una opción: "))
 
    if opcion == 1:
        n = len(copia)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if copia[j].nombre > copia[j + 1].nombre:
                    copia[j], copia[j + 1] = copia[j + 1], copia[j]
 
    elif opcion == 2:
        for i in range(1, len(copia)):
            actual = copia[i]
            j = i - 1
            while j >= 0 and copia[j].tipo > actual.tipo:
                copia[j + 1] = copia[j]
                j -= 1
            copia[j + 1] = actual
 
    elif opcion == 3:
        def quick_sort(lista, inicio, fin):
            if inicio < fin:
                pivote = lista[fin].poder_combate
                i = inicio - 1
                for j in range(inicio, fin):
                    if lista[j].poder_combate >= pivote:
                        i += 1
                        lista[i], lista[j] = lista[j], lista[i]
                lista[i + 1], lista[fin] = lista[fin], lista[i + 1]
                pi = i + 1
                quick_sort(lista, inicio, pi - 1)
                quick_sort(lista, pi + 1, fin)
 
        quick_sort(copia, 0, len(copia) - 1)
    
    elif opcion == 4:
        return
 
    else:
        print("Opcion invalida")
        return


print ("-----POKEDEX NACIONAL-----")
Pokedex.mapa()
print()
print ("-----REGISTRO DE MEDALLAS-----")
Registro_medallas.mostrar_set()