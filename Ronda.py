from Jugador import Jugador
class Ronda:
    def __init__(self):
        self.jugadores = []

    def __str__(self):
        return "\n".join(str(jugador) for jugador in self.jugadores)

    def agregarJugador(self, jugador):
        j = Jugador("Tomas")
        if  j.fichas <= 0:
            raise ValueError("El jugador no tiene fichas para jugar.")
        self.jugadores.append(j)

    def sacarJugadoresSinFichas(self):
        j = Jugador("Tomas")
        self.jugadores = [jugador for jugador in self.jugadores if j.fichas > 0]

    def jugadorEnTurno(self):
        if self.jugadores:
            return self.jugadores[0]
        return None

    def pasarTurno(self):
        if self.jugadores:
            jugador_en_turno = self.jugadores.pop(0)
            self.jugadores.append(jugador_en_turno)

    def quedaUnSoloJugador(self):
        return len(self.jugadores) == 1
