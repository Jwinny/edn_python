def tem_tamanho_minimo(senha, minimo=8):
    """Verifica se a senha tem pelo menos `minimo` caracteres."""
    return len(senha) >= minimo

def contem_numero(senha):
    """Verifica se a senha contém pelo menos um número."""
    return any(caractere.isdigit() for caractere in senha)

def verificar_senha(senha):
    """Verifica se a senha atende a todos os critérios de segurança."""
    if not tem_tamanho_minimo(senha):
        return False, "A senha deve conter pelo menos 8 caracteres."
    if not contem_numero(senha):
        return False, "A senha deve conter pelo menos um número."
    return True, "Senha válida."
