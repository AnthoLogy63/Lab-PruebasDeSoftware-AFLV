import pytest
from reembolso_1 import calcular_reembolso

# ============================================================
# FASE RED: Pruebas escritas ANTES de implementar la función.
# Estas pruebas fallarán inicialmente (ciclo TDD - Red).
# ============================================================

# --- CLASE DE EQUIVALENCIA: Cancelación con mucha antelación (> 72 horas) ---
def test_cancelacion_mayor_72h_devuelve_100_porciento():
    """Cliente normal, cancela con 100 horas: debe recibir el 100%."""
    assert calcular_reembolso(200.0, 100, False) == 200.0

def test_cancelacion_mayor_72h_vip_devuelve_100_porciento():
    """Cliente VIP, cancela con 100 horas: también recibe el 100%."""
    assert calcular_reembolso(200.0, 100, True) == 200.0

# --- CLASE DE EQUIVALENCIA: Cancelación media (24 a 72 horas) ---
def test_cancelacion_media_devuelve_50_porciento():
    """Cliente normal, cancela con 48 horas: debe recibir el 50%."""
    assert calcular_reembolso(200.0, 48, False) == 100.0

def test_cancelacion_media_vip_devuelve_50_porciento():
    """Cliente VIP, cancela con 48 horas: también recibe el 50%."""
    assert calcular_reembolso(200.0, 48, True) == 100.0

# --- CLASE DE EQUIVALENCIA: Cancelación de última hora (< 24 horas) ---
def test_cancelacion_ultima_hora_no_vip_devuelve_0():
    """Cliente normal, cancela con 2 horas: debe recibir el 0%."""
    assert calcular_reembolso(200.0, 2, False) == 0.0

def test_cancelacion_ultima_hora_vip_devuelve_50_porciento():
    """Cliente VIP, cancela con 2 horas: regla VIP le asegura el 50%."""
    assert calcular_reembolso(200.0, 2, True) == 100.0

# ============================================================
# VALORES LÍMITE (según Myers - Análisis de Valor Límite)
# Probamos los puntos exactos de frontera: 24 y 72 horas.
# ============================================================

def test_valor_limite_exacto_24h_normal():
    """Exactamente 24 horas: debe caer en la clase 'media' (50%)."""
    assert calcular_reembolso(200.0, 24, False) == 100.0

def test_valor_limite_justo_antes_24h():
    """23.9 horas: última hora, cliente normal recibe 0%."""
    assert calcular_reembolso(200.0, 23.9, False) == 0.0

def test_valor_limite_exacto_72h_normal():
    """Exactamente 72 horas: debe caer en la clase 'media' (50%)."""
    assert calcular_reembolso(200.0, 72, False) == 100.0

def test_valor_limite_justo_sobre_72h():
    """72.1 horas: antelación alta, recibe 100%."""
    assert calcular_reembolso(200.0, 72.1, False) == 200.0

def test_valor_limite_0h():
    """0 horas (cancela al momento): cliente normal recibe 0%."""
    assert calcular_reembolso(200.0, 0, False) == 0.0

def test_valor_limite_0h_vip():
    """0 horas, cliente VIP: recibe el 50% garantizado."""
    assert calcular_reembolso(200.0, 0, True) == 100.0

# ============================================================
# PRUEBAS DE ROBUSTEZ (Error Guessing - Myers)
# Entradas inválidas que el sistema debe rechazar con ValueError.
# ============================================================

def test_monto_negativo_lanza_error():
    """Monto negativo: debe lanzar ValueError."""
    with pytest.raises(ValueError):
        calcular_reembolso(-100.0, 50, False)

def test_monto_cero_es_valido():
    """Monto de 0 es técnicamente válido: devuelve 0."""
    assert calcular_reembolso(0, 50, False) == 0.0

def test_horas_negativas_lanza_error():
    """Horas negativas no tienen sentido: debe lanzar ValueError."""
    with pytest.raises(ValueError):
        calcular_reembolso(200.0, -5, False)

def test_monto_tipo_incorrecto_lanza_error():
    """Monto de tipo string: debe lanzar TypeError."""
    with pytest.raises(TypeError):
        calcular_reembolso("doscientos", 50, False)

def test_es_vip_tipo_incorrecto_lanza_error():
    """es_vip de tipo string: debe lanzar TypeError."""
    with pytest.raises(TypeError):
        calcular_reembolso(200.0, 50, "si")
