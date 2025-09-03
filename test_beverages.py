# -*- coding: utf-8 -*-
import pytest
from beverages import Espresso, DarkRoast, HouseBlend, Decaf, Beverage
from condiments import Mocha, Whip, Soy, Caramel
from builder import build_beverage


def test_espresso_simple():
    bebida = Espresso()
    assert bebida.get_description() == "Espresso"
    assert pytest.approx(bebida.cost(), 0.01) == 1.99

def test_darkroast_doble_mocha_whip():
    bebida = DarkRoast()
    bebida = Mocha(bebida)
    bebida = Mocha(bebida)
    bebida = Whip(bebida)
    assert bebida.get_description() == "Caf� Dark Roast, Mocha, Mocha, Crema"
    # 0.99 + 0.20 + 0.20 + 0.10 = 1.49
    assert pytest.approx(bebida.cost(), 0.01) == 1.49

def test_houseblend_soy_mocha_whip():
    bebida = HouseBlend()
    bebida = Soy(bebida)
    bebida = Mocha(bebida)
    bebida = Whip(bebida)
    assert bebida.get_description() == "Caf� de la Casa, Soja, Mocha, Crema"
    # 0.89 + 0.10 + 0.20 + 0.10 = 1.29
    assert pytest.approx(bebida.cost(), 0.01) == 1.29

def test_houseblend_doble_caramel():
    bebida = HouseBlend()
    bebida = Caramel(bebida)
    bebida = Caramel(bebida)
    assert bebida.get_description() == "Caf� de la Casa, Caramelo, Caramelo"
    # 0.89 + 0.20 + 0.20 = 1.29
    assert pytest.approx(bebida.cost(), 0.01) == 1.29

def test_espresso_grande_caramel():
    bebida = Espresso()
    bebida.set_size(Beverage.GRANDE)
    bebida = Caramel(bebida)
    assert bebida.get_description() == "Espresso, Caramelo"
    # Espresso 1.99 + Caramel GRANDE 0.25 = 2.24
    assert bebida.get_size() == "Grande"
    assert pytest.approx(bebida.cost(), 0.01) == 2.24

def test_build_beverage_darkroast_tall_soy_whip():
    bebida = build_beverage("DarkRoast", "Tall", ["Soy", "Whip"])
    assert bebida.get_description() == "Caf� Dark Roast, Soja, Crema"
    # 0.99 + Soy Tall 0.10 + Whip Tall 0.10 = 1.19
    assert bebida.get_size() == "Tall"
    assert pytest.approx(bebida.cost(), 0.01) == 1.19