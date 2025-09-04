# -*- coding: utf-8 -*-
import pytest
from beverages import Espresso, DarkRoast, HouseBlend, Decaf, Beverage
from condiments import Mocha, Whip, Soy, Caramel
from builder import build_beverage
from size import Size


def test_espresso_simple():
    bebida = Espresso()
    assert bebida.get_description() == "Espresso"
    assert pytest.approx(bebida.cost(), 0.01) == 1.99

def test_darkroast_doble_mocha_whip():
    bebida = DarkRoast()
    bebida = Mocha(bebida)
    bebida = Mocha(bebida)
    bebida = Whip(bebida)
    assert bebida.get_description() == "Café Dark Roast, Mocha, Mocha, Crema"
    # 0.99 + 0.20 + 0.20 + 0.10 = 1.49
    assert pytest.approx(bebida.cost(), 0.01) == 1.64

def test_houseblend_soy_mocha_whip():
    bebida = HouseBlend()
    bebida = Soy(bebida)
    bebida = Mocha(bebida)
    bebida = Whip(bebida)
    assert bebida.get_description() == "Café de la Casa, Soja, Mocha, Crema"
    # 0.89 + 0.10 + 0.20 + 0.10 = 1.29
    assert pytest.approx(bebida.cost(), 0.01) == 1.44

def test_houseblend_doble_caramel():
    bebida = HouseBlend()
    bebida = Caramel(bebida)
    bebida = Caramel(bebida)
    assert bebida.get_description() == "Café de la Casa, Caramelo, Caramelo"
    # 0.89 + 0.20 + 0.20 = 1.29
    assert pytest.approx(bebida.cost(), 0.01) == 1.39

def test_espresso_grande_caramel():
    bebida = Espresso()
    bebida.set_size(Size.GRANDE)
    bebida = Caramel(bebida)
    assert bebida.get_description() == "Espresso, Caramelo"
    # Espresso 1.99 + Caramel GRANDE 0.25 = 2.24
    assert bebida.get_size() == Size.GRANDE
    assert pytest.approx(bebida.cost(), 0.01) == 2.27
