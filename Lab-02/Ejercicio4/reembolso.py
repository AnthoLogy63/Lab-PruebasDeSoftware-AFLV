# reembolso.py — VERSION DEFECTUOSA (ilustra el defecto que TDD detecta)
def calcular_reembolso(monto, horas, es_vip):
    if horas >= 24:       # ERROR: esta condición captura también horas >= 72
        return monto * 0.50
    elif horas > 72:      # Esta rama nunca se ejecuta
        return monto * 1.00
    else:
        return monto * 0.00
