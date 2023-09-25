# persistence/models.py

class CompraMilhas:
    def __init__(self, milhas_comprar: int, desconto: int, bonus: int):
        self.milhas_comprar = milhas_comprar
        self.desconto = desconto
        self.bonus = bonus
