import random
import time


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pila = []


# Nombres de los jugadores
nombres_jugadores = ["Jarod", "Jassiel", "David", "Nick"]

# Creamos los jugadores
jugadores = [Jugador(nombre) for nombre in nombres_jugadores]

# Definimos la baraja como una lista de listas, donde cada sublista representa un palo
baraja = [
    ["1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B", "10B", "JB", "QB", "KB"],  # Bastos
    ["1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC"],  # Corazones
    ["1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"],  # Diamantes
    ["1T", "2T", "3T", "4T", "5T", "6T", "7T", "8T", "9T", "10T", "JT", "QT", "KT"]  # Treboles
]


# Función para repartir los naipes hasta que cada jugador tenga 10 naipes
def repartir_naipes(jugadores, baraja):
    naipes_repartidos = set()  # Conjunto para rastrear los naipes ya repartidos

    # Repartimos los naipes hasta que todos los jugadores tengan 10 naipes
    while any(len(jugador.pila) < 10 for jugador in jugadores):
        for jugador in jugadores:
            # Verificamos si el jugador ya tiene 10 naipes
            if len(jugador.pila) == 10:
                continue  # Pasamos al siguiente jugador

            # Seleccionamos un naipe aleatorio que no haya sido repartido antes
            naipe = random.choice(sum(baraja, []))
            while naipe in naipes_repartidos:
                naipe = random.choice(sum(baraja, []))

            # Agregamos el naipe a la pila del jugador y lo marcamos como repartido
            jugador.pila.append(naipe)
            naipes_repartidos.add(naipe)


# Repartimos los naipes entre los jugadores
repartir_naipes(jugadores, baraja)

# Iniciamos el juego
for i in range(10):  # 10 rondas, cada jugador recibe 1 carta por ronda
    for jugador in jugadores:
        print(f"Turno de {jugador.nombre}:")
        print("  ", jugador.pila.pop(0))  # Mostramos el naipe del jugador
        time.sleep(2)  # Espera de 2 segundos entre turnos
