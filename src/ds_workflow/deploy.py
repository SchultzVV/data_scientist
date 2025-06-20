
def simulate_canary(old_metric: float, new_metric: float, threshold: float = 0.02):
    """Avalia métrica do deploy canário e retorna métrica atualizada e status."""
    if new_metric + threshold < old_metric:
        print("Canário falhou, iniciando rollback...")
        return old_metric, False
    print("Novo modelo aprovado!")
    return new_metric, True
