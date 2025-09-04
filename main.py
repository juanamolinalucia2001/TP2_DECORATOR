from beverages import Espresso, DarkRoast, HouseBlend, Decaf
from condiments import Mocha, Whip, Soy, Caramel, Milk
from pretty_print import PrettyPrint
from size import Size
from builder import build_beverage

def main():
    print("Bienvenido a Mensita UNSAM Coffee!")
    print("--- Preparando pedidos ---")

    # Pedido 1: Espresso simple
    b1 = Espresso()
    print(f"Pedido 1: {b1.get_description()} (${b1.cost():.2f}) tamaño {b1.get_size().label}")

    # Pedido 2: DarkRoast + doble Mocha + Crema
    b2 = Whip(Mocha(Mocha(DarkRoast())))
    print(f"Pedido 2: {b2.get_description()} (${b2.cost():.2f})")

    # Pedido 3: HouseBlend + Soy + Mocha + Whip
    b3 = Whip(Mocha(Soy(HouseBlend())))
    print(f"Pedido 3: {b3.get_description()} (${b3.cost():.2f})")

    # Pedido 4: Espresso + Caramel
    b4 = Caramel(Espresso())
    print(f"Pedido 4: {b4.get_description()} (${b4.cost():.2f})")

    # Pedido 5: HouseBlend + doble Caramel
    b5 = Caramel(Caramel(HouseBlend()))
    print(f"Pedido 5: {b5.get_description()} (${b5.cost():.2f})")

    # Pedido 6: Decaf + Soy + Whip + Caramel (cambiando size en la cadena decorada)
    b6 = Caramel(Whip(Soy(Decaf())))
    b6.set_size(Size.GRANDE)   # <- Propaga hacia adentro (arreglo aplicado)
    print(f"Pedido 6: {b6.get_description()} ({b6.get_size().label}) ${b6.cost():.2f}")

    # Pedidos con tamaños
    # Pedido A: HouseBlend Venti + Soy
    bA = Soy(HouseBlend())
    bA.set_size(Size.VENTI)
    print(f"Pedido VENTI: {bA.get_description()} ({bA.get_size().label}) ${bA.cost():.2f}")

    # Pedido B: Espresso Grande + Caramel
    bB = Caramel(Espresso())
    bB.set_size(Size.GRANDE)
    print(f"Pedido GRANDE: {bB.get_description()} ({bB.get_size().label}) ${bB.cost():.2f}")

    # Pedido C: DarkRoast Tall + Soy + Whip
    bC = Whip(Soy(DarkRoast()))
    bC.set_size(Size.TALL)
    print(f"Pedido TALL: {bC.get_description()} ({bC.get_size().label}) ${bC.cost():.2f}")


    # Pedido D: DarkRoast Venti + Soy + Whip 
    bD = build_beverage("DarkRoast", Size.VENTI,condiments=["Soy", "Whip"])
    print(f"Pedido VENTI: {bD.get_description()} ({bD.get_size().label}) ${bD.cost():.2f}")
    
    #Comparacion con prettyprint
    # Pedido E: DarkRoast TALL + doble Mocha + triple Crema
    bE = build_beverage("DarkRoast", Size.TALL,condiments=["Mocha", "Mocha","Whip", "Whip", "Whip"])
    print(f"Pedido sin prettyprint: {bE.get_description()} ({bE.get_size().label}) ${bE.cost():.2f}")
    pretty_bE = PrettyPrint(bE)
    print(f"Pedido con prettyprint: {pretty_bE.get_description()} ({pretty_bE.get_size().label}) ${pretty_bE.cost():.2f}")

if __name__ == "__main__":
    main()
