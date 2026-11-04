---
name: modo
description: Elige el arnés de desarrollo de la carpeta actual (harness-sdd, harness-ligero o ninguno) instalándolo a scope project (queda en enabledPlugins de su .claude/settings.json). Úsala cuando el usuario diga "/modo harness-sdd", "en esta carpeta quiero el arnés SDD", "usa el arnés ligero aquí", "quita el arnés" o similar.
argument-hint: "harness-sdd | harness-ligero | ninguno"
---

1. Decide el modo a partir de lo que pide el usuario: `harness-sdd`, `harness-ligero` o `ninguno`. Si no está claro, pregunta cuál y espera.
2. Ejecuta, desde la raíz de la carpeta de trabajo:
   `python "${CLAUDE_PLUGIN_ROOT}/scripts/modo.py" <modo>`
3. Responde en una línea qué modo queda activo y que el cambio se aplica al ejecutar `/reload-plugins` o al abrir una sesión nueva.

Solo puede haber un arnés activo por carpeta; el script desactiva el otro.
