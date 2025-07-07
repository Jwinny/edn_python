import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Atividade_01.funcoes import solicitar_numero_float

def calcular_imc() -> None:
    peso = solicitar_numero_float("Digite seu peso em kg: ")
    altura = solicitar_numero_float("Digite sua altura em metros: ")
    imc = peso / (altura ** 2)
    match imc:
        case _ if imc < 18.5:
            classificacao = "Abaixo do peso"
        case _ if 18.5 <= imc < 25:
            classificacao = "Peso normal"
        case _ if 25 <= imc < 30:
            classificacao = "Sobrepeso"
        case _ if 30 <= imc < 35:
            classificacao = "Obesidade grau 1"
        case _ if 35 <= imc < 40:
            classificacao = "Obesidade grau 2"
        case _:
            classificacao = "Obesidade grau 3 ou mórbida"
    print(f"Seu IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")
calcular_imc()