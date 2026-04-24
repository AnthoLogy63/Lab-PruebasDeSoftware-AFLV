while True:
    entrada_base = input("Ingrese la base del rectángulo: ").strip()

    if entrada_base == "":
        print("Error: Ingrese un valor numérico válido para la base.")
        continue

    try:
        base = float(entrada_base)

        if base <= 0:
            print("Error: La base debe ser mayor que 0.")
            continue

        break
    except ValueError:
        print("Error: La base debe ser un número válido.")

while True:
    entrada_altura = input("Ingrese la altura del rectángulo: ").strip()

    if entrada_altura == "":
        print("Error: Ingrese un valor numérico válido para la altura.")
        continue

    try:
        altura = float(entrada_altura)

        if altura <= 0:
            print("Error: La altura debe ser mayor que 0.")
            continue

        break
    except ValueError:
        print("Error: La altura debe ser un número válido.")

area = base * altura

print("\nResultado del cálculo:")
print(f"Base: {base}")
print(f"Altura: {altura}")
print(f"Área: {area}")

