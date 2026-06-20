class HashMap:
    def __init__(self, tamaño=15):
        self.tamaño = tamaño
        self.buckets = [[] for _ in range(tamaño)]

    def hash_funcion(self, key):
        suma_num = sum(int(char) for char in key if char.isdigit())
        return suma_num % 10

    def agregar(self, key, value):
        indice = self.hash_funcion(key)
        bucket = self.buckets[indice]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def buscar(self, key):
        indice = self.hash_funcion(key)
        bucket = self.buckets[indice]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def borrar(self, key):
        indice = self.hash_funcion(key)
        bucket = self.buckets[indice]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

    def mapa(self):
        for indice, bucket in enumerate(self.buckets):
            print(f"Bucket {indice}: {bucket}")