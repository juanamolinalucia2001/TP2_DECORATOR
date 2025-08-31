from abc import ABC, abstractmethod
from beverages import Beverage

# --- Decorador abstracto ---
class CondimentDecorator(Beverage, ABC):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    @abstractmethod
    def get_description(self) -> str:
        pass

    def get_size(self) -> str:
        return self._beverage.get_size()

# --- Decoradores concretos ---
class Milk(CondimentDecorator):
    PRICES = {Beverage.TALL: 0.10, Beverage.GRANDE: 0.15, Beverage.VENTI: 0.20}

    def get_description(self) -> str:
        return f"{self._beverage.get_description()}, Leche"

    def cost(self) -> float:
        return self._beverage.cost() + self.PRICES.get(self.get_size(), 0.15)

class Mocha(CondimentDecorator):
    PRICES = {Beverage.TALL: 0.20, Beverage.GRANDE: 0.25, Beverage.VENTI: 0.30}

    def get_description(self) -> str:
        return f"{self._beverage.get_description()}, Mocha"

    def cost(self) -> float:
        return self._beverage.cost() + self.PRICES.get(self.get_size(), 0.25)

class Soy(CondimentDecorator):
    PRICES = {Beverage.TALL: 0.10, Beverage.GRANDE: 0.15, Beverage.VENTI: 0.20}

    def get_description(self) -> str:
        return f"{self._beverage.get_description()}, Soja"

    def cost(self) -> float:
        return self._beverage.cost() + self.PRICES.get(self.get_size(), 0.15)

class Whip(CondimentDecorator):
    PRICES = {Beverage.TALL: 0.10, Beverage.GRANDE: 0.15, Beverage.VENTI: 0.20}

    def get_description(self) -> str:
        return f"{self._beverage.get_description()}, Crema"

    def cost(self) -> float:
        return self._beverage.cost() + self.PRICES.get(self.get_size(), 0.15)

class Caramel(CondimentDecorator):
    PRICES = {Beverage.TALL: 0.20, Beverage.GRANDE: 0.25, Beverage.VENTI: 0.30}

    def get_description(self) -> str:
        return f"{self._beverage.get_description()}, Caramelo"

    def cost(self) -> float:
        return self._beverage.cost() + self.PRICES.get(self.get_size(), 0.25)
