def solicitar_numero_inteiro(mensagem: str) -> int:
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print("Por favor, insira apenas números inteiros.")
            continue