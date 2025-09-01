from enum import Enum

class Size(Enum):
    TALL = ("Tall", 1.00)
    GRANDE = ("Grande", 1.15)
    VENTI = ("Venti", 1.30)
    # Para agregar uno nuevo:
    # SHORT = ("Short", 0.90)

    def __init__(self, label: str, factor: float):
        self._label = label
        self._factor = factor

    @property
    def label(self) -> str:
        return self._label

    @property
    def factor(self) -> float:
        return self._factor
