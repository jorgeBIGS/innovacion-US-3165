#!/usr/bin/env python3
"""Genera las versiones Word descargables a partir de los Markdown del repositorio.

Las plantillas que cada docente tiene que rellenar a mano se publican también en .docx,
para que pueda escribir en ellas sin pasar por el repositorio.

    python3 bin/generar-docx.py

Requiere pandoc.
"""
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (origen, destino, título, ¿sólo los tramos marcados para el alumnado?)
DOCUMENTOS = [
    ("marco/PLANTILLA-ficha-calibracion.md", "descargas/ficha-calibracion.docx",
     "Ficha de calibración disciplinar", False),
    ("instrumentos/cuestionario-autopercepcion.md",
     "descargas/cuestionario-autopercepcion.docx",
     "Cuestionario de autopercepción y actitudes", True),
    ("instrumentos/consentimiento-informado.md",
     "descargas/consentimiento-informado.docx",
     "Información y consentimiento informado", True),
]

# Cabecera del cuestionario que recibe el alumnado, en lugar de la ficha metodológica.
ENCABEZADOS = {
    "instrumentos/cuestionario-autopercepcion.md": """Este cuestionario es **anónimo y voluntario**. No se califica y no responder no tiene
ninguna consecuencia académica. Sirve para saber cómo cambia la forma en que el alumnado
usa la inteligencia artificial a lo largo del curso.

Responde con sinceridad: no hay respuestas correctas ni incorrectas. Lo repetirás al final
del cuatrimestre, y el código que construyes en la primera pregunta es lo único que
permite emparejar ambas respuestas sin identificarte.
""",
}

PIE = """

---

Proyecto de innovación docente nº 3165 · Universidad de Sevilla · IV Plan Propio de
Docencia, Acción 221, Modalidad B. Plantilla publicada bajo CC BY-SA 4.0 en
https://jorgebigs.github.io/innovacion-US-3165/
"""


def sin_front_matter(texto):
    return re.sub(r"\A---\n.*?\n---\n", "", texto, flags=re.S)


def solo_alumnado(texto):
    """Devuelve sólo los tramos entre <!-- alumnado:inicio --> y <!-- alumnado:fin -->."""
    tramos = re.findall(r"<!--\s*alumnado:inicio\s*-->(.*?)<!--\s*alumnado:fin\s*-->",
                        texto, flags=re.S)
    if not tramos:
        raise SystemExit("No hay marcas de alumnado en el documento")
    return "\n".join(t.strip() for t in tramos)


def main():
    if not shutil.which("pandoc"):
        sys.exit("Falta pandoc: sudo apt install pandoc")

    for origen, destino, titulo, recortar in DOCUMENTOS:
        ruta_origen = os.path.join(RAIZ, origen)
        ruta_destino = os.path.join(RAIZ, destino)
        os.makedirs(os.path.dirname(ruta_destino), exist_ok=True)

        with io.open(ruta_origen, encoding="utf-8") as f:
            cuerpo = sin_front_matter(f.read())
        if recortar:
            cuerpo = ENCABEZADOS.get(origen, "") + "\n" + solo_alumnado(cuerpo)
        cuerpo += PIE

        with tempfile.NamedTemporaryFile("w", suffix=".md", encoding="utf-8",
                                         delete=False) as tmp:
            tmp.write(cuerpo)
            temporal = tmp.name

        try:
            subprocess.run(
                ["pandoc", temporal, "-f", "gfm", "-o", ruta_destino,
                 "--metadata", "title=" + titulo,
                 "--metadata", "lang=es-ES"],
                check=True)
        finally:
            os.unlink(temporal)

        print("%s -> %s (%d KB)"
              % (origen, destino, os.path.getsize(ruta_destino) // 1024))


if __name__ == "__main__":
    main()
