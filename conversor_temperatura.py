class Temperatura:
    def _init_(self) -> None:
        pass

while True:
    converter = input("Qual opção você deseja?\n1. Converter de Fahrenheit para Celsius.\n2. Converter de Celsius para Fahrenheit.\n")
    if converter in ["1", "2"]:
        break
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

input("Pressione Enter para continuar...")

if converter == "1":
    fahrenheit = float(input("Digite a temperatura em Fahrenheit:\n"))
    celsius = (fahrenheit - 32) * 5/9
    print(f"A temperatura convertida é {celsius:.2f} graus Celsius.")
elif converter == "2":
    celsius = float(input("Digite a temperatura em Celsius:\n"))
    fahrenheit = (celsius * 9/5) + 32
    print(f"A temperatura convertida é {fahrenheit:.2f} graus Fahrenheit.")

while True:
    teste2 = input("Deseja voltar para a tela inicial?\n1. Voltar para a tela inicial\n2. Encerrar o programa\n")
    if teste2 in ["1", "2"]:
        break
    else:
        print("Selecione uma opção válida")

if teste2 == "2":
    print("Programa encerrado.")
elif teste2 == "1":
  import limpartexto
  import main 