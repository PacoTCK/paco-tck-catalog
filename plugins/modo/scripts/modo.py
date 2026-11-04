"""Activa un arnés en .claude/settings.json de la carpeta actual y desactiva los demás."""
import json
import sys
from pathlib import Path

CATALOGO = "paco-tck-catalog"
ARNESES = ("harness-sdd", "harness-ligero")  # el modo es el nombre del plugin del catálogo

modo = sys.argv[1] if len(sys.argv) > 1 else ""
if modo not in (*ARNESES, "ninguno"):
    sys.exit(f"Modo desconocido: {modo!r}. Opciones: {', '.join(ARNESES)}, ninguno")

ruta = Path.cwd() / ".claude" / "settings.json"
datos = json.loads(ruta.read_text(encoding="utf-8")) if ruta.exists() else {}
activos = datos.setdefault("enabledPlugins", {})
for arnes in ARNESES:
    activos[f"{arnes}@{CATALOGO}"] = arnes == modo

ruta.parent.mkdir(exist_ok=True)
ruta.write_text(json.dumps(datos, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"{ruta}: modo {modo}")
