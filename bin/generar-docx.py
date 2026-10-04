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

DOCUMENTOS = [
    ("marco/PLANTILLA-ficha-calibracion.md", "descargas/ficha-calibracion.docx",
     "Ficha de calibración disciplinar"),
]

PIE = """

---

Proyecto de innovación docente nº 3165 · Universidad de Sevilla · IV Plan Propio de
Docencia, Acción 221, Modalidad B. Plantilla publicada bajo CC BY-SA 4.0 en
https://jorgebigs.github.io/innovacion-US-3165/
"""


def sin_front_matter(texto):
    return re.sub(r"\A---\n.*?\n---\n", "", texto, flags=re.S)


def main():
    if not shutil.which("pandoc"):
        sys.exit("Falta pandoc: sudo apt install pandoc")

    for origen, destino, titulo in DOCUMENTOS:
        ruta_origen = os.path.join(RAIZ, origen)
        ruta_destino = os.path.join(RAIZ, destino)
        os.makedirs(os.path.dirname(ruta_destino), exist_ok=True)

        with io.open(ruta_origen, encoding="utf-8") as f:
            cuerpo = sin_front_matter(f.read()) + PIE

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
