---
name: modo
description: Elige el arnés de desarrollo de la carpeta actual (pesado, ligero o ninguno) escribiendo enabledPlugins en su .claude/settings.json. Úsala cuando el usuario diga "/modo pesado", "en esta carpeta quiero el arnés ligero", "usa el arnés pesado aquí", "quita el arnés" o similar.
argument-hint: "pesado | ligero | ninguno"
---

1. Decide el modo a partir de lo que pide el usuario: `pesado`, `ligero` o `ninguno`. Si no está claro, pregunta cuál y espera.
2. Ejecuta, desde la raíz de la carpeta de trabajo:
   `python "${CLAUDE_PLUGIN_ROOT}/scripts/modo.py" <modo>`
3. Responde en una línea qué modo queda activo y que el cambio se aplica al ejecutar `/reload-plugins` o al abrir una sesión nueva.

Solo puede haber un arnés activo por carpeta; el script desactiva el otro.
