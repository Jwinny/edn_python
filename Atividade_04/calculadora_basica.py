import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Atividade_01.funcoes import solicitar_numero_float, solicitar_numero_inteiro
import funcoes_calculadora_basica

def calculadora():
    print("Bem-vindo à calculadora")
    print("""
    Escolha uma opção:
    1. Somar
    2. Subtrair
    3. Multiplicar
    4. Dividir
    5. Sair
    """)
    while True:
        opcao = solicitar_numero_inteiro('Digite a opção desejada: ')
        num1 = solicitar_numero_float("Digite o primeiro número: ")
        num2 = solicitar_numero_float("Digite o segundo número: ")
        match opcao:
            case 1:
                resultado = funcoes_calculadora_basica.soma(num1, num2)
                print(f"\nResultado: {num1} + {num2} = {resultado:.2f}")
                break
            case 2:
                resultado = funcoes_calculadora_basica.subtracao(num1, num2)
                print(f"\nResultado: {num1} - {num2} = {resultado:.2f}")
                break
            case 3:
                resultado = funcoes_calculadora_basica.multiplicacao(num1, num2)
                print(f"\nResultado: {num1} * {num2} = {resultado:.2f}")
                break
            case 4:
                resultado = funcoes_calculadora_basica.divisao(num1, num2)
                print(f"\nResultado: {num1} / {num2} = {resultado:.2f}")
                break
            case 5:
                print("\nSaindo da calculadora. Até logo!")
                break
            case _:
                print("\nOpção inválida. Tente novamente.")
                continue

calculadora()