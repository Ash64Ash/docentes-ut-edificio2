import json
import os
import unittest
import xml.etree.ElementTree as ET

import yaml

from docentes import Docente, GestorDocentes


class TestGestorDocentes(unittest.TestCase):

    def setUp(self):
        self.g = GestorDocentes()
        self.g.agregar(Docente(1001, "Ana López", "Sistemas"))

    def test_agregar_docente(self):
        self.g.agregar(Docente(1002, "Carlos Medina", "Mecatrónica"))
        self.assertEqual(len(self.g.listar()), 2)

    def test_numero_duplicado(self):
        with self.assertRaises(ValueError):
            self.g.agregar(Docente(1001, "Otro", "Otra"))

    def test_numero_invalido(self):
        with self.assertRaises(ValueError):
            self.g.agregar(Docente(-5, "Pedro", "Sistemas"))

    def test_nombre_vacio(self):
        with self.assertRaises(ValueError):
            self.g.agregar(Docente(1005, "  ", "Sistemas"))

    def test_buscar_existente(self):
        self.assertEqual(self.g.buscar(1001).nombre, "Ana López")

    def test_buscar_inexistente(self):
        self.assertIsNone(self.g.buscar(9999))

    def test_actualizar(self):
        self.g.actualizar(1001, especialidad="Redes")
        self.assertEqual(self.g.buscar(1001).especialidad, "Redes")

    def test_eliminar(self):
        self.g.eliminar(1001)
        self.assertIsNone(self.g.buscar(1001))

    def test_eliminar_inexistente(self):
        with self.assertRaises(KeyError):
            self.g.eliminar(9999)

    def test_exportar_json(self):
        self.g.exportar_json("prueba.json")
        with open("prueba.json", encoding="utf-8") as f:
            datos = json.load(f)
        os.remove("prueba.json")
        self.assertEqual(datos[0]["numero_empleado"], 1001)

    def test_exportar_yaml(self):
        self.g.exportar_yaml("prueba.yaml")
        with open("prueba.yaml", encoding="utf-8") as f:
            datos = yaml.safe_load(f)
        os.remove("prueba.yaml")
        self.assertEqual(datos[0]["nombre"], "Ana López")

    def test_exportar_xml(self):
        self.g.exportar_xml("prueba.xml")
        raiz = ET.parse("prueba.xml").getroot()
        os.remove("prueba.xml")
        self.assertEqual(raiz.find("docente/especialidad").text, "Sistemas")


if __name__ == "__main__":
    unittest.main()
    
  
