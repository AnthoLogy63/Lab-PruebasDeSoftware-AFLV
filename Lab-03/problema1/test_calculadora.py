# test_calculadora.py
# Suite de pruebas unitarias para el módulo calculadora.py
# Laboratorio 03 - Pruebas de Software
# Universidad Nacional de San Agustín
#
# Patrón aplicado : AAA (Arrange – Act – Assert)
# Técnicas de diseño: Partición de Equivalencia y Análisis de Valores Límite

import pytest
from calculadora import sumar, restar, multiplicar, dividir


# ═══════════════════════════════════════════════════════════════════
#  PRUEBAS PARA sumar()
# ═══════════════════════════════════════════════════════════════════

def test_sumar_enteros_positivos():
    """TC-01: Suma de dos enteros positivos."""
    # Arrange
    a, b = 5, 3
    # Act
    resultado = sumar(a, b)
    # Assert
    assert resultado == 8, f"Esperado 8 pero se obtuvo {resultado}"


def test_sumar_con_numero_negativo():
    """TC-02: Suma con un número negativo (resultado cero)."""
    # Arrange
    a, b = -4, 4
    # Act
    resultado = sumar(a, b)
    # Assert
    assert resultado == 0, f"Esperado 0 pero se obtuvo {resultado}"


# Prueba parametrizada – sumar (cubre casos adicionales de partición de equivalencia)
@pytest.mark.parametrize("a, b, esperado", [
    (5,    3,    8),       # TC-01 enteros positivos
    (-4,   4,    0),       # TC-02 negativo + positivo
    (0,    0,    0),       # borde: doble cero
    (-3,  -7,  -10),       # ambos negativos
    (1.5,  2.5, 4.0),      # decimales positivos
])
def test_sumar_parametrizado(a, b, esperado):
    assert sumar(a, b) == esperado


# ═══════════════════════════════════════════════════════════════════
#  PRUEBAS PARA restar()
# ═══════════════════════════════════════════════════════════════════

def test_restar_resultado_positivo():
    """TC-03: Resta con resultado positivo."""
    # Arrange
    a, b = 10, 3
    # Act
    resultado = restar(a, b)
    # Assert
    assert resultado == 7, f"Esperado 7 pero se obtuvo {resultado}"


def test_restar_resultado_negativo():
    """TC-04: Resta con resultado negativo (sustraendo mayor al minuendo)."""
    # Arrange
    a, b = 3, 10
    # Act
    resultado = restar(a, b)
    # Assert
    assert resultado == -7, f"Esperado -7 pero se obtuvo {resultado}"


# ═══════════════════════════════════════════════════════════════════
#  PRUEBAS PARA multiplicar()
# ═══════════════════════════════════════════════════════════════════

def test_multiplicar_por_cero():
    """TC-05: Multiplicación de cualquier número por cero debe retornar 0."""
    # Arrange
    a, b = 5, 0
    # Act
    resultado = multiplicar(a, b)
    # Assert
    assert resultado == 0, f"Esperado 0 pero se obtuvo {resultado}"


def test_multiplicar_decimales():
    """TC-06: Multiplicación de número decimal con entero."""
    # Arrange
    a, b = 2.5, 4
    # Act
    resultado = multiplicar(a, b)
    # Assert
    assert resultado == 10.0, f"Esperado 10.0 pero se obtuvo {resultado}"


# ═══════════════════════════════════════════════════════════════════
#  PRUEBAS PARA dividir()
# ═══════════════════════════════════════════════════════════════════

def test_dividir_exacta():
    """TC-07: División exacta (sin residuo)."""
    # Arrange
    a, b = 10, 2
    # Act
    resultado = dividir(a, b)
    # Assert
    assert resultado == 5.0, f"Esperado 5.0 pero se obtuvo {resultado}"


def test_dividir_por_cero_lanza_excepcion():
    """TC-08: División por cero debe lanzar ValueError con el mensaje correcto."""
    # Arrange
    a, b = 5, 0
    # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        dividir(a, b)
    assert "No se puede dividir entre cero" in str(exc_info.value)


def test_dividir_resultado_decimal():
    """TC-09: División con resultado decimal (no exacta)."""
    # Arrange
    a, b = 7, 2
    # Act
    resultado = dividir(a, b)
    # Assert
    assert resultado == 3.5, f"Esperado 3.5 pero se obtuvo {resultado}"


# ═══════════════════════════════════════════════════════════════════
#  PRUEBA PARAMETRIZADA INTEGRAL (todas las operaciones)
# ═══════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("operacion, a, b, esperado", [
    ("sumar",       5,    3,    8),
    ("restar",      10,   3,    7),
    ("restar",      3,    10,  -7),
    ("multiplicar", 5,    0,    0),
    ("multiplicar", 2.5,  4,   10.0),
    ("dividir",     10,   2,    5.0),
    ("dividir",     7,    2,    3.5),
])
def test_operaciones_parametrizadas(operacion, a, b, esperado):
    """Prueba parametrizada que cubre las cuatro operaciones con múltiples conjuntos de datos."""
    operaciones = {
        "sumar":       sumar,
        "restar":      restar,
        "multiplicar": multiplicar,
        "dividir":     dividir,
    }
    resultado = operaciones[operacion](a, b)
    assert abs(resultado - esperado) < 1e-9, (
        f"{operacion}({a}, {b}): esperado {esperado}, obtuvo {resultado}"
    )
