from Reserva import Reserva # Solo este import

class Nodo:
    def __init__(self, reserva: Reserva):
        self.reserva = reserva
        self.siguiente = None
        self.anterior = None