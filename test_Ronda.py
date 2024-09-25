import pytest
from Ronda import Ronda , Jugador 
def test_agregar_jugador():
    """Verifica que se pueda agregar un jugador con fichas a la ronda."""
    ronda = Ronda()
    jugador = Jugador("Tomás", 5)
    ronda.agregarJugador(jugador)
    assert len(ronda.jugadores) == 1
    assert ronda.jugadores[0].nombre == "Tomás"

def test_agregar_jugador_sin_fichas():
    """Verifica que no se pueda agregar un jugador sin fichas."""
    ronda = Ronda()
    jugador_sin_fichas = Jugador("Ana", 0)
    with pytest.raises(ValueError):
        ronda.agregarJugador(jugador_sin_fichas)

def test_sacar_jugadores_sin_fichas():
    """Verifica que los jugadores sin fichas sean eliminados de la ronda."""
    ronda = Ronda()
    jugador1 = Jugador("Tomas", 5)
    jugador2 = Jugador("Ana", 0)
    ronda.agregarJugador(jugador1)
    ronda.agregarJugador(jugador2)
   
    ronda.sacarJugadoresSinFichas()
    assert (len(ronda.jugadores) >= 1)
    assert (ronda.jugadores[0] == "Tomas",5)

def test_jugador_en_turno():
    """Verifica que el primer jugador agregado esté en turno."""
    ronda = Ronda()
    jugador1 = Jugador("Tomás", 5)
    jugador2 = Jugador("Ana", 3)
    
    ronda.agregarJugador(jugador1)
    ronda.agregarJugador(jugador2)

    assert ronda.jugadorEnTurno() == jugador1

def test_pasar_turno():
    """Verifica que el turno pase correctamente entre los jugadores."""
    ronda = Ronda()
    jugador1 = Jugador("Tomás", 5)
    jugador2 = Jugador("Ana", 3)

    ronda.agregarJugador(jugador1)
    ronda.agregarJugador(jugador2)

    ronda.pasarTurno()
    assert ronda.jugadores[0] == jugador2
    assert ronda.jugadores[1] == jugador1

def test_queda_un_solo_jugador():
    """Verifica que quedaUnSoloJugador devuelva True cuando queda un solo jugador."""
    ronda = Ronda()
    jugador1 = Jugador("Tomás", 5)
    ronda.agregarJugador(jugador1)

    assert ronda.quedaUnSoloJugador()

    jugador2 = Jugador("Ana", 3)
    ronda.agregarJugador(jugador2)

    assert not ronda.quedaUnSoloJugador()

def test_str_ronda():
    """Verifica que el método __str__ de la ronda devuelva correctamente la representación."""
    ronda = Ronda()
    jugador1 = Jugador("Tomás", 5)
    jugador2 = Jugador("Ana", 3)

    ronda.agregarJugador(jugador1)
    ronda.agregarJugador(jugador2)

    expected_output = "Tomás, 5 fichas\nAna, 3 fichas"
    assert str(ronda) == expected_output
