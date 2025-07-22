from decimal import ROUND_HALF_UP, Decimal


class Money:
    def __init__(self, amount: float):
        # Usando Decimal para evitar problemas com float
        self.amount = Decimal(str(amount)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    def __add__(self, other):
        if not isinstance(other, Money):
            raise TypeError("Can only add Money to Money")
        return Money(float(self.amount + other.amount))

    def __sub__(self, other):
        if not isinstance(other, Money):
            raise TypeError("Can only subtract Money from Money")
        return Money(float(self.amount - other.amount))

    def __repr__(self):
        return f"Money({self.amount})"
    
    def __eq__(self, other):
        if not isinstance(other, Money):
            return False
        return self.amount == other.amount
