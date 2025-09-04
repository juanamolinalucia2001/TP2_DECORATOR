import pytest
from beverages import Espresso, DarkRoast, HouseBlend, Decaf, Beverage
from condiments import Mocha, Whip, Soy, Caramel
from condiments_extra import Honey, Cacao, Cinnamon, Vanilla
from builder import build_beverage
from size import Size
from pretty_print import PrettyPrint

def test_espresso_simple():
    bebida = Espresso()
    assert bebida.get_description() == "Espresso"
    # Espresso 1.99 = 1.99
    assert pytest.approx(bebida.cost(), 0.01) == 1.99

def test_darkroast_doble_mocha_whip():
    bebida = DarkRoast()
    bebida = Mocha(bebida)
    bebida = Mocha(bebida)
    bebida = Whip(bebida)
    assert bebida.get_description() == "Café Dark Roast, Mocha, Mocha, Crema"
    # DarkRoast 0.99 + Mocha Tall 0.25 + Mocha Tall 0.25 + Whip Tall 0.15 = 1.64
    assert pytest.approx(bebida.cost(), 0.01) == 1.64

def test_houseblend_soy_mocha_whip():
    bebida = HouseBlend()
    bebida = Soy(bebida)
    bebida = Mocha(bebida)
    bebida = Whip(bebida)
    assert bebida.get_description() == "Café de la Casa, Soja, Mocha, Crema"
    # HouseBlend 0.89 + Soy Tall 0.15 + Mocha Tall 0.25 + Whip Tall 0.15 = 1.44
    assert pytest.approx(bebida.cost(), 0.01) == 1.44

def test_houseblend_doble_caramel():
    bebida = HouseBlend()
    bebida = Caramel(bebida)
    bebida = Caramel(bebida)
    assert bebida.get_description() == "Café de la Casa, Caramelo, Caramelo"
    # HouseBlend 0.89 + Caramel Tall 0.25 + Caramel Tall 0.25 = 1.39
    assert pytest.approx(bebida.cost(), 0.01) == 1.39

def test_espresso_grande_caramel():
    bebida = Espresso()
    bebida.set_size(Size.GRANDE)
    bebida = Caramel(bebida)
    assert bebida.get_description() == "Espresso, Caramelo"
    # Espresso 1.99 + Caramel GRANDE 0.25*1.15 = 2.29
    assert bebida.get_size() == Size.GRANDE
    assert pytest.approx(bebida.cost(), 0.01) == 2.29

def test_espresso_con_honey():
    bebida = Espresso()
    bebida = Honey(bebida)
    assert bebida.get_description() == "Espresso, Miel"
    # Espresso 1.99 + Honey Tall 0.30 = 2.29
    assert pytest.approx(bebida.cost(), 0.01) == 2.29

def test_builder_houseblend_soy_mocha_whip_grande():
    bebida = build_beverage("HouseBlend", size=Size.GRANDE, condiments=["Soy", "Mocha", "Whip"])
    assert bebida.get_description() == "Café de la Casa, Soja, Mocha, Crema"
    assert bebida.get_size() == Size.GRANDE
    # HouseBlend 0.89 + Soy GRANDE 0.15*1.15 + Mocha GRANDE 0.25*1.15 + Whip GRANDE 0.15*1.15 = 1.52
    assert pytest.approx(bebida.cost(), 0.01) == 1.52

def test_builder_houseblend_doble_caramel():
    bebida = build_beverage("HouseBlend", condiments=["Caramel", "Caramel"])
    assert bebida.get_description() == "Café de la Casa, Caramelo, Caramelo"
    # HouseBlend 0.89 + Caramel Tall 0.25 + Caramel Tall 0.25 = 1.39
    assert pytest.approx(bebida.cost(), 0.01) == 1.39

def test_pretty_print():
    # Doble Mocha
    bebida = Whip(Mocha(Mocha(DarkRoast())))
    pp = PrettyPrint(bebida)
    assert pp.get_description() == "Café Dark Roast, Double Mocha, Crema"
    # DarkRoast 0.99 + Mocha Tall 0.25 + Mocha Tall 0.25 + Whip Tall 0.15 = 1.64
    assert pytest.approx(pp.cost(), 0.01) == bebida.cost()

    # Triple Mocha
    bebida2 = Whip(Mocha(Mocha(Mocha(DarkRoast()))))
    pp2 = PrettyPrint(bebida2)
    assert pp2.get_description() == "Café Dark Roast, Triple Mocha, Crema"
    # DarkRoast 0.99 + Mocha Tall 0.25*3 + Whip Tall 0.15 = 1.89
    assert pytest.approx(pp2.cost(), 0.01) == bebida2.cost()

    # Cuádruple Caramel
    bebida3 = Caramel(Caramel(Caramel(Caramel(HouseBlend()))))
    pp3 = PrettyPrint(bebida3)
    assert pp3.get_description() == "Café de la Casa, 4x Caramelo"
    # HouseBlend 0.89 + Caramel Tall 0.25*4 = 1.89
    assert pytest.approx(pp3.cost(), 0.01) == bebida3.cost()

