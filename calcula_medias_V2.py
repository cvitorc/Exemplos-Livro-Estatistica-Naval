# Função para calcular a média aritmética de uma lista de valores numéricos
def calcular_media(valores):
    # Verifica se a lista está vazia para evitar divisão por zero
    if len(valores) == 0:
        return 0  
    
    # Calcula a soma de todos os elementos da lista
    soma = sum(valores)
    
    # Calcula a média dividindo a soma pelo número de elementos
    media = soma / len(valores)
    
    return media

# Exemplo de uso da função
valores = [8.5, 7.3, 9.0, 6.8, 7.5]  # Lista de notas de alunos

# Chamada da função para calcular a média
media = calcular_media(valores)

# Exibe os valores da lista e a média calculada com duas casas decimais
print(f"Os valores são: {valores}")
print(f"A média aritmética é: {media:.2f}")
