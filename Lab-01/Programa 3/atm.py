saldo = 1000.0

def mostrar_menu():
    print("\n===== CAJERO AUTOMÁTICO =====")
    print(f"Saldo actual: S/. {saldo:.2f}")
    print("1. Consultar Saldo")
    print("2. Depositar Dinero")
    print("3. Retirar Dinero")
    print("4. Salir")
    print("=============================")

while True:
    mostrar_menu()

    entrada_opcion = input("Seleccione una opción: ").strip()

    if entrada_opcion == "":
        print("Error: Ingrese una opción válida (1-4).")
        continue

    if entrada_opcion not in ["1", "2", "3", "4"]:
        print("Error: Opción no válida. Ingrese un número del 1 al 4.")
        continue

    opcion = int(entrada_opcion)

    if opcion == 1:
        print(f"\nSu saldo actual es: S/. {saldo:.2f}")

    elif opcion == 2:
        while True:
            entrada_monto = input("Ingrese el monto a depositar: S/. ").strip()

            if entrada_monto == "":
                print("Error: Ingrese un monto válido.")
                continue

            try:
                monto = float(entrada_monto)

                if monto <= 0:
                    print("Error: El monto a depositar debe ser mayor que 0.")
                    continue

                saldo += monto
                print(f"Depósito exitoso. Nuevo saldo: S/. {saldo:.2f}")
                break

            except ValueError:
                print("Error: El monto debe ser un número válido.")

    elif opcion == 3:
        while True:
            entrada_monto = input("Ingrese el monto a retirar: S/. ").strip()

            if entrada_monto == "":
                print("Error: Ingrese un monto válido.")
                continue

            try:
                monto = float(entrada_monto)

                if monto <= 0:
                    print("Error: El monto a retirar debe ser mayor que 0.")
                    continue

                if monto > saldo:
                    print(f"Error: Fondos insuficientes. Su saldo es S/. {saldo:.2f}")
                    continue

                saldo -= monto
                print(f"Retiro exitoso. Nuevo saldo: S/. {saldo:.2f}")
                break

            except ValueError:
                print("Error: El monto debe ser un número válido.")

    elif opcion == 4:
        print("Gracias por usar el cajero. ¡Hasta luego!")
        break
