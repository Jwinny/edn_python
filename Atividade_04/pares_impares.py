pares = 0
impares = 0

while True:
    print("""
========================================
    ANÁLISE DE NÚMEROS PARES E ÍMPARES
========================================
1 - Inserir número
2 - Mostrar contagem
3 - Sair
========================================
""")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        try:
            num = int(input("Digite um número inteiro: "))
            if num % 2 == 0:
                pares += 1
                print("→ Número par.")
            else:
                impares += 1
                print("→ Número ímpar.")
        except ValueError:
            print("→ Entrada inválida.")
    elif opcao == "2":
        print(f"\nTotal de pares: {pares}")
        print(f"Total de ímpares: {impares}")
        input("Pressione ENTER para continuar...")
    elif opcao == "3":
        print("Encerrando o programa.")
        break
    else:
        print("→ Opção inválida.")
