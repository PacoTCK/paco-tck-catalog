"""Activa un arnés en la carpeta actual y desactiva los demás.

Escribir enabledPlugins no basta: un plugin que no está descargado no carga. Por eso el arnés
elegido se instala con la CLI (scope project, que también lo activa en .claude/settings.json).
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

CATALOGO = "paco-tck-catalog"
ARNESES = ("harness-sdd", "superpowers", "andrej-karpathy-skills")  # pesado, ligero, ultraligero  # el modo es el nombre del plugin del catálogo

modo = sys.argv[1] if len(sys.argv) > 1 else ""
if modo not in (*ARNESES, "ninguno"):
    sys.exit(f"Modo desconocido: {modo!r}. Opciones: {', '.join(ARNESES)}, ninguno")

if modo != "ninguno":
    r = subprocess.run([shutil.which("claude") or "claude", "plugin", "install", f"{modo}@{CATALOGO}",
                        "--scope", "project"], capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"No se pudo instalar {modo}: {(r.stdout + r.stderr).strip()}")

ruta = Path.cwd() / ".claude" / "settings.json"
datos = json.loads(ruta.read_text(encoding="utf-8")) if ruta.exists() else {}
activos = datos.setdefault("enabledPlugins", {})
for arnes in ARNESES:
    activos[f"{arnes}@{CATALOGO}"] = arnes == modo

ruta.parent.mkdir(exist_ok=True)
ruta.write_text(json.dumps(datos, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"{ruta}: modo {modo}")
