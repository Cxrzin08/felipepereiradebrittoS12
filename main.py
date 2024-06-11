from conversor_temperatura import Temperatura
from conversor_medidas import ConversorMedidas

def reiniciar():
    print("Olá sou o programa do Felipe, digite qual opção você deseja")
    print('''
    [0]. Sair
    [1]. Temperatura - Celsius para Fahrenheit
    [2]. Temperatura - Fahrenheit para Celsius
    [3]. Temperatura - Kelvin para Celsius
    [4]. Temperatura - Celsius para Kelvin
    [5]. Temperatura - Kelvin para Fahrenheit
    [6]. Temperatura - Fahrenheit para Kelvin
    [7]. Converter medidas - Centímetros para Metros      
    [8]. Converter medidas - Metros para Centímetros
    [9]. Converter medidas - Metros para Kilômetros
    [10]. Converter medidas - Kilômetros para Metros
    ''')

def entradatemp():
    while True:
        valor = input("Digite o valor da temperatura: ")
        try:
            valor = float(valor)
            return valor
        except ValueError:
            print("Por favor, digite um número válido.")

def entradamed():
    while True:
        valor = input("Digite o valor para a conversão: ")
        try:
            valor = float(valor)
            return valor
        except ValueError:
            print("Por favor, digite um número válido.")

while True:
    while True:
        reiniciar()
        selecao = input("Digite uma opção: ")
        if selecao in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            break
        else:
            print("Opção inválida, por favor digite uma opção válida")

    match selecao:
        case "0":
            print("Programa encerrado.")
            break
        case "1":
            valor = entradatemp()
            resultado = Temperatura.c_para_f(valor)
            print(f"A temperatura convertida é: {resultado} Fahrenheit")
        case "2":
            valor = entradatemp()
            resultado = Temperatura.f_para_c(valor)
            print(f"A temperatura convertida é: {resultado} Celsius")
        case "3":
            valor = entradatemp()
            resultado = Temperatura.k_para_c(valor)
            print(f"A temperatura convertida é: {resultado} Celsius")
        case "4":
            valor = entradatemp()
            resultado = Temperatura.c_para_k(valor)
            print(f"A temperatura convertida é: {resultado} Kelvin")
        case "5":
            valor = entradatemp()
            resultado = Temperatura.k_para_f(valor)
            print(f"A temperatura convertida é: {resultado} Fahrenheit")
        case "6":
            valor = entradatemp()
            resultado = Temperatura.f_para_k(valor)
            print(f"A temperatura convertida é: {resultado} Kelvin")
        case "7":
            valor = entradamed()
            resultado = ConversorMedidas.cm_para_m(valor)
            print(f"Os centímetros convertidos para metros é: {resultado} Metros")
        case "8":
            valor = entradamed()
            resultado = ConversorMedidas.m_para_cm(valor)
            print(f"Os metros convertidos para centímetros é: {resultado} Centímetros")
        case "9":
            valor = entradamed()
            resultado = ConversorMedidas.m_para_km(valor)
            print(f"Os metros convertidos para kilômetros é: {resultado} Kilômetros")
        case "10":
            valor = entradamed()
            resultado = ConversorMedidas.km_para_m(valor)
            print(f"Os kilômetros convertidos para metros é: {resultado} metros")

    while True:
        teste = input("\n\nDeseja voltar para a tela inicial? Se sim, digite (Sim) \nDeseja encerrar o programa? Se sim digite (Encerrar)\n").capitalize()
        if teste == "Sim":
            break
        elif teste == "Encerrar":
            print("Programa encerrado.")
            exit()
        else:
            print("Por favor digite uma opção correspondente.")
