from conversor_temperatura import Temperatura
from conversor_medidas import Medidas

print('''
    [0]. Sair
    [1]. Temperatura - C para F
      ''')
selecao = input("Digite uma opção: ")


if selecao == "0":
    print("Programa encerrado")
    exit()
if selecao == "1":
    valor_c = float(input("Qual a temperatura em celcius que deseja converter?"))
    resultado = Temperatura.c_para_f(valor_c)
    print(f"A temperatura convertida é : {resultado}")