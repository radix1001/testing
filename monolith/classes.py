from dataclasses import dataclass
from decimal import *

getcontext().prec = 4  # Decimal precision


@dataclass(frozen=True)
# frozen setup as True to immutability (prevent side effects)
class Bmi:
    height: Decimal
    weight: Decimal

    def bmi(self) -> Decimal:
        return self.weight / (self.height * self.height)

