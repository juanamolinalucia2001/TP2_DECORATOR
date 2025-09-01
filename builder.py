from beverages import Espresso, DarkRoast, HouseBlend, Decaf, Beverage
from condiments import Mocha, Whip, Soy, Caramel

def build_beverage(base, size=None, condiments=None):
    """
    Construye el pedido en base a la bebida, tamaño y adicionales
    """
    bebidas = {"Espresso": Espresso(), "DarkRoast": DarkRoast(), "HouseBlend": HouseBlend(), "Decaf": Decaf()}
    condimentos ={"Mocha": Mocha, "Whip": Whip, "Soy": Soy, "Caramel": Caramel}
    tamaños = {"Tall": Beverage.TALL, "Grande": Beverage.GRANDE, "Venti": Beverage.VENTI} 

    bebida = bebidas[base]
    if size is not None:
        bebida.set_size(tamaños[size])
    if condiments is not None:
        for c in condiments:
            bebida = condimentos[c](bebida)

    return bebida