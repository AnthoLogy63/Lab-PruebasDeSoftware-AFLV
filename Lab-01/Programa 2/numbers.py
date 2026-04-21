while True:
    entrada_cantidad = input("¿Cuántos números desea ingresar? ").strip()

    if entrada_cantidad == "":
        print("Error: Ingrese un número entero válido mayor que 0.")
        continue

    try:
        cantidad = int(entrada_cantidad)

        if cantidad <= 0:
            print("Error: La cantidad debe ser mayor que 0.")
            continue

        break
    except ValueError:
        print("Error: La cantidad de números debe ser un número entero válido.")

numeros = []

for i in range(cantidad):
    while True:
        entrada_num = input(f"Ingrese el número entero {i + 1}: ").strip()

        if entrada_num == "":
            print("Entrada no válida. Por favor, ingrese un número entero.")
            continue

        try:
            num = int(entrada_num)
            numeros.append(num)
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

print("\nListado de números y su clasificación:")
for num in numeros:
    if num % 2 == 0:
        paridad = "par"
    else:
        paridad = "impar"
    print(f"{num}: {paridad}")