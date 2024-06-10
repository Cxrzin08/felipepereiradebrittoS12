class Temperatura:
    def __init__(self):
        pass

    def c_para_f(valor_c):
        resultado = valor_c * 1.8 + 32
        return resultado

    def f_para_c(valor_f):
        resultado = (valor_f - 32) / 1.8
        return resultado

    def k_para_c(valor_k):
        resultado = valor_k - 273.15
        return resultado
    
    def c_para_k(valor_c):
        resultado = valor_c + 273.15
        return resultado
    
    def k_para_f(valor_k):
        resultado = valor_k * 9 / 5 - 459.67
        return resultado
    
    def f_para_k(valor_f):
        resultado = (valor_f + 459.67) * 5 / 9
        return resultado
