import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import funcoes_media_escolar

def main():
    turma = {}
    while True:
        funcoes_media_escolar.exibir_titulo()
        funcoes_media_escolar.exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            funcoes_media_escolar.registrar_notas(turma)
        elif opcao == "2":
            funcoes_media_escolar.calcular_medias(turma)
            input("\nPressione ENTER para continuar...")
        elif opcao == "3":
            print("\nEncerrando o programa. Até logo! 👋")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
