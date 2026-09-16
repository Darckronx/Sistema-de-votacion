# sistema-votacion/votacion.py

votos = {}          # {nombre: candidato}
historial = []

# sistema-votacion/votacion.py
import json

votos = {}
historial = []


def reiniciar_votacion():
    """Guarda el historial en archivo y limpia la votación actual."""
    global votos

    if votos:
        with open("historial.json", "a", encoding="utf-8") as f:
            f.write(json.dumps(votos, ensure_ascii=False) + "\n")
        print("💾 Historial guardado en historial.json")
    else:
        print("⚠️  No había votos que guardar.")

    votos = {}
    print("🔄 Votación reiniciada correctamente.")