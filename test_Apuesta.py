import pytest
from Apuestas import Apuesta

def test_constructor():
    a = Apuesta()
    assert a.fichas == 0  

def test_repr():
    a = Apuesta()
    assert repr(a) == "Apuesta: 0 fichas"  

def test_ponerFichas():
    a = Apuesta()
    a.ponerFichas(5)
    assert a.fichas == 5 

    a.ponerFichas(3)
    assert a.fichas == 8  

def test_tomarFichas():
    a = Apuesta()
    a.ponerFichas(10) 
    a.tomarFichas(3)
    assert a.fichas == 7  

def test_tomarFichas_error():
    a = Apuesta()
    a.ponerFichas(5)
    with pytest.raises(ValueError):
        a.tomarFichas(6) 

def test_tomarTodas():
    a = Apuesta()
    a.ponerFichas(7)
    todas = a.tomarTodas()
    assert todas == 7 
    assert a.fichas == 0  

def test_tieneFichas():
    a = Apuesta()
    a.ponerFichas(5)
    assert a.tieneFichas(3) 
    assert not a.tieneFichas(6)  

def test_estaVacia():
    a = Apuesta()
    assert a.estaVacia()  
    a.ponerFichas(5)
    assert not a.estaVacia()  
    a.tomarTodas()
    assert a.estaVacia()  
