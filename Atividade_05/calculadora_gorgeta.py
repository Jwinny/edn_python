print("""
====================================
        CALCULADORA DE GORJETA
====================================
""")

try:
    valor_conta = float(input("Digite o valor total da conta: R$ "))
    porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta (ex: 10 para 10%): "))
    gorjeta = (valor_conta * porcentagem_gorjeta) / 100
    print(f"Gorjeta a ser deixada: R$ {gorjeta:.2f}")
except ValueError:
    print("Entrada inválida.")