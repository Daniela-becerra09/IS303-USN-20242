def tuplas(entrada):
    # Verificamos que la entrada sea una tupla
    if not isinstance(entrada, tuple):
        raise ValueError("La entrada debe ser una tupla.")
    
    # Ordenamos la tupla y devolvemos una nueva tupla
    return tuple(sorted(entrada))

# Ejemplo de uso
entrada = (3, 1, 4, 2)
resultado = tuplas(entrada)
print(resultado)  # Salida: (1, 2, 3, 4)
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import time
import random

def tuplas(entrada):
    # Verificamos que la entrada sea una tupla
    if not isinstance(entrada, tuple):
        raise ValueError("La entrada debe ser una tupla.")
    
    # Ordenamos la tupla y devolvemos una nueva tupla
    return tuple(sorted(entrada))

# Generamos una tupla con 10,000 datos aleatorios
entrada = tuple(random.randint(1, 10000) for _ in range(10000))

# Tomamos el tiempo antes de ordenar
start_time = time.time()

# Ordenamos la tupla
resultado = tuplas(entrada)

# Tomamos el tiempo después de ordenar
end_time = time.time()

# Calculamos el tiempo total en segundos
tiempo_total = end_time - start_time

# Imprimimos el resultado del tiempo
print(f"Tiempo de ejecución: {tiempo_total:.6f} segundos")
