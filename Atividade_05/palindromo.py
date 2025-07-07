print("""
==========================================
        VERIFICADOR DE PALÍNDROMO
==========================================
""")

texto = input("Digite uma palavra ou frase: ")
limpo = ''.join(c.lower() for c in texto if c.isalnum())
if limpo == limpo[::-1]:
    print("Sim")
else:
    print("Não")
print("\nObrigado por usar o Verificador de Palíndromo!")