import pytest
from reembolso import calcular_reembolso  # Fallará: el módulo aún no existe

# === CLASES DE EQUIVALENCIA ===

def test_cancelacion_mayor_72h_devuelve_100_porciento():
    """Cliente normal, 100 horas: recibe el 100%."""
    assert calcular_reembolso(200.0, 100, False) == 200.0

def test_cancelacion_media_devuelve_50_porciento():
    """Cliente normal, 48 horas: recibe el 50%."""
    assert calcular_reembolso(200.0, 48, False) == 100.0

def test_cancelacion_ultima_hora_no_vip_devuelve_0():
    """Cliente normal, 2 horas: recibe el 0%."""
    assert calcular_reembolso(200.0, 2, False) == 0.0

def test_cancelacion_ultima_hora_vip_devuelve_50_porciento():
    """Cliente VIP, 2 horas: regla VIP garantiza el 50%."""
    assert calcular_reembolso(200.0, 2, True) == 100.0

# === VALORES LÍMITE (Myers) ===

def test_valor_limite_exacto_24h_normal():
    assert calcular_reembolso(200.0, 24, False) == 100.0

def test_valor_limite_justo_antes_24h():
    assert calcular_reembolso(200.0, 23.9, False) == 0.0

def test_valor_limite_exacto_72h_normal():
    assert calcular_reembolso(200.0, 72, False) == 100.0

def test_valor_limite_justo_sobre_72h():
    assert calcular_reembolso(200.0, 72.1, False) == 200.0

def test_valor_limite_0h():
    assert calcular_reembolso(200.0, 0, False) == 0.0

def test_valor_limite_0h_vip():
    assert calcular_reembolso(200.0, 0, True) == 100.0

# === ROBUSTEZ — ERROR GUESSING (Myers) ===

def test_monto_negativo_lanza_error():
    with pytest.raises(ValueError):
        calcular_reembolso(-100.0, 50, False)

def test_monto_cero_es_valido():
    assert calcular_reembolso(0, 50, False) == 0.0

def test_horas_negativas_lanza_error():
    with pytest.raises(ValueError):
        calcular_reembolso(200.0, -5, False)

def test_monto_tipo_incorrecto_lanza_error():
    with pytest.raises(TypeError):
        calcular_reembolso("doscientos", 50, False)

def test_es_vip_tipo_incorrecto_lanza_error():
    with pytest.raises(TypeError):
        calcular_reembolso(200.0, 50, "si")


