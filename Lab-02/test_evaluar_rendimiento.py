import pytest
from evaluar_rendimiento import evaluar_rendimiento

def test_insuficiente():
    assert evaluar_rendimiento(5) == "Insuficiente"

def test_regular():
    assert evaluar_rendimiento(13) == "Regular"

def test_excelente():
    assert evaluar_rendimiento(18) == "Excelente"

def test_limite_10():
    assert evaluar_rendimiento(10) == "Insuficiente"

def test_limite_11():
    assert evaluar_rendimiento(11) == "Regular"

def test_limite_15():
    assert evaluar_rendimiento(15) == "Regular"

def test_limite_16():
    assert evaluar_rendimiento(16) == "Excelente"

def test_limite_0():
    assert evaluar_rendimiento(0) == "Insuficiente"

def test_limite_20():
    assert evaluar_rendimiento(20) == "Excelente"

def test_menor_cero():
    with pytest.raises(ValueError):
        evaluar_rendimiento(-1)

def test_mayor_20():
    with pytest.raises(ValueError):
        evaluar_rendimiento(21)