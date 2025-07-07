# verificador_de_senhas.py

from funcoes_de_verificacao_senha import verificar_senha

def exibir_menu():
    print("""
========================================
   🛡️  VERIFICADOR DE SENHAS  🛡️
========================================
Critérios mínimos:
- Pelo menos 8 caracteres
- Pelo menos 1 número
========================================
""")

def exibir_opcoes():
    print("""
[1] Verificar nova senha
[2] Sair
""")

def main():
    while True:
        exibir_menu()
        exibir_opcoes()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            senha = input("\nDigite sua senha: ")
            mensagem = verificar_senha(senha)
            print(f"\nResultado: {mensagem}")
        elif escolha == "2":
            print("\nEncerrando o verificador. Até mais!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
