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
    disponibles = []
    for bucket in pokedex.buckets:
        if bucket is not None:
            disponibles.append(bucket[1])
    pokemon = random.choice(disponibles)
    print(f"Un {pokemon.nombre} salvaje ha aparecido")
    time.sleep (1)
    print(f"{pokemon.nombre} atrapado exitosamente")
    time.sleep(1)
    if len(equipo) < 6:
        equipo.append (pokemon)
        print (f"{pokemon.nombre} agregado al equipo")
        time.sleep(1)
    else:
        pc.agregar(pokemon)
        print(f"{pokemon.nombre} guardado en la pc")
        time.sleep(1)
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

def transferir_pokemon (pc, transferencias):
    if pc.cabeza is None:
        print("no hay pokemones en la PC")
        return
    
    disponibles = []
    actual = pc.cabeza
    while actual is not None:
        disponibles.append(actual.valor)
        actual = actual.siguiente

    print("--- pokemones en la PC ---")
    for i in range(len(disponibles)):
        print(f"  {i + 1}. {disponibles[i]}")
    eleccion = int(input("Elegi el numero del pokemon que queres transferir: "))
    if eleccion < 1 or eleccion > len(disponibles):
        print("numero invalido")
        return

    pokemon = disponibles[eleccion - 1]
    pc.remover(pokemon)
    if transferencias.tamaño() >= 5:
        transferencias.stack.pop(0)
    transferencias.push(pokemon)
    print(f"{pokemon.nombre} fue transferido al profesor Oak")
    time.sleep(1.5)

def deshacer_transferencia(pc, transferencias):
    if transferencias.isEmpty():
        print("No hay transferencias para deshacer")
        return
    pokemon = transferencias.pop()
    pc.agregar(pokemon)
    print(f"{pokemon.nombre} volvio a la PC")
    time.sleep(1.5)

def mover_pokemon(equipo, pc):
    print("1. equipo a pc")
    print("2. pc a equipo")
    print("3. cancelar")
    opcion = input("Elegi una opción: ")
 
    if opcion == "1":
        if len(equipo) == 0:
            print("Tu equipo esta vacio")
            return
        print("Tu equipo")
        for i in range(len(equipo)):
            print(f"  {i + 1}. {equipo[i]}")
        eleccion = int(input("Elegi el numero del pokemon que queres mandar a la PC: "))
        if eleccion < 1 or eleccion > len(equipo):
            print("numero invalido")
            return
        pokemon = equipo[eleccion - 1]
        equipo.remove(pokemon)
        pc.agregar(pokemon)
        print(f"{pokemon.nombre} fue mandado a la PC")
        time.sleep(1.5)
    elif opcion == "2":
        if pc.cabeza is None:
            print("La PC esta vacia")
            return
        if len(equipo) >= 6:
            print("Tu equipo esta lleno, saca uno primero")
            return
        disponibles = []
        nodo = pc.cabeza
        while nodo is not None:
            disponibles.append(nodo.valor)
            nodo = nodo.siguiente
        print("Pokemon en la PC")
        for i in range(len(disponibles)):
            print(f"  {i + 1}. {disponibles[i]}")
        eleccion = int(input("Elegi el numero del pokemon que queres traer al equipo: "))
        if eleccion < 1 or eleccion > len(disponibles):
            print("numero invalido")
            return
        pokemon = disponibles[eleccion - 1]
        pc.remover(pokemon)
        equipo.append(pokemon)
        print(f"{pokemon.nombre} entro a tu equipo")
        time.sleep(1.5)
    elif opcion == "3":
        return
    else:
        print("opcion invalida")

def desafiar_lider(lista_lideres, registro_medallas):
    if len(lista_lideres) == 0:
        print("No hay lideres.")
        return
    print("--- lideres de gimnasio ---")
    for i in range(len(lista_lideres)):
        lider = lista_lideres[i]
        tiene = registro_medallas.contiene(lider["medalla"])
        if tiene:
            estado = "(vencido)"
        else:
            estado = "(por vencer)"
        print(f"  {i + 1}. {estado} {lider['lider']} - {lider['medalla']}") 
    eleccion = int(input("Elegi el numero del lider que queres desafiar: "))
    if eleccion < 1 or eleccion > len(lista_lideres):
        print("numero invalido")
        return
    lider = lista_lideres[eleccion - 1]
    print(f"Peleando con {lider['lider']}")
    time.sleep(2)
    gano = random.random() < 0.5
    if gano:
        print(f"Ganaste contra {lider['lider']}")
        time.sleep(1.5)
        agregada = registro_medallas.agregar(lider["medalla"])
        if agregada:
            print(f"Obtuviste la {lider['medalla']}")
            time.sleep(1)
        else:
            print(f"Ya tenias la {lider['medalla']}")
            time.sleep(1)
    else:
        print(f"Perdiste contra {lider['lider']}")
        time.sleep(1.5)
 

def ver_equipo():
    if not equipo:
        print("Tu equipo esta vacio")
        return
    print("---Tu equipo---")
    for i, p in enumerate(equipo, start=1):
        print(f"  {i}. {p}")
    time.sleep(2.5)
 
def ver_registro(lista_lideres, registro_medallas):
    obtenidas = 0
    for l in lista_lideres:
        if registro_medallas.contiene(l["medalla"]):
            obtenidas += 1
    print(f"Medallas: {obtenidas}/{len(lista_lideres)}")
    for lider in lista_lideres:
        marca = "(obtenida)" if registro_medallas.contiene(lider["medalla"]) else "(por obtener)"
        print(f"  {marca} {lider["medalla"]} - {lider["lider"]}")
    time.sleep(2.5)

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
    time.sleep(2.5)

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

def buscar_en_equipo(equipo):
    if len(equipo) == 0:
        print("Tu equipo esta vacio")
        return
    nombre = input("escribi el nombre del Pokemon que queres buscar: ")
    encontrado = False
    for i in range(len(equipo)):
        if equipo[i].nombre.lower() == nombre.lower():
            print(f"{equipo[i].nombre} esta en tu equipo")
            time.sleep(1.5)
            encontrado = True
            break
    if not encontrado:
        print(f"{nombre} no esta en tu equipo")
        time.sleep(1.5)

def consultar_pokedex(pokedex):
    id_ordenados = []
    for bucket in pokedex.buckets:
        if bucket is not None:
            id_ordenados.append(int(bucket[0]))
    id_ordenados.sort()
    id = int(input("Escribi el id del pokemon que vas a buscar: "))
    izquierda = 0
    derecha = len(id_ordenados) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if id_ordenados[medio] == id:
            pokemon = pokedex.buscar(str(id))
            print(f"El id {id} es de: {pokemon}")
            return
        elif id_ordenados[medio] < id:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    print(f"El id {id} no esta en la pokedex")
    time.sleep(1.5)