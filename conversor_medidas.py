class ConversorMedidas:
    def __init__(self) -> None:
        pass


    def cm_para_m(valor_cm):
        resultado = valor_cm / 100
        return resultado

    def m_para_cm(valor_m):
        resultado = valor_m * 100
        return resultado
    
    def m_para_km(valor_m):
        resultado = valor_m / 1000
        return resultado

    def km_para_m(valor_km):
        resultado = valor_km * 1000
        return resultado

    def cm_para_km(valor_cm):
        resultado = valor_cm / 100000
        return resultado

    def km_para_cm(valor_km):
        resultado = valor_km * 100000
        return resultado
