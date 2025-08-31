# main.py
# Script principal para probar el patrón Decorator.

from beverages import Espresso, DarkRoast, HouseBlend, Decaf
from condiments import Mocha, Whip, Soy ,Caramel

def main():
    """
    Función principal que simula la preparación de cafés en Starbuzz.
    """
    print("Bienvenido a Starbuzz Coffee!")
    print("--- Preparando pedidos ---")

    # Pedido 1: Un Espresso simple, sin condimentos.
    beverage1 = Espresso()
    print(f"Pedido 1: {beverage1.get_description()} ${beverage1.cost():.2f}")

    # Pedido 2: Un DarkRoast con doble Mocha y Crema.
    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)  # Envolvemos con el primer Mocha
    beverage2 = Mocha(beverage2)  # Envolvemos con el segundo Mocha
    beverage2 = Whip(beverage2)   # Envolvemos con Crema
    print(f"Pedido 2: {beverage2.get_description()} ${beverage2.cost():.2f}")

    # Pedido 3: Un HouseBlend con Soja, Mocha y Crema.
    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(f"Pedido 3: {beverage3.get_description()} ${beverage3.cost():.2f}")

    # Pedido 4: Un Espresso con Caramelo.
    beverage4 = Espresso()
    beverage4 = Caramel(beverage4)
    print(f"Pedido 4: {beverage4.get_description()} ${beverage4.cost():.2f}")

    # Pedido 5: Un HouseBlend con doble Caramelo.
    beverage5 = HouseBlend()
    beverage5 = Caramel(beverage5)
    beverage5 = Caramel(beverage5)
    print(f"Pedido 5: {beverage5.get_description()} ${beverage5.cost():.2f}")

    # Pedido 6: Un Descafeinado con Soja, Crema y Caramelo.
    beverage6 = Decaf()
    beverage6 = Soy(beverage6)
    beverage6 = Whip(beverage6)
    beverage6 = Caramel(beverage6)  # Triple Caramelo
    print(f"Pedido 6: {beverage6.get_description()} ${beverage6.cost():.2f}")


if __name__ == "__main__":
    main()