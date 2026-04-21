import unittest
import subprocess
import os
import sys

class TestNumbers(unittest.TestCase):
    script_path = os.path.join(os.path.dirname(__file__), 'numbers.py')

    def run_script(self, input_string):
        process = subprocess.Popen(
            [sys.executable, self.script_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=input_string)
        return stdout, stderr

    def test_flujo_basico(self):
        nombre = "Prueba de flujo básico"
        try:
            stdout, _ = self.run_script("2\n10\n15\n")
            self.assertIn("10: par", stdout)
            self.assertIn("15: impar", stdout)
            print(f"{nombre} - SUPERADA")
        except AssertionError:
            print(f"{nombre} - NO SUPERADA")
            raise

    def test_negativos_cero(self):
        nombre = "Prueba de números negativos y cero"
        try:
            stdout, _ = self.run_script("3\n-4\n-7\n0\n")
            self.assertIn("-4: par", stdout)
            self.assertIn("-7: impar", stdout)
            self.assertIn("0: par", stdout)
            print(f"{nombre} - SUPERADA")
        except AssertionError:
            print(f"{nombre} - NO SUPERADA")
            raise

    def test_errores_en_lista(self):
        nombre = "Prueba de reintento ante entrada inválida en lista"
        try:
            stdout, _ = self.run_script("1\nerror\n8\n")
            self.assertIn("Entrada no válida", stdout)
            self.assertIn("8: par", stdout)
            print(f"{nombre} - SUPERADA")
        except AssertionError:
            print(f"{nombre} - NO SUPERADA")
            raise

    def test_cantidad_letras(self):
        nombre = "Prueba de cantidad de números no válida (letras)"
        try:
            stdout, _ = self.run_script("abc\n")
            self.assertIn("Error", stdout)
            print(f"{nombre} - SUPERADA")
        except AssertionError:
            print(f"{nombre} - NO SUPERADA")
            raise

    def test_limites_cantidad(self):
        nombre = "Prueba de límites de cantidad (0 y negativos)"
        try:
            stdout, _ = self.run_script("0\n")
            self.assertIn("Listado de números y su clasificación", stdout)
            stdout_neg, _ = self.run_script("-5\n")
            self.assertIn("Listado de números y su clasificación", stdout_neg)
            print(f"{nombre} - SUPERADA")
        except AssertionError:
            print(f"{nombre} - NO SUPERADA")
            raise

    def test_decimales(self):
        nombre = "Prueba de rechazo de números decimales"
        try:
            stdout, _ = self.run_script("2.5\n")
            self.assertIn("Error", stdout)
            stdout_num, _ = self.run_script("1\n4.5\n5\n")
            self.assertIn("Entrada no válida", stdout_num)
            self.assertIn("5: impar", stdout_num)
            print(f"{nombre} - SUPERADA")
        except AssertionError:
            print(f"{nombre} - NO SUPERADA")
            raise

    def test_gigantes(self):
        nombre = "Prueba de números extremadamente grandes"
        try:
            gigante_par = "2" * 500
            gigante_impar = ("9" * 500) + "1"
            stdout, _ = self.run_script(f"2\n{gigante_par}\n{gigante_impar}\n")
            self.assertIn(f"{gigante_par}: par", stdout)
            self.assertIn(f"{gigante_impar}: impar", stdout)
            print(f"{nombre} - SUPERADA")
        except AssertionError:
            print(f"{nombre} - NO SUPERADA")
            raise

    def test_vacios_espacios(self):
        nombre = "Prueba de entradas vacías y con espacios"
        try:
            stdout, _ = self.run_script(" \n")
            self.assertIn("Error", stdout)
            stdout_num, _ = self.run_script("1\n  \n9\n")
            self.assertIn("Entrada no válida", stdout_num)
            self.assertIn("9: impar", stdout_num)
            print(f"{nombre} - SUPERADA")
        except AssertionError:
            print(f"{nombre} - NO SUPERADA")
            raise

    def test_caracteres_especiales(self):
        nombre = "Prueba de caracteres especiales"
        try:
            stdout, _ = self.run_script("1\n@#$%\n7\n")
            self.assertIn("Entrada no válida", stdout)
            self.assertIn("7: impar", stdout)
            print(f"{nombre} - SUPERADA")
        except AssertionError:
            print(f"{nombre} - NO SUPERADA")
            raise

    def test_cantidad_espacios(self):
        nombre = "Prueba de cantidad y números con espacios laterales"
        try:
            stdout, _ = self.run_script("  2  \n 4 \n 3 \n")
            self.assertIn("4: par", stdout)
            self.assertIn("3: impar", stdout)
            print(f"{nombre} - SUPERADA")
        except AssertionError:
            print(f"{nombre} - NO SUPERADA")
            raise

if __name__ == "__main__":
    unittest.main()
