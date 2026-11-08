# paco-tck-catalog

Catálogo de plugins de Claude Code de PacoTCK. Cada plugin vive en su propio repo; este repo solo los lista, salvo `modo`, que vive aquí.

| Plugin | Qué hace | Repo |
|---|---|---|
| `jarvis` | Skills `claude-architect` y `eval-builder` con sus wikis | [PacoTCK/Jarvis](https://github.com/PacoTCK/Jarvis) (`brain/`) |
| `harness-sdd` | Arnés SDD: ciclo de 7 fases, subagentes, gates y guard | [PacoTCK/data-eng-harness-v2](https://github.com/PacoTCK/data-eng-harness-v2) |
| `sdd-companion` | Mod del arnés: fase SDD encima del prompt, gasto en la línea de estado, panel `/sdd-panel`. Se instala solo con `harness-sdd` (dependencia) | [PacoTCK/data-eng-harness-v2](https://github.com/PacoTCK/data-eng-harness-v2/tree/master/adapters/claude-code/mods/sdd-companion) |
| `modo` | `/modo harness-sdd \| harness-ligero \| ninguno`: elige el arnés de la carpeta actual | aquí (`plugins/modo/`) |

## Instalar

```
/plugin marketplace add PacoTCK/paco-tck-catalog
/plugin install jarvis@paco-tck-catalog
/plugin install modo@paco-tck-catalog
```

Para tenerlos en todas las carpetas, instálalos con scope *user*. Los arneses no se instalan a mano: los activa `/modo` en cada carpeta.

Instalar un plugin solo funciona si tienes acceso de lectura a su repo.
