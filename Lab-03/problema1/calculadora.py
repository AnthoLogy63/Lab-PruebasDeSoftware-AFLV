# calculadora.py
# Módulo de operaciones aritméticas básicas
# Laboratorio 03 - Pruebas de Software
# Universidad Nacional de San Agustín

def sumar(a, b):
    """Retorna la suma de dos números.

    Args:
        a (int | float): Primer operando.
        b (int | float): Segundo operando.

    Returns:
        int | float: Resultado de a + b.
    """
    return a + b


def restar(a, b):
    """Retorna la diferencia entre dos números (a - b).

    Args:
        a (int | float): Minuendo.
        b (int | float): Sustraendo.

    Returns:
        int | float: Resultado de a - b.
    """
    return a - b


def multiplicar(a, b):
    """Retorna el producto de dos números.

    Args:
        a (int | float): Primer factor.
        b (int | float): Segundo factor.

    Returns:
        int | float: Resultado de a * b.
    """
    return a * b


def dividir(a, b):
    """Retorna el cociente de la división de a entre b.

    Args:
        a (int | float): Dividendo.
        b (int | float): Divisor.

    Returns:
        float: Resultado de a / b.

    Raises:
        ValueError: Si b es igual a cero.
    """
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b
