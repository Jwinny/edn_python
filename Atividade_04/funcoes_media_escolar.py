def exibir_titulo():
    print("""
========================================
       SISTEMA DE NOTAS DA TURMA        
========================================
""")

def exibir_menu():
    print("""
[1] Adicionar aluno
[2] Exibir médias
[3] Sair
""")

def registrar_notas(turma):
    nome = input("Nome do aluno: ").strip()
    if not nome:
        print("Nome inválido.")
        return
    try:
        notas = list(map(float, input("Digite as notas separadas por espaço: ").split()))
        turma[nome] = notas
        print(f"\n✅ Aluno '{nome}' adicionado com sucesso!\n")
    except ValueError:
        print("❌ Entrada inválida. Use apenas números.")

def calcular_medias(turma):
    print("""
----------------------------------------
           MÉDIAS DOS ALUNOS            
----------------------------------------
""")
    if not turma:
        print("Nenhum aluno registrado.")
        return

    total = 0
    for nome, notas in turma.items():
        media = sum(notas) / len(notas) if notas else 0
        print(f"{nome:<25} Média: {media:.2f}")
        total += media

    media_geral = total / len(turma)
    print("\n----------------------------------------")
    print(f"MÉDIA GERAL DA TURMA: {media_geral:.2f}")
    print("----------------------------------------")
