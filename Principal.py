from Perinola import Perinola
from Apuestas import Apuesta
from Jugador import Jugador
from Ronda import Ronda



# Primero creamos algunos jugadores
jugador1 = Jugador("Tomás", 15)
jugador2 = Jugador("Andrés", 5)
jugador3 = Jugador("Lucía", 0)
jugador4 = Jugador("Marta", 10)

# Creamos una ronda
ronda = Ronda()

# Agregamos jugadores a la ronda
ronda.agregarJugador(jugador1)
ronda.agregarJugador(jugador2)
# Intentamos agregar un jugador sin fichas (esto debería dar un error)
try:
    ronda.agregarJugador(jugador3)
except ValueError as e:
    print(e)  # Imprime: El jugador no tiene fichas para jugar.

ronda.agregarJugador(jugador4)

# Mostramos el estado inicial de la ronda
print("Estado inicial de la ronda:")
print(ronda)  # Debería mostrar los jugadores en el orden en que fueron agregados

# Pasamos el turno
ronda.pasarTurno()
print("\nDespués de pasar el turno:")
print(ronda)  # El primer jugador debería estar ahora al final de la lista

# Verificamos el jugador en turno
print("\nJugador en turno:")
print(ronda.jugadorEnTurno())  # Debería mostrar el jugador que ahora está al principio

# Eliminamos jugadores sin fichas
ronda.sacarJugadoresSinFichas()
print("\nDespués de eliminar jugadores sin fichas:")
print(ronda)  # Solo deberían quedar jugadores con fichas

# Verificamos si queda un solo jugador
if ronda.quedaUnSoloJugador():
    print("\nQueda un solo jugador en la ronda.")
else:
    print("\nQuedan varios jugadores en la ronda.")

