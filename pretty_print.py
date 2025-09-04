# pretty_print.py
from beverages import Beverage

class PrettyPrint(Beverage):
    """
    Decorador de presentación para condensar condimentos repetidos.
    Solo afecta get_description(), no el costo.
    """
    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    def get_description(self) -> str:
        desc = self._beverage.get_description().split(", ")
        if not desc:
            return ""
        
        # Procesar repeticiones consecutivas
        result = []
        count = 1
        for i in range(1, len(desc)+1):
            if i < len(desc) and desc[i] == desc[i-1]:
                count += 1
            else:
                if count == 1:
                    result.append(desc[i-1])
                elif count == 2:
                    result.append(f"Double {desc[i-1]}")
                elif count == 3:
                    result.append(f"Triple {desc[i-1]}")
                else:
                    result.append(f"{count}x {desc[i-1]}")
                count = 1
        return ", ".join(result)

    def cost(self) -> float:
        return self._beverage.cost()

    def get_size(self):
        return self._beverage.get_size()

    def set_size(self, size):
        self._beverage.set_size(size)
        return self