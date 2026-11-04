"""Activa un arnés en .claude/settings.json de la carpeta actual y desactiva los demás."""
import json
import sys
from pathlib import Path

CATALOGO = "paco-tck-catalog"
MODOS = {"pesado": "harness-pesado", "ligero": "harness-ligero"}  # modo -> plugin del catálogo

modo = sys.argv[1] if len(sys.argv) > 1 else ""
if modo not in (*MODOS, "ninguno"):
    sys.exit(f"Modo desconocido: {modo!r}. Opciones: {', '.join(MODOS)}, ninguno")

ruta = Path.cwd() / ".claude" / "settings.json"
datos = json.loads(ruta.read_text(encoding="utf-8")) if ruta.exists() else {}
activos = datos.setdefault("enabledPlugins", {})
for nombre, plugin in MODOS.items():
    activos[f"{plugin}@{CATALOGO}"] = nombre == modo

ruta.parent.mkdir(exist_ok=True)
ruta.write_text(json.dumps(datos, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"{ruta}: modo {modo}")
