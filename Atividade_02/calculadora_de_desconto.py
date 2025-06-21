import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Atividade_01.funcoes import solicitar_numero_inteiro, solicitar_numero_float

print("Bem-vindo à calculadora de desconto!")
valor_unitario = 50.00
porcentagem_desconto = 20
print(
f"""
╔══════════════════════════════════╗
║   🎉 PROMOÇÃO IMPERDÍVEL! 🎉     ║
╠══════════════════════════════════╣
║ 👕 Camiseta                      ║
║ 💰 De: R$ {valor_unitario:.2f}                  ║
║ 🔻 Com desconto de: {porcentagem_desconto}%          ║
╠══════════════════════════════════╣
║ 📦 Estoque limitado! Aproveite!  ║
╚══════════════════════════════════╝
"""
)

quantidade_de_camisetas = solicitar_numero_inteiro("Quantas camisetas gostaria de comprar hoje? ")
valor_total = valor_unitario * quantidade_de_camisetas
desconto = (valor_total * porcentagem_desconto) / 100
valor_final = valor_total - desconto
print("Certo !!\n")
print(
f"""
 ════════════════════════════════════════════
║              📦 RESUMO DO PEDIDO           ║
 ════════════════════════════════════════════
 👕 Produto        : Camiseta               
 💲 Preço unitário : R$ {valor_unitario:.2f}
 🔢 Quantidade     : {quantidade_de_camisetas:<2}
 🧾 Valor total    : R$ {valor_total:.2f}
 💸 Desconto       : R$ {desconto:.2f}
 💰 Valor final    : R$ {valor_final:.2f}

"""
)