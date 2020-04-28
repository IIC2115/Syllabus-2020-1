import random

def inputs(size):
    aviones = []
    for _ in range(size):
        x = random.uniform(max(-100000, -size), min(size, 100000))
        y = random.uniform(max(-100000, -size), min(size, 100000))
        aviones.append((x,y))
    return aviones
    
