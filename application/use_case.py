# application/use_cases.py
from persistence.models import CompraMilhas

class CalcularCompraMilhasUseCase:
    @staticmethod
    def calcular_compra(compra_milhas: CompraMilhas):
        base_preco_por_milheiro = 70
        preco_com_desconto = base_preco_por_milheiro * (1 - compra_milhas.desconto / 100)
        milhas_bonus = compra_milhas.milhas_comprar * (compra_milhas.bonus / 100)
        total_milhas = compra_milhas.milhas_comprar + milhas_bonus
        total_custo = total_milhas * preco_com_desconto
        custo_por_milheiro = total_custo / total_milhas
        return {
            "milhas_comprar": compra_milhas.milhas_comprar,
            "preco_referencia": "R$ 70,00/milheiro",
            "desconto": f"{compra_milhas.desconto}%",
            "preco_com_desconto": f"R${preco_com_desconto:.2f}/milheiro",
            "bonus": f"{compra_milhas.bonus}%",
            "milhas_bonus": int(milhas_bonus),
            "milhas_totais": int(total_milhas),
            "valor_total": f"R${compra_milhas.milhas_comprar * preco_com_desconto:.2f}",
            "valor_por_milheiro": f"R${custo_por_milheiro:.2f}"
        }
