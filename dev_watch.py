#!/usr/bin/env python3
"""
Reconstrucción automática para desarrollo local.
Observa content/ y pages/ y ejecuta build.py al detectar un cambio,
imitando lo que Netlify hará solo en producción tras cada "Guardar".

Uso:  python3 dev_watch.py     (dejar corriendo en una terminal)
"""
import time, subprocess, pathlib

ROOT = pathlib.Path(__file__).parent
WATCH = [ROOT / "content", ROOT / "pages", ROOT / "build.py"]


def snapshot():
    s = {}
    for w in WATCH:
        if w.is_file():
            s[w] = w.stat().st_mtime
        elif w.is_dir():
            for f in w.rglob("*"):
                if f.is_file():
                    s[f] = f.stat().st_mtime
    return s


def build():
    subprocess.run(["python3", str(ROOT / "build.py")])


print("👀  Observando content/ y pages/ … (Ctrl+C para salir)")
build()
last = snapshot()
while True:
    time.sleep(1)
    cur = snapshot()
    if cur != last:
        print("↻  Cambio detectado — reconstruyendo el sitio…")
        build()
        last = cur
