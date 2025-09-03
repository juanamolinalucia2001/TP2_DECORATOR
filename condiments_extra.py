from beverages import CondimentDecorator, Beverage

class Topping(CondimentDecorator):
    """
    Condimentador genérico para cualquier topping.
    Se le pasa el nombre y el precio base al instanciar.
    """
    def __init__(self, beverage: Beverage, name: str, price: float):
        super().__init__(beverage)
        self.name = name
        self.price = price

    def get_description(self) -> str:
        return f"{self._beverage.get_description()}, {self.name}"

    def cost(self) -> float:
        # Se multiplica por el factor del tamaño como los demás condimentos
        return self._beverage.cost() + self.price * self.get_size().factor
    

class Honey(Topping):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage, "Miel", 0.30)

class Cacao(Topping):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage, "Cacao", 0.50)

class Cinnamon(Topping):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage, "Canela", 0.40)
        
class Vanilla(Topping):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage, "Vainilla", 0.35)


