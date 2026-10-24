import json
import yaml
import xml.etree.ElementTree as ET
from dataclasses import dataclass, asdict


@dataclass
class Docente:
    numero_empleado: int
    nombre: str
    especialidad: str


class GestorDocentes:
    """Administra los docentes del Edificio 2 de la UT Coahuila."""

    def __init__(self):
        self._docentes = {}

    def _validar(self, docente):
        if not isinstance(docente.numero_empleado, int) or docente.numero_empleado <= 0:
            raise ValueError("El número de empleado debe ser un entero positivo")
        if not docente.nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if not docente.especialidad.strip():
            raise ValueError("La especialidad no puede estar vacía")

    def agregar(self, docente):
        self._validar(docente)
        if docente.numero_empleado in self._docentes:
            raise ValueError("Ya existe un docente con ese número de empleado")
        self._docentes[docente.numero_empleado] = docente

    def buscar(self, numero_empleado):
        return self._docentes.get(numero_empleado)

    def actualizar(self, numero_empleado, nombre=None, especialidad=None):
        docente = self.buscar(numero_empleado)
        if docente is None:
            raise KeyError("Docente no encontrado")
        if nombre is not None:
            docente.nombre = nombre
        if especialidad is not None:
            docente.especialidad = especialidad
        self._validar(docente)

    def eliminar(self, numero_empleado):
        if numero_empleado not in self._docentes:
            raise KeyError("Docente no encontrado")
        del self._docentes[numero_empleado]

    def listar(self):
        return sorted(self._docentes.values(), key=lambda d: d.nombre)

    # ---------- Formatos de presentación ----------
    def a_tabla(self):
        enc = "No. Empleado".ljust(14) + "Nombre".ljust(28) + "Especialidad".ljust(25)
        lineas = [enc, "-" * len(enc)]
        for d in self.listar():
            lineas.append(
                str(d.numero_empleado).ljust(14)
                + d.nombre.ljust(28)
                + d.especialidad.ljust(25)
            )
        return "\n".join(lineas)

    def exportar_json(self, ruta):
        datos = [asdict(d) for d in self.listar()]
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

    def exportar_yaml(self, ruta):
        datos = [asdict(d) for d in self.listar()]
        with open(ruta, "w", encoding="utf-8") as f:
            yaml.safe_dump(datos, f, allow_unicode=True, sort_keys=False)

    def exportar_xml(self, ruta):
        raiz = ET.Element("docentes")
        for d in self.listar():
            nodo = ET.SubElement(raiz, "docente")
            ET.SubElement(nodo, "numero_empleado").text = str(d.numero_empleado)
            ET.SubElement(nodo, "nombre").text = d.nombre
            ET.SubElement(nodo, "especialidad").text = d.especialidad
        arbol = ET.ElementTree(raiz)
        ET.indent(arbol, space="    ")
        arbol.write(ruta, encoding="utf-8", xml_declaration=True)