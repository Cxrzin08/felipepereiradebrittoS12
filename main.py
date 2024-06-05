from conversor_temperatura import Temperatura
from conversor_medidas import ConversorMedidas

print('''
    [0]. Sair
    [1]. Temperatura - Celsius para Fahrenheit
    [2]. Temperatura - Fahrenheit para Celsius
      ''')
selecao = input("Digite uma opção: ")


if selecao == "0":
    print("Programa encerrado")
    exit()
if selecao == "1":
    valor_c = float(input("Qual a temperatura em celcius que deseja converter?"))
    resultado = Temperatura.c_para_f(valor_c)
    print(f"A temperatura convertida é : {resultado}")
if selecao == "2"
    valor_f = float(input("Qual a temperatura em fahrenheit que deseja converter?"))
    resultado = Temperatura.f_para_c(valor_f)
    print(f"A temperatura convertida é : {resultado}")