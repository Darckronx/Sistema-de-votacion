# sistema-votacion/votacion.py

import json

HEAD
votos = {}       # {nombre_votante: candidato}
historial = []

HEAD

def registrar_voto(nombre, candidato):
    """Registra el voto de una persona. Evita votos duplicados."""
    if nombre in votos:
        print(f"❌ {nombre} ya votó por {votos[nombre]}")
        return False
    votos[nombre] = candidato
    print(f"✅ Voto registrado: {nombre} → {candidato}")
    return True

# sistema-votacion/votacion.py
import json
feature/reiniciar-votacion

votos = {}
historial = []


HEAD
def ver_resultados():
    """Muestra los resultados con conteo y porcentaje."""
    if not votos:
        print("⚠️  No hay votos registrados.")
        return

    total = len(votos)
    conteo = {}
    for candidato in votos.values():
        conteo[candidato] = conteo.get(candidato, 0) + 1

    print(f"\n📊 Resultados ({total} votos en total):")
    for candidato, cantidad in conteo.items():
        porcentaje = (cantidad / total) * 100
        print(f"  {candidato}: {cantidad} votos ({porcentaje:.2f}%)")
feature/ver-resultados
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
feature/reiniciar-votacion
