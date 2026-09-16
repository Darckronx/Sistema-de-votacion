# sistema-votacion/votacion.py

votos = {}
historial = []


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