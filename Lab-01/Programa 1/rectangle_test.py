import unittest
import subprocess
import sys

class TestRectangle(unittest.TestCase):

    def run_script(self, input_data):
        process = subprocess.Popen(
            [sys.executable, "rectangle.py"],  # ejecuta tu programa
            stdin=subprocess.PIPE,            # simula entrada por teclado
            stdout=subprocess.PIPE,           # captura lo que imprime
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input_data)
        return stdout, stderr

    # ---------------- CASOS VALIDOS ----------------

    def test_enteros(self):
        nombre = "Prueba con valores enteros positivos"
        stdout, _ = self.run_script("5\n4\n")
        self.assertIn("Área: 20.0", stdout)
        print(f"{nombre} - SUPERADA")

    def test_decimales(self):
        nombre = "Prueba con valores decimales"
        stdout, _ = self.run_script("2.5\n3.2\n")
        self.assertIn("Área: 8.0", stdout)
        print(f"{nombre} - SUPERADA")

    def test_valores_grandes(self):
        nombre = "Prueba con valores grandes"
        stdout, _ = self.run_script("12345.67\n9876.54\n")
        self.assertIn("Área:", stdout)
        print(f"{nombre} - SUPERADA")

    def test_espacios(self):
        nombre = "Prueba con espacios"
        stdout, _ = self.run_script(" 6 \n 7 \n")
        self.assertIn("Área: 42.0", stdout)
        print(f"{nombre} - SUPERADA")

    def test_valores_pequenos(self):
        nombre = "Prueba con valores pequeños"
        stdout, _ = self.run_script("0.0001\n0.0002\n")
        self.assertIn("Área:", stdout)
        print(f"{nombre} - SUPERADA")

    # ---------------- CASOS INVALIDOS ----------------

    def test_base_invalida(self):
        nombre = "Base inválida (texto)"
        stdout, _ = self.run_script("abc\n5\n4\n")
        self.assertIn("Error", stdout)
        print(f"{nombre} - SUPERADA")

    def test_altura_invalida(self):
        nombre = "Altura inválida (símbolos)"
        stdout, _ = self.run_script("5\n@@\n4\n")
        self.assertIn("Error", stdout)
        print(f"{nombre} - SUPERADA")

    def test_base_negativa(self):
        nombre = "Base negativa"
        stdout, _ = self.run_script("-5\n4\n6\n")
        self.assertIn("Error", stdout)
        print(f"{nombre} - SUPERADA")

    def test_altura_cero(self):
        nombre = "Altura cero"
        stdout, _ = self.run_script("5\n0\n3\n")
        self.assertIn("Error", stdout)
        print(f"{nombre} - SUPERADA")

    def test_base_vacia(self):
        nombre = "Base vacía"
        stdout, _ = self.run_script("\n5\n4\n")
        self.assertIn("Error", stdout)
        print(f"{nombre} - SUPERADA")

    def test_formato_incorrecto(self):
        nombre = "Formato incorrecto"
        stdout, _ = self.run_script("2..5\n3\n4\n")
        self.assertIn("Error", stdout)
        print(f"{nombre} - SUPERADA")

    def test_altura_negativa(self):
        nombre = "Altura negativa"
        stdout, _ = self.run_script("5\n-3\n4\n")
        self.assertIn("Error", stdout)
        print(f"{nombre} - SUPERADA")


if __name__ == "__main__":
    unittest.main()