from abc import ABC, abstractmethod
from beverages import Beverage
from size import Size

# --- Decorador abstracto ---
class CondimentDecorator(Beverage, ABC):
    """
    Hereda de Beverage para ser tratable como bebida.
    Envuelve una Beverage interna (composición).
    """
    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    def get_size(self) -> Size: # Delegamos en el componente interno

        return self._beverage.get_size()

    def set_size(self, size: Size):  #añadimos el get_size asi los condimentos pueden usar la clase para los tamaños y precios de los mismos

        self._beverage.set_size(size) # Propaga el cambio de tamaño hacia adentro para mantener consistencia.

        return self

# --- Decoradores concretos: sumamos precio BASE * factor del Size ---

class Milk(CondimentDecorator):
    BASE = 0.15

    def get_description(self) -> str:
        return f"{self._beverage.get_description()}, Leche"

    def cost(self) -> float:
        return self._beverage.cost() + self.BASE * self.get_size().factor # BASE * factor del Size

class Mocha(CondimentDecorator):
    BASE = 0.25

    def get_description(self) -> str:
        return f"{self._beverage.get_description()}, Mocha"

    def cost(self) -> float:
        return self._beverage.cost() + self.BASE * self.get_size().factor # BASE * factor del Size

class Soy(CondimentDecorator):
    BASE = 0.15

    def get_description(self) -> str:
        return f"{self._beverage.get_description()}, Soja"

    def cost(self) -> float:
        return self._beverage.cost() + self.BASE * self.get_size().factor # BASE * factor del Size

class Whip(CondimentDecorator):
    BASE = 0.15

    def get_description(self) -> str:
        return f"{self._beverage.get_description()}, Crema"

    def cost(self) -> float:
        return self._beverage.cost() + self.BASE * self.get_size().factor # BASE * factor del Size

class Caramel(CondimentDecorator):
    BASE = 0.25

    def get_description(self) -> str:
        return f"{self._beverage.get_description()}, Caramelo"

    def cost(self) -> float:
        return self._beverage.cost() + self.BASE * self.get_size().factor # BASE * factor del Size
