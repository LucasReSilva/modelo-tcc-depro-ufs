"""Cálculo de indicadores operacionais de produção (exemplo para o Anexo)."""


def calcular_eficiencia(producao_real: float, capacidade_nominal: float) -> float:
    """Retorna a eficiência operacional (%) de uma linha produtiva."""
    if capacidade_nominal <= 0:
        raise ValueError("A capacidade nominal deve ser maior que zero.")
    return (producao_real / capacidade_nominal) * 100.0


def calcular_tempo_ciclo(tempo_disponivel_min: float, producao_real: float) -> float:
    """Retorna o tempo de ciclo médio (min/unidade)."""
    if producao_real <= 0:
        raise ValueError("A produção real deve ser maior que zero.")
    return tempo_disponivel_min / producao_real


if __name__ == "__main__":
    linhas = [
        ("Linha A", 480, 510, 5952.0),
        ("Linha B", 390, 436, 5889.0),
        ("Linha C", 520, 537, 5616.0),
    ]

    for nome, producao, capacidade, tempo_min in linhas:
        eficiencia = calcular_eficiencia(producao, capacidade)
        ciclo = calcular_tempo_ciclo(tempo_min, producao)
        print(f"{nome}: ciclo = {ciclo:.1f} min | eficiência = {eficiencia:.1f}%")
