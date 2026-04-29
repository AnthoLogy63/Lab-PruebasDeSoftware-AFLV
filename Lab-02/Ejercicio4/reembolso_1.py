def calcular_reembolso(monto, horas, es_vip):
    """
    Calcula el monto de reembolso al cancelar una reserva de hotel.

    Parámetros:
        monto (float): Monto total de la reserva. Debe ser >= 0.
        horas (float): Horas de anticipación con que se cancela. Debe ser >= 0.
        es_vip (bool): Indica si el cliente tiene estado VIP.

    Retorna:
        float: Monto a reembolsar.

    Lanza:
        ValueError: Si el monto es negativo.
        TypeError: Si los tipos de datos no son correctos.
    """
    # Validación de robustez
    if not isinstance(monto, (int, float)):
        raise TypeError("El monto debe ser un número.")
    if monto < 0:
        raise ValueError("El monto de la reserva no puede ser negativo.")
    if not isinstance(horas, (int, float)):
        raise TypeError("Las horas deben ser un número.")
    if horas < 0:
        raise ValueError("Las horas de anticipación no pueden ser negativas.")
    if not isinstance(es_vip, bool):
        raise TypeError("El parámetro es_vip debe ser booleano.")

    # Lógica de negocio: regla VIP tiene PRIORIDAD sobre última hora
    if horas > 72:
        return monto * 1.00  # 100% de reembolso
    elif horas >= 24:
        return monto * 0.50  # 50% de reembolso
    else:
        # Menos de 24 horas
        if es_vip:
            return monto * 0.50  # VIP: mínimo 50%
        return monto * 0.00     # No VIP: 0% de reembolso
