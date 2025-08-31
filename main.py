from beverages import Espresso, DarkRoast, HouseBlend, Decaf, Beverage
from condiments import Mocha, Whip, Soy, Caramel

def main():
    print("Bienvenido a Mensita UNSAM Coffee!")
    print("--- Preparando pedidos ---")

    # Pedido 1: Espresso simple
    beverage1 = Espresso()
    print(f"Pedido 1: {beverage1.get_description()} (${beverage1.cost():.2f})")

    # Pedido 2: DarkRoast + doble Mocha + Crema
    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(f"Pedido 2: {beverage2.get_description()} (${beverage2.cost():.2f})")

    # Pedido 3: HouseBlend + Soy + Mocha + Whip
    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(f"Pedido 3: {beverage3.get_description()} (${beverage3.cost():.2f})")

    # Pedido 4: Espresso + Caramel
    beverage4 = Espresso()
    beverage4 = Caramel(beverage4)
    print(f"Pedido 4: {beverage4.get_description()} (${beverage4.cost():.2f})")

    # Pedido 5: HouseBlend + doble Caramel
    beverage5 = HouseBlend()
    beverage5 = Caramel(beverage5)
    beverage5 = Caramel(beverage5)
    print(f"Pedido 5: {beverage5.get_description()} (${beverage5.cost():.2f})")

    # Pedido 6: Decaf + Soy + Whip + Caramel
    beverage6 = Decaf()
    beverage6 = Soy(beverage6)
    beverage6 = Whip(beverage6)
    beverage6 = Caramel(beverage6)
    print(f"Pedido 6: {beverage6.get_description()} (${beverage6.cost():.2f})")

    # Pedidos con tamaños
    # Pedido A: HouseBlend Venti + Soy
    beverageA = HouseBlend()
    beverageA.set_size(Beverage.VENTI)
    beverageA = Soy(beverageA)
    print(f"Pedido VENTI: {beverageA.get_description()} ({beverageA.get_size()}) ${beverageA.cost():.2f}")

    # Pedido B: Espresso Grande + Caramel
    beverageB = Espresso()
    beverageB.set_size(Beverage.GRANDE)
    beverageB = Caramel(beverageB)
    print(f"Pedido GRANDE: {beverageB.get_description()} ({beverageB.get_size()}) ${beverageB.cost():.2f}")

    # Pedido C: DarkRoast Tall + Soy + Whip
    beverageC = DarkRoast()
    beverageC.set_size(Beverage.TALL)
    beverageC = Soy(beverageC)
    beverageC = Whip(beverageC)
    print(f"Pedido TALL: {beverageC.get_description()} ({beverageC.get_size()}) ${beverageC.cost():.2f}")

if __name__ == "__main__":
    main()
