# condiments.py
# Contiene el Decorador Abstracto y los Decoradores Concretos.

from abc import ABC, abstractmethod
from beverages import Beverage

# --- Decorador Abstracto ---
class CondimentDecorator(Beverage, ABC):
    """
    Clase base para los decoradores de condimentos.
    Hereda de Beverage para tener el mismo tipo.
    Mantiene una referencia a la bebida que está envolviendo.
    """
    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    @abstractmethod
    def get_description(self) -> str:
        pass

    def get_size(self) -> str:
        """
        Delegamos el tamaño a la bebida envuelta.
        """
        return self._beverage.get_size()

# --- Decoradores Concretos ---
class Milk(CondimentDecorator):
    """
    Decorador para añadir Leche a una bebida.
    """
    PRICES = {
        Beverage.TALL: 0.10,
        Beverage.GRANDE: 0.15,
        Beverage.VENTI: 0.20,
    }

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Leche"

    def cost(self) -> float:
        extra = self.PRICES.get(self.get_size(), 0.15)
        return self._beverage.cost() + extra


class Mocha(CondimentDecorator):
    """
    Decorador para añadir Mocha a una bebida.
    """
    PRICES = {
        Beverage.TALL: 0.20,
        Beverage.GRANDE: 0.25,
        Beverage.VENTI: 0.30,
    }

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Mocha"

    def cost(self) -> float:
        extra = self.PRICES.get(self.get_size(), 0.25)
        return self._beverage.cost() + extra


class Soy(CondimentDecorator):
    """
    Decorador para añadir Soja a una bebida.
    """
    PRICES = {
        Beverage.TALL: 0.10,
        Beverage.GRANDE: 0.15,
        Beverage.VENTI: 0.20,
    }

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Soja"

    def cost(self) -> float:
        extra = self.PRICES.get(self.get_size(), 0.15)
        return self._beverage.cost() + extra


class Whip(CondimentDecorator):
    """
    Decorador para añadir Crema a una bebida.
    """
    PRICES = {
        Beverage.TALL: 0.10,
        Beverage.GRANDE: 0.15,
        Beverage.VENTI: 0.20,
    }

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Crema"

    def cost(self) -> float:
        extra = self.PRICES.get(self.get_size(), 0.15)
        return self._beverage.cost() + extra


class Caramel(CondimentDecorator):
    """
    Decorador para añadir Caramelo a una bebida.
    """
    PRICES = {
        Beverage.TALL: 0.20,
        Beverage.GRANDE: 0.25,
        Beverage.VENTI: 0.30,
    }

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Caramelo"

    def cost(self) -> float:
        extra = self.PRICES.get(self.get_size(), 0.25)
        return self._beverage.cost() + extra
