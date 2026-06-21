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

