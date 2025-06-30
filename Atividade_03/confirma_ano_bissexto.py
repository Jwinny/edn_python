import os   
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Atividade_01.funcoes import solicitar_numero_inteiro
def confirmar_ano_bissexto() -> None:
    while True:
        ano = solicitar_numero_inteiro("Digite um ano para verificar se é bissexto: ")
        if ano < 0:
            print("Ano inválido. Por favor, digite um ano positivo.")
            continue
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print(f"{ano} é um ano bissexto.")
        else:
            print(f"{ano} não é um ano bissexto.")
        break
confirmar_ano_bissexto()