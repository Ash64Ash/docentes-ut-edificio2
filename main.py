from docentes import Docente, GestorDocentes

gestor = GestorDocentes()
gestor.agregar(Docente(1001, "Ana López Ramírez", "Sistemas Computacionales"))
gestor.agregar(Docente(1002, "Carlos Medina Soto", "Mecatrónica"))
gestor.agregar(Docente(1003, "Laura Treviño Garza", "Procesos Industriales"))

print(gestor.a_tabla())

gestor.exportar_json("docentes.json")
gestor.exportar_yaml("docentes.yaml")
gestor.exportar_xml("docentes.xml")
print("\nArchivos docentes.json, docentes.yaml y docentes.xml generados.")
