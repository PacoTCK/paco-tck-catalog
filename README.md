# paco-tck-catalog

Catálogo de plugins de Claude Code de PacoTCK. Cada plugin vive en su propio repo; este repo solo los lista, salvo `modo`, que vive aquí.

| Plugin | Qué hace | Repo |
|---|---|---|
| `jarvis` | Skills `claude-architect` y `eval-builder` con sus wikis | [PacoTCK/Jarvis](https://github.com/PacoTCK/Jarvis) (`brain/`) |
| `harness-sdd` | Arnés SDD: ciclo de 7 fases, subagentes, gates y guard | [PacoTCK/data-eng-harness-v2](https://github.com/PacoTCK/data-eng-harness-v2) |
| `superpowers` | Modo ligero: brainstorming, plan, subagente por tarea con revisión y TDD | [obra/superpowers](https://github.com/obra/superpowers) (de terceros, MIT) |
| `andrej-karpathy-skills` | Modo ultraligero: una skill con cuatro pautas de código | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) (de terceros, MIT) |
| `modo` | `/modo harness-sdd \| superpowers \| andrej-karpathy-skills \| ninguno`: elige el arnés de la carpeta actual | aquí (`plugins/modo/`) |

## Instalar

```
/plugin marketplace add PacoTCK/paco-tck-catalog
/plugin install jarvis@paco-tck-catalog
/plugin install modo@paco-tck-catalog
```

Para tenerlos en todas las carpetas, instálalos con scope *user*. Los arneses no se instalan a mano: los activa `/modo` en cada carpeta.

Instalar un plugin solo funciona si tienes acceso de lectura a su repo.
