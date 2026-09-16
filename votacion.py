# sistema-votacion/votacion.py

votos = {}       # {nombre_votante: candidato}
historial = []


def registrar_voto(nombre, candidato):
    """Registra el voto de una persona. Evita votos duplicados."""
    if nombre in votos:
        print(f"❌ {nombre} ya votó por {votos[nombre]}")
        return False
    votos[nombre] = candidato
    print(f"✅ Voto registrado: {nombre} → {candidato}")
    return True
