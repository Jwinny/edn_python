import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Atividade_01.funcoes import solicitar_numero_float, solicitar_numero_inteiro

print("Bem-vindo à calculadora de consumo de combustível!")
distancia_percorrida = solicitar_numero_inteiro("Digite a distância percorrida (em km): ")
combustivel_gasto = solicitar_numero_inteiro("Digite quanto combustivel foi gasto (em litros): ")
consumo_medio = distancia_percorrida / combustivel_gasto
print(f"\nO consumo médio do veículo é de {consumo_medio:.2f} km/l.")
