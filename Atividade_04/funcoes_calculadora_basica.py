def soma(a, b):
    try:
        return a + b
    except TypeError:
        return "Erro: Os valores devem ser numéricos."
def subtracao(a, b):
    try:
        return a - b
    except TypeError:
        return "Erro: Os valores devem ser numéricos."
def multiplicacao(a, b):
    try:
        return a * b
    except TypeError:
        return "Erro: Os valores devem ser numéricos."
def divisao(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: Divisão por zero não é permitida." 