import funcoes
valor_unitario = 12.40
print("🏬 Bem vindo a loja de cadeiras infantis")
print(
f"""
╔══════════════════════════════════╗
║   🎉 PROMOÇÃO IMPERDÍVEL! 🎉     ║
╠══════════════════════════════════╣
║ 🪑 Cadeira Infantil              ║
║ 💰 De: R$ 19.90                  ║
║ 🔻 Por: R$ {valor_unitario:.2f}                 ║
╠══════════════════════════════════╣
║ 📦 Estoque limitado! Aproveite!  ║
╚══════════════════════════════════╝
"""
)
quantidade_de_cadeiras = funcoes.solicitar_numero_inteiro("Quantas cadeiras infantis gostaria de comprar hoje ? ")
valor_total = valor_unitario*quantidade_de_cadeiras
print("Certo !!\n")
print(f"""
╔════════════════════════════════════════════╗
║              📦 RESUMO DO PEDIDO           ║
╠════════════════════════════════════════════╣
║ 🪑 Produto        : Cadeira Infantil       ║
║ 💲 Preço unitário : R$ {valor_unitario:.2f}               ║
║ 🔢 Quantidade     : {quantidade_de_cadeiras:<2}                     ║
║ 🧾 Valor total    : R$ {valor_total:.2f}               ║
╚════════════════════════════════════════════╝
""")