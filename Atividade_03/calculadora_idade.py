import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 
from Atividade_01.funcoes import solicitar_numero_inteiro

def define_faixa_etaria() -> None: 
    while True:
        idade = solicitar_numero_inteiro("Digite a sua idade: ")
        if idade < 0:
            print("Idade inválida.")
            continue
        elif idade < 12:
            print("Você é uma criança.")
        elif idade < 18:
            print("Você é um adolescente.")
        elif idade < 60:
            print("Você é um adulto.")
        else:
            print("Você é um idoso.")
        break

define_faixa_etaria()
