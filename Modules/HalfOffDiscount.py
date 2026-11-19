from Modules.DiscountStrategy import DiscountStrategy

class HalfOffDiscount(DiscountStrategy):
    def __init__(self, threshold: float, amount: float):
        self.threshold = threshold
        self.amount = amount

    def apply(self, total: float) -> float:
        return total/2 if total >= self.threshold else total