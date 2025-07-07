from datetime import datetime

print("""
==========================================
        CALCULADORA DE DIAS DE VIDA
==========================================
""")

nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")

if nascimento.count("/") != 2:
    print("→ Formato inválido. Certifique-se de usar dd/mm/aaaa.")
else:
    try:
        data_nasc = datetime.strptime(nascimento, "%d/%m/%Y")
        hoje = datetime.today()
        dias_vividos = (hoje - data_nasc).days
        print(f"Você está vivo há {dias_vividos} dias.")
    except ValueError:
        print("Data inválida. Verifique o dia, mês e ano.")
