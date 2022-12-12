#!/usr/bin/python3

import model_dashboard
import pytest

# Test if the function exists
def test_model_dashboard():
    assert model_dashboard.build_model(0,0,0)

# Test if wrong type raises an exception
def test_type_taille():
    with pytest.raises(Exception):
        model_dashboard.build_model([1],1,1)

def test_type_nb_rooms():
    with pytest.raises(Exception):
        model_dashboard.build_model(1,[1],1)

def test_type_garden():
    with pytest.raises(Exception):
        model_dashboard.build_model(1,1,[1])

# Test if wrong value raises an exception
def test_taille_negative():
    with pytest.raises(Exception):
        model_dashboard.build_model(-1,1,1)

def test_nb_rooms_negative():
    with pytest.raises(Exception):
        model_dashboard.build_model(1,-1,1)

def test_garden_negative():
    with pytest.raises(Exception):
        model_dashboard.build_model(1,1,-1)

# Test if price is positive
def test_positive():
    price = model_dashboard.build_model(230,2,1)
    assert price > 0, f"The price should be greater than 0 expected, got: {price}"

# Test with values from the dataset
#def test_values():
#    assert model_dashboard.build_model(121.8065352034,2,0) == 256477.460465462
#    assert model_dashboard.build_model(205.9991686803,2,0) == 260972.164974894
#    assert model_dashboard.build_model(186.5591664373,2,0) == 256534.245748472
#    assert model_dashboard.build_model(187.1437846716,1,1) == 282674.291716703
#    assert model_dashboard.build_model(83.3153631652,2,1) == 266555.384156006
#    assert model_dashboard.build_model(161.7815803479,2,1) == 319158.41869534
#    assert model_dashboard.build_model(165.0130482406,2,1) == 320042.987510679
#    assert model_dashboard.build_model(193.7314621901,3,1) == 324222.967162171
#    assert model_dashboard.build_model(94.650536354,2,0) == 222231.558650076
