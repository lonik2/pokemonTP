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
        contador = 0
        for indice, bucket in enumerate(self.buckets):
            contador+= 1
            print(contador, bucket)

