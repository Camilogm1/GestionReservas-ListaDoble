class Reserva: # Sin imports arriba
    def __init__(self, cliente: str, id_reserva: int, costo: float):
        self.cliente = cliente
        self.id_reserva = id_reserva
        self.costo = max(costo, 0)
