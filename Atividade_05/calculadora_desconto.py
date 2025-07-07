print("""
==========================================
      CALCULADORA DE DESCONTO EM PRODUTO
==========================================
""")

try:
    preco = float(input("Digite o preço original do produto: R$ "))
    desconto = float(input("Digite o percentual de desconto (ex: 15 para 15%): "))
    valor_desconto = (preco * desconto) / 100
    preco_final = preco - valor_desconto
    print(f"Preço final com desconto: R$ {preco_final:.2f}")
except ValueError:
    print("Entrada inválida.")
