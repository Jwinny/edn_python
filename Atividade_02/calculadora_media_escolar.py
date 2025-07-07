import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Atividade_01.funcoes import solicitar_numero_float

print("Bem-vindo à calculadora de média escolar!")
lista_de_notas = []
while True:
    nota = solicitar_numero_float("Digite uma nota (ou -1 para sair): ")
    if nota == -1:
        break
    elif 0 <= nota <= 10:
        lista_de_notas.append(nota)
    else:
        print("Nota inválida. Por favor, insira uma nota entre 0 e 10.")
if not lista_de_notas:
    print("Nenhuma nota foi inserida. Encerrando o programa.")
    sys.exit()
else:
    print(
        f"""
    Foram inseridas {len(lista_de_notas)} notas.
    A média das notas é: {sum(lista_de_notas) / len(lista_de_notas):.2f} se você quiser conferir.
    Aqui estão as notas inseridas: {lista_de_notas}
    Obrigado por usar a calculadora de média escolar!
    """
    )