while True:
    try:
        primeiro_numero = int(input("Digite o primeiro número: "))
        segundo_numero = int(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, insira apenas números inteiros.")
        continue
    break

soma = primeiro_numero + segundo_numero

print(f"A soma de {primeiro_numero} e {segundo_numero} é: {soma}")