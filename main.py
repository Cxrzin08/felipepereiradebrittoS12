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
    ''')

while True:
    reiniciar()
    selecao = input("Digite uma opção: ")
    if selecao not in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
        print("Opção inválida, por favor selecione uma das opções.")
        continue

    if selecao == "0":
        print("Programa encerrado")
        exit()
    elif selecao in ["1", "2", "3", "4", "5", "6"]:
        valor = float(input("Digite o valor da temperatura: "))
        if selecao == "1":
            resultado = Temperatura.c_para_f(valor)
            print(f"A temperatura convertida é: {resultado} Fahrenheit")
        elif selecao == "2":
            resultado = Temperatura.f_para_c(valor)
            print(f"A temperatura convertida é: {resultado} Celsius")
        elif selecao == "3":
            resultado = Temperatura.k_para_c(valor)
            print(f"A temperatura convertida é: {resultado} Celsius")
        elif selecao == "4":
            resultado = Temperatura.c_para_k(valor)
            print(f"A temperatura convertida é: {resultado} Kelvin")
        elif selecao == "5":
            resultado = Temperatura.k_para_f(valor)
            print(f"A temperatura convertida é: {resultado} Fahrenheit")
        elif selecao == "6":
            resultado = Temperatura.f_para_k(valor)
            print(f"A temperatura convertida é: {resultado} Kelvin")
    elif selecao in ["7", "8"]:
        valor = float(input("Digite o valor para a conversão: "))
        if selecao == "7":
            resultado = ConversorMedidas.cm_para_m(valor)
            print(f"Os centímetros convertidos para metros é: {resultado} metros")
        elif selecao == "8":
            resultado = ConversorMedidas.m_para_cm(valor)
            print(f"Os metros convertidos para centímetros é: {resultado} centímetros")

    while True:
        teste = input("Deseja voltar para a tela inicial? Se sim, digite (Sim): ").capitalize()
        if teste == "Sim":
            break
        else:
            print("Por favor digite uma opção correspondente.")
