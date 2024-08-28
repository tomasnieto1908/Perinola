class Apuesta:
     def __init__(self):
          self.fichas = 0
     def __repr__(self):
          return f"Apuesta: {self.fichas} fichas" 
     def ponerFichas(self,Cuantas=1):
          self.fichas = self.fichas + Cuantas
     def tomarFichas(self, Cuantas=1):
        if Cuantas > self.fichas:
            raise ValueError("No hay suficientes fichas en la apuesta")
        self.fichas = self.fichas - Cuantas
     def tomarTodas(self):
        todas = self.fichas
        self.fichas = 0
        return todas
     def tieneFichas(self, Cuantas=1):
        return self.fichas >= Cuantas
     def estaVacia(self):
        return self.fichas == 0