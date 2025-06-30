import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Atividade_01.funcoes import solicitar_numero_float

def converter_celsius_para_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32
def converter_fahrenheit_para_kelvin(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5/9 + 273.15
def converter_kelvin_para_fahrenheit(kelvin: float) -> float:
    return (kelvin - 273.15) * 9/5 + 32
def converter_celsius_para_kelvin(celsius: float) -> float:
    return celsius + 273.15
def converter_kelvin_para_celsius(kelvin: float) -> float:
    return kelvin - 273.15
def converter_fahrenheit_para_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5/9

def conversor_temperatura() -> None:
    print("Bem-vindo ao conversor de temperatura!")
    while True:
        print("\nEscolha uma opção:")
        print("1. Converter Celsius para Fahrenheit")
        print("2. Converter Fahrenheit para Kelvin")
        print("3. Converter Kelvin para Fahrenheit")
        print("4. Converter Celsius para Kelvin")
        print("5. Converter Kelvin para Celsius")
        print("6. Converter Fahrenheit para Celsius")
        print("0. Sair")
        
        opcao = input("Digite sua opção: ")
        
        if opcao == '0':
            print("Saindo do programa.")
            break
        
        match opcao:
            case '1':
                temperatura = solicitar_numero_float("Digite a temperatura: ")
                resultado = converter_celsius_para_fahrenheit(temperatura)
                print(f"{temperatura} °C é igual a {resultado:.2f} °F")
            case '2':
                temperatura = solicitar_numero_float("Digite a temperatura: ")
                resultado = converter_fahrenheit_para_kelvin(temperatura)
                print(f"{temperatura} °F é igual a {resultado:.2f} K")
            case '3':
                temperatura = solicitar_numero_float("Digite a temperatura: ")
                resultado = converter_kelvin_para_fahrenheit(temperatura)
                print(f"{temperatura} K é igual a {resultado:.2f} °F")
            case '4':
                temperatura = solicitar_numero_float("Digite a temperatura: ")
                resultado = converter_celsius_para_kelvin(temperatura)
                print(f"{temperatura} °C é igual a {resultado:.2f} K")
            case '5':
                temperatura = solicitar_numero_float("Digite a temperatura: ")
                resultado = converter_kelvin_para_celsius(temperatura)
                print(f"{temperatura} K é igual a {resultado:.2f} °C")
            case '6':
                temperatura = solicitar_numero_float("Digite a temperatura: ")
                resultado = converter_fahrenheit_para_celsius(temperatura)
                print(f"{temperatura} °F é igual a {resultado:.2f} °C")
            case _:
                print("Opção inválida, tente novamente.")
                continue
        break
conversor_temperatura()
