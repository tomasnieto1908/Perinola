from Perinola import Perinola
from Apuestas import Apuesta
from Jugador import Jugador

p = Perinola()
p.tirar()
print(p.cara_visible)



a = Apuesta()
a.ponerFichas(5)
print(a)

jugador = Jugador("Tomás", 15)
print(jugador) 


