#!/usr/bin/env python3
"""Genera las páginas de curso de cada asignatura a partir de _data/asignaturas.yml.

Las páginas son sólo cabeceras: todo el contenido vive en _includes/lecciones/ y en los
datos de la asignatura. Ejecuta este script después de añadir o cambiar una asignatura:

    python3 bin/generar-cursos.py
"""
import io
import os
import sys

try:
    import yaml
except ImportError:
    sys.exit("Falta PyYAML:  pip install pyyaml")

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS = os.path.join(RAIZ, "_data", "asignaturas.yml")
DESTINO = os.path.join(RAIZ, "cursos")

INDICE = """---
layout: curso
asignatura: {slug}
title: "{nombre}"
descripcion: "Curso de alfabetización en IA generativa de {nombre}."
permalink: /cursos/{slug}/
---
"""

LECCION = """---
layout: leccion
asignatura: {slug}
leccion: {n}
title: "Lección {n} · {nombre}"
---
"""


def main():
    with io.open(DATOS, encoding="utf-8") as f:
        asignaturas = yaml.safe_load(f)

    escritos = 0
    for a in asignaturas:
        carpeta = os.path.join(DESTINO, a["slug"])
        os.makedirs(carpeta, exist_ok=True)

        with io.open(os.path.join(carpeta, "index.md"), "w", encoding="utf-8") as f:
            f.write(INDICE.format(**a))
        escritos += 1

        if a.get("estado") != "completo":
            # Sin datos no hay lecciones que generar; la portada del curso avisa.
            for n in range(1, 5):
                suelta = os.path.join(carpeta, "leccion-%d.md" % n)
                if os.path.exists(suelta):
                    os.remove(suelta)
            continue

        for n in range(1, 5):
            ruta = os.path.join(carpeta, "leccion-%d.md" % n)
            with io.open(ruta, "w", encoding="utf-8") as f:
                f.write(LECCION.format(slug=a["slug"], n=n, nombre=a["nombre"]))
            escritos += 1

    print("%d páginas generadas en cursos/ para %d asignaturas"
          % (escritos, len(asignaturas)))


if __name__ == "__main__":
    main()
