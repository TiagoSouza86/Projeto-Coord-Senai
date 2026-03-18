# processamento.py

def validar_dados(notas):
    """
    RN: Verifica se a lista de notas não está vazia ou corrompida.
    Retorna True se estiver tudo ok, ou False se houver erro.
    """
    if not notas: 
        return False
    if not isinstance(notas, list): 
        return False
  
    for nota in notas:
        if not isinstance(nota, (int, float)):
            return False
    return True

def calcular_media(notas):
    """Calcula a média aritmética simples."""
    return sum(notas) / len(notas)

def definir_situacao(media):
    """RN: Se a média for menor que 7.0, está em Recuperação."""
    if media < 7.0:
        return "Recuperação"
    return "Aprovado"