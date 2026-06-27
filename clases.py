class HashMap:
    def __init__(self, tamaño=17):
        self.tamaño = tamaño
        self.buckets = [None for _ in range(tamaño)]

    def hash_funcion(self, key):
        suma_num = sum(int(char) for char in key if char.isdigit())
        return suma_num % self.tamaño

    def agregar(self, key, value):
        indice = self.hash_funcion(key)
        intentos = 0
        while self.buckets[indice] is not None and intentos < self.tamaño:
            k, v = self.buckets[indice]
            if k == key:
                self.buckets[indice] = (key, value)
                return
            indice = (indice + 1) % self.tamaño
            intentos += 1
        if intentos < self.tamaño:
            self.buckets[indice] = (key, value)

    def buscar(self, key):
        indice = self.hash_funcion(key)
        intentos = 0
        while self.buckets[indice] is not None and intentos < self.tamaño:
            k, v = self.buckets[indice]
            if k == key:
                return v
            indice = (indice + 1) % self.tamaño
            intentos += 1
        return None

    def borrar(self, key):
        indice = self.hash_funcion(key)
        intentos = 0
        while self.buckets[indice] is not None and intentos < self.tamaño:
            k, v = self.buckets[indice]
            if k == key:
                self.buckets[indice] = None
                return
            indice = (indice + 1) % self.tamaño
            intentos += 1

    def mapa(self):
        for indice, bucket in enumerate(self.buckets):
            print(f"{indice+1}: {bucket}")

class HashSet:
    def __init__(self, tamaño=8):
        self.tamaño = tamaño
        self.buckets = [[] for _ in range(tamaño)]
      
    def hash_funcion(self, value):
        return sum(ord(char) for char in value) % self.tamaño

    def agregar(self, value):
        indice = self.hash_funcion(value)
        bucket = self.buckets[indice]
        if value not in bucket:
            bucket.append(value)
            return True
        return False

    def contiene(self, value):
        indice = self.hash_funcion(value)
        bucket = self.buckets[indice]
        return value in bucket

    def borrar(self, value):
        indice = self.hash_funcion(value)
        bucket = self.buckets[indice]
        if value in bucket:
            bucket.remove(value)

    def mostrar_set(self):
        for indice, bucket in enumerate(self.buckets):
            print(f"{indice+1}: {bucket}")

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
 
    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
 
    def mostrar(self):
        if self.cabeza is None:
            print("La PC esta vacia")
            return
        actual = self.cabeza
        contador = 1
        while actual is not None:
            print(f"  {contador}. {actual.valor}")
            actual = actual.siguiente
            contador += 1
    
    def remover(self, valor):
        if self.cabeza is None:
            return
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            return
        actual = self.cabeza
        while actual.siguiente is not None:
            if actual.siguiente.valor == valor:
                actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente

class Stack:
    def __init__ (self):
        self.stack = []

    def push (self, element):
        self.stack.append(element)

    def isEmpty (self):
        return len(self.stack) == 0

    def pop (self):
        if self.isEmpty():
            return "lista vacia"
        return self.stack.pop()

    def peek (self):
        if self.isEmpty():
            return "lista vacia"
        return self.stack[-1]

    def tamaño (self):
        return len(self.stack)

class Queue:
    def __init__ (self):
        self.queue = []
    
    def push (self, element):
        self.queue.append(element)

    def isEmpty (self):
        return len(self.queue) == 0

    def pop (self):
        if self.isEmpty():
            return "lista vacia"
        return self.queue.pop(0)

    def peek (self):
        if self.isEmpty():
            return "lista vacia"
        return self.queue[0]

    def tamaño (self):
        return len(self.queue)