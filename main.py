from conversor_temperatura import Temperatura
from conversor_medidas import ConversorMedidas

print('''
    [0]. Sair
    [1]. Temperatura - Celsius para Fahrenheit
    [2]. Temperatura - Fahrenheit para Celsius
    [3]. Converter medidas - Centímetros para Metros      
    [4]. Converter medidas - Metros para Centímetros
      ''')


while True:
    selecao = input("Digite uma opção: ")
    if selecao in ["0", "1", "2", "3", "4"]:
        break
    else:
        print("Opção inválida, por favor selecione uma das opções.")
        
match selecao:

case "0":
    print("Programa encerrado")
    exit()
case "1":
    valor_c = float(input("Qual a temperatura em celcius que deseja converter?"))
    resultado = Temperatura.c_para_f(valor_c)
    print(f"A temperatura convertida é : {resultado}")
case "2":
    valor_f = float(input("Qual a temperatura em fahrenheit que deseja converter?"))
    resultado = Temperatura.f_para_c(valor_f)
    print(f"A temperatura convertida é : {resultado}")
case "3":
    valor_cm = float(input("Digite os metros que você deseja converter?"))
    resultado = ConversorMedidas.cm_para_m(valor_cm)
    print(f"Os metros convertidos para centímetros é: {resultado}")
case "4":
    valor_m = float(input("Digite os centímetros que deseja converter:"))
    resultado = ConversorMedidas.m_para_cm(valor_m)
    print(f"Os centímetros convertidos para metros é :{resultado}")

teste = input("Deseja voltar para a tela inical se caso deseja digite (Sim):\n").capitalize
