from conversor_temperatura import Temperatura
from conversor_medidas import ConversorMedidas

print('''
    [0]. Sair
    [1]. Temperatura - Celsius para Fahrenheit
    [2]. Temperatura - Fahrenheit para Celsius
    [3]. Converter medidas - Centímetros para Metros
    [4]. Converter medidas - Metros para Centímetros
      ''')
selecao = input("Digite uma opção: ")


if selecao == "0":
    print("Programa encerrado")
    exit()
elif selecao == "1":
    valor_c = float(input("Qual a temperatura em celcius que deseja converter?"))
    resultado = Temperatura.c_para_f(valor_c)
    print(f"A temperatura convertida é : {resultado}")
elif selecao == "2"
    valor_f = float(input("Qual a temperatura em fahrenheit que deseja converter?"))
    resultado = Temperatura.f_para_c(valor_f)
    print(f"A temperatura convertida é : {resultado}")
elif selecao == "3":
    valor_cm = float(input("Digite os metros que  deseja converter":))
resultado =      ConversorMedidas.cm_para_m(valor_cm)

elif selecao == "4":
    valor_m = float(input("Digite os centímetros que deseja converter:"))