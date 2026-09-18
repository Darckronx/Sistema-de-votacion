# 🗳️ Sistema de Votación

Proyecto colaborativo para practicar ramas, tags, merges y conventional commits en Git.

## 📋 Descripción

Sistema simple de votación en Python que permite registrar votos, ver resultados con porcentajes y reiniciar la votación guardando un historial.

## ⚙️ Funciones

| Función | Descripción | Responsable |
|---|---|---|
| `registrar_voto(nombre, candidato)` | Registra el voto de una persona y evita votos duplicados usando un diccionario. | Alfonso (rama `feature/registrar-voto`) |
| `ver_resultados()` | Muestra el conteo y el porcentaje de votos por candidato. | Alfonso (rama `feature/ver-resultados`) |
| `reiniciar_votacion()` | Guarda el historial en `historial.json` y limpia la votación actual. | Alfonso (rama `feature/reiniciar-votacion`) |
| `mostrar_ganador()` | Muestra el candidato ganador o si hubo empate. | Equipo (mejora final en `main`) |

## 🚀 Uso

```python
from votacion import registrar_voto, ver_resultados, reiniciar_votacion, mostrar_ganador

registrar_voto("Ana", "Candidato A")
registrar_voto("Luis", "Candidato B")
registrar_voto("Maria", "Candidato A")

ver_resultados()
mostrar_ganador()
reiniciar_votacion()
```

## 🌿 Flujo de ramas

- `feature/registrar-voto` → tag `v0.1-registro`
- `feature/ver-resultados` → tag `v0.1-resultados`
- `feature/reiniciar-votacion` → tag `v0.1-reinicio`
- `main` → tag final `v1.0`

## 🧾 Conventional Commits usados

- `feat:` nuevas funcionalidades
- `fix:` corrección de errores
- `refactor:` mejoras internas sin cambiar comportamiento
- `docs:` documentación
- `chore:` tareas de mantenimiento
- `test:` pruebas

## 👥 Equipo

- Alfonso — 3 roles (registro, resultados, reinicio y merge final)

## 📌 Versión

**v1.0** — Sistema completo con las 3 funciones + mejora del ganador.