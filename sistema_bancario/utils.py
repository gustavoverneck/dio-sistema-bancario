def real_para_centavos(valor: float) -> int:
    return int(valor * 100)

def centavos_para_real(valor: int) -> float:
    return valor / 100