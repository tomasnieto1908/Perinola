import pytest
from Perinola import Perinola


def test_prueba():
   assert True


def test_constructor():
   p = Perinola()
   assert p.cara_visible == "Pon 1"


def test_repr():
   p = Perinola()
   p.tirar()
   msj = p.__repr__().lower()
   assert "salio" in msj
   assert p.cara_visible.lower() in msj


def test_tirar_aleatorio():
   p = Perinola()
   cara_original = p.cara_visible
   salioOtro = False
   for _ in range(1000):
       p.tirar()
       if p.cara_visible != cara_original:
           salioOtro = True
           break


   assert salioOtro


def test_tirar_valores_en_opciones():
   p = Perinola()
   opciones = ("Pon 1", "Toma 2", "Todos Ponen", "Toma 1", "Pon 2", "Toma Todo")
   for _ in range(1000):
       p.tirar()
       assert p.cara_visible in opciones


def test_tirar_return():
   p = Perinola()
   caras_posibles = ("Pon 1", "Toma 2", "Todos Ponen", "Toma 1", "Pon 2", "Toma Todo")
   for _ in range(1000):
       resultado = p.tirar()
       assert resultado in caras_posibles


def test_tirar_aleatorio_todos_los_valores():
   p = Perinola()
   caras_posibles = {"Pon 1", "Toma 2", "Todos Ponen", "Toma 1", "Pon 2", "Toma Todo"}
   caras_obtenidas = set()


   for _ in range(1000):
       p.tirar()
       caras_obtenidas.add(p.cara_visible)


   assert caras_obtenidas == caras_posibles
