import pytest
from Jugador import Jugador

def test_constructor_jugador():
    """Verifica que el constructor inicializa correctamente el nombre y las fichas."""
    jugador = Jugador("Tomás", 5)
    assert jugador.nombre == "Tomás"
    assert jugador.fichas == 5

def test_dar_ficha():
    """Verifica que el método darFicha añade correctamente las fichas."""
    jugador = Jugador("Tomás", 5)
    jugador.darFicha(3)
    assert jugador.fichas == 8

    jugador.darFicha()
    assert jugador.fichas == 9  
def test_sacar_ficha():
    """Verifica que el método sacarFicha elimina correctamente las fichas."""
    jugador = Jugador("Tomás", 5)
    jugador.sacarFicha(3)
    assert jugador.fichas == 2

    jugador.sacarFicha()
    assert jugador.fichas == 1  
def test_sacar_ficha_error():
    """Verifica que se lance un ValueError cuando intentas sacar más fichas de las disponibles."""
    jugador = Jugador("Tomás", 2)
    with pytest.raises(ValueError):
        jugador.sacarFicha(5)

def test_tiene_ficha():
    """Verifica que el método tieneFicha funcione correctamente."""
    jugador = Jugador("Tomás", 5)
    assert jugador.tieneFicha(3)  
    assert not jugador.tieneFicha(6) 

def test_sin_fichas():
    """Verifica que el método sinFichas devuelva True cuando no hay fichas."""
    jugador = Jugador("Tomás", 0)
    assert jugador.sinFichas()

    jugador = Jugador("Ana", 5)
    assert not jugador.sinFichas()

def test_repr_jugador():
    """Verifica que el método __repr__ devuelva correctamente la representación del jugador."""
    jugador = Jugador("Tomás", 5)
    assert repr(jugador) == "Tomás, 5 fichas"
