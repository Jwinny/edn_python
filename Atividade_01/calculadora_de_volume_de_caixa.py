import funcoes
print("📦 Calculadora de volume de caixa")

comprimento = funcoes.solicitar_numero_inteiro("Digite o valor, em centimetros, do comprimento da sua caixa: ")
largura = funcoes.solicitar_numero_inteiro("Digite o valor, em centimetros, da largura da sua caixa: ")
altura = funcoes.solicitar_numero_inteiro("Digite o valor, em centimetros, da altura da sua caixa: ")

volume = comprimento*largura*altura

print(f"O volume da caixa que você informou é de {volume} cm³")  