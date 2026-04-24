import unittest
import subprocess
import sys

class TestATM(unittest.TestCase):

    def run_script(self, input_data):
        result = subprocess.run(
            [sys.executable, "atm.py"],
            input=input_data,
            capture_output=True,
            text=True
        )
        return result.stdout, result.stderr

    # ───────────── CASO 1.1 – Consultar saldo inicial ─────────────
    def test_consultar_saldo_inicial(self):
        nombre = "Prueba de consulta de saldo inicial"
        try:
            stdout, _ = self.run_script("1\n4\n")
            self.assertIn("1000.00", stdout)
            print(f"{nombre} - SUPERADA")
        except AssertionError:
            print(f"{nombre} - NO SUPERADA")
            raise

    # ───────────── CASO 2.1 – Depósito válido ─────────────
    def test_deposito_valido(self):
        nombre = "Prueba de depósito válido"
        try:
            stdout, _ = self.run_script("2\n500\n4\n")
            self.assertIn("1500.00", stdout)
            print(f"{nombre} - SUPERADA")
        except AssertionError:
            print(f"{nombre} - NO SUPERADA")
            raise

    # ───────────── CASO 2.2 – Depósito decimal ─────────────
    def test_deposito_decimal(self):
        nombre = "Prueba de depósito con monto decimal"
        try:
            stdout, _ = self.run_script("2\n250.50\n4\n")
            self.assertIn("1250.50", stdout)
            print(f"{nombre} - SUPERADA")
        except AssertionError:
            print(f"{nombre} - NO SUPERADA")
            raise

    # ───────────── CASO 3.1 – Retiro válido ─────────────
    def test_retiro_valido(self):
        nombre = "Prueba de retiro válido"
        try:
            stdout, _ = self.run_script("3\n200\n4\n")
            self.assertIn("800.00", stdout)
            print(f"{nombre} - SUPERADA")
        except AssertionError:
            print(f"{nombre} - NO SUPERADA")
            raise

    # ───────────── CASO 3.2 – Retiro exacto al saldo ─────────────
    def test_retiro_exacto_saldo(self):
        nombre = "Prueba de retiro exacto al saldo disponible"
        try:
            stdout, _ = self.run_script("3\n1000\n4\n")
            self.assertIn("0.00", stdout)
            print(f"{nombre} - SUPERADA")
        except AssertionError:
            print(f"{nombre} - NO SUPERADA")
            raise

    # ───────────── CASO 4.1 – Retiro mayor al saldo ─────────────
    def test_retiro_mayor_saldo(self):
        nombre = "Prueba de retiro mayor al saldo disponible"
        try:
            stdout, _ = self.run_script("3\n1500\n200\n4\n")
            self.assertIn("Error", stdout)
            self.assertIn("800.00", stdout)
            print(f"{nombre} - SUPERADA")
        except AssertionError:
            print(f"{nombre} - NO SUPERADA")
            raise

    # ───────────── CASO 5.1 – Depósito negativo ─────────────
    def test_deposito_negativo(self):
        nombre = "Prueba de depósito con monto negativo"
        try:
            stdout, _ = self.run_script("2\n-100\n500\n4\n")
            self.assertIn("Error", stdout)
            print(f"{nombre} - SUPERADA")
        except AssertionError:
            print(f"{nombre} - NO SUPERADA")
            raise

    # ───────────── CASO 5.2 – Retiro negativo ─────────────
    def test_retiro_negativo(self):
        nombre = "Prueba de retiro con monto negativo"
        try:
            stdout, _ = self.run_script("3\n-50\n100\n4\n")
            self.assertIn("Error", stdout)
            print(f"{nombre} - SUPERADA")
        except AssertionError:
            print(f"{nombre} - NO SUPERADA")
            raise

    # ───────────── CASO 6.1 – Depósito igual a cero ─────────────
    def test_deposito_cero(self):
        nombre = "Prueba de depósito con monto cero"
        try:
            stdout, _ = self.run_script("2\n0\n100\n4\n")
            self.assertIn("Error", stdout)
            print(f"{nombre} - SUPERADA")
        except AssertionError:
            print(f"{nombre} - NO SUPERADA")
            raise

    # ───────────── CASO 6.2 – Retiro igual a cero ─────────────
    def test_retiro_cero(self):
        nombre = "Prueba de retiro con monto cero"
        try:
            stdout, _ = self.run_script("3\n0\n100\n4\n")
            self.assertIn("Error", stdout)
            print(f"{nombre} - SUPERADA")
        except AssertionError:
            print(f"{nombre} - NO SUPERADA")
            raise

    # ───────────── CASO 7.1 – Monto con texto ─────────────
    def test_deposito_texto(self):
        nombre = "Prueba de depósito con texto inválido"
        try:
            stdout, _ = self.run_script("2\nabc\n300\n4\n")
            self.assertIn("Error", stdout)
            print(f"{nombre} - SUPERADA")
        except AssertionError:
            print(f"{nombre} - NO SUPERADA")
            raise

    # ───────────── CASO 7.2 – Retiro con texto ─────────────
    def test_retiro_texto(self):
        nombre = "Prueba de retiro con texto inválido"
        try:
            stdout, _ = self.run_script("3\n@@\n100\n4\n")
            self.assertIn("Error", stdout)
            print(f"{nombre} - SUPERADA")
        except AssertionError:
            print(f"{nombre} - NO SUPERADA")
            raise

    # ───────────── CASO 8.1 – Opción inválida ─────────────
    def test_opcion_invalida(self):
        nombre = "Prueba de opción de menú inválida"
        try:
            stdout, _ = self.run_script("9\n4\n")
            self.assertIn("Error", stdout)
            print(f"{nombre} - SUPERADA")
        except AssertionError:
            print(f"{nombre} - NO SUPERADA")
            raise

    # ───────────── CASO 8.2 – Opción vacía ─────────────
    def test_opcion_vacia(self):
        nombre = "Prueba de opción vacía en el menú"
        try:
            stdout, _ = self.run_script("\n4\n")
            self.assertIn("Error", stdout)
            print(f"{nombre} - SUPERADA")
        except AssertionError:
            print(f"{nombre} - NO SUPERADA")
            raise

    # ───────────── CASO 9.1 – Operaciones múltiples ─────────────
    def test_operaciones_multiples(self):
        nombre = "Prueba de operaciones múltiples (depósito + retiro)"
        try:
            # Depositar 500 → saldo 1500, luego retirar 300 → saldo 1200
            stdout, _ = self.run_script("2\n500\n3\n300\n1\n4\n")
            self.assertIn("1200.00", stdout)
            print(f"{nombre} - SUPERADA")
        except AssertionError:
            print(f"{nombre} - NO SUPERADA")
            raise

    # ───────────── CASO 10.1 – Salir ─────────────
    def test_salir(self):
        nombre = "Prueba de opción Salir"
        try:
            stdout, _ = self.run_script("4\n")
            self.assertIn("Hasta luego", stdout)
            print(f"{nombre} - SUPERADA")
        except AssertionError:
            print(f"{nombre} - NO SUPERADA")
            raise

if __name__ == "__main__":
    unittest.main(verbosity=2)
