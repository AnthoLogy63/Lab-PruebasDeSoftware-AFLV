def evaluar_rendimiento(nota):
    if not isinstance(nota, (int, float)):
        raise TypeError("La nota debe ser numérica")
    if isinstance(nota, bool):
        raise TypeError("La nota no puede ser booleana")
    if nota != nota:
        raise ValueError("La nota no puede ser NaN")
    if nota == float("inf") or nota == float("-inf"):
        raise ValueError("La nota no puede ser infinita")

    if not 0 <= nota <= 20:
        raise ValueError("Nota fuera de rango")

    if nota <= 10:
        return "Insuficiente"
    if nota <= 15:
        return "Regular"
    return "Excelente"