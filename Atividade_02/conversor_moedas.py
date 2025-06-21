import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Atividade_01.funcoes import solicitar_numero_float, solicitar_numero_inteiro

cambio_dolar = 5.20
cambio_euro = 6.15
print("Bem-vindo ao conversor de moedas!")
print(f"""
Taxas de câmbio atuais:
1 Dólar = R$ {cambio_dolar:.2f}
1 Euro = R$ {cambio_euro:.2f}
""")
print("""
Escolha uma opção:
1. Converter de Real para Dólar
2. Converter de Real para Euro
3. Converter de Dólar para Real
4. Converter de Euro para Real
5. Sair
""")

while True:
    opcao = solicitar_numero_inteiro("Digite a opção desejada: ")
    match opcao:
        case 1:
            valor_real = solicitar_numero_float("Digite o valor em Reais: ")
            valor_dolar = valor_real / cambio_dolar
            print(f"\n{valor_real:.2f} Reais equivalem a {valor_dolar:.2f} Dólares.")
            break
        case 2:
            valor_real = solicitar_numero_float("Digite o valor em Reais: ")
            valor_euro = valor_real / cambio_euro
            print(f"\n{valor_real:.2f} Reais equivalem a {valor_euro:.2f} Euros.")
            break
        case 3:
            valor_dolar = solicitar_numero_float("Digite o valor em Dólares: ")
            valor_real = valor_dolar * cambio_dolar
            print(f"\n{valor_dolar:.2f} Dólares equivalem a {valor_real:.2f} Reais.")
            break
        case 4:
            valor_euro = solicitar_numero_float("Digite o valor em Euros: ")
            valor_real = valor_euro * cambio_euro
            print(f"\n{valor_euro:.2f} Euros equivalem a {valor_real:.2f} Reais.")
            break
        case 5:
            print("\nSaindo do conversor. Até logo!")
            break
        case _:
            print("\nOpção inválida. Tente novamente.")