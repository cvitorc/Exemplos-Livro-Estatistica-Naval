# Função para calcular a média ponderada de uma lista de valores com seus respectivos pesos
def calcular_media_ponderada(valores, pesos):
    # Verifica se a lista está vazia ou se os tamanhos de valores e pesos são diferentes
    if len(valores) == 0 or len(valores) != len(pesos):
        return 0  # Retorna 0 para evitar erro de divisão por zero ou listas incompatíveis
    
    # Calcula a soma dos produtos entre valores e pesos
    soma_ponderada = sum(v * p for v, p in zip(valores, pesos))
    
    # Calcula a soma total dos pesos
    soma_pesos = sum(pesos)
    
    # Calcula a média ponderada dividindo a soma ponderada pela soma dos pesos
    media_ponderada = soma_ponderada / soma_pesos
    
    return media_ponderada

# Exemplo de uso da função
valores = [8.5, 7.3, 9.0, 6.8, 7.5]  # Lista de notas dos alunos
pesos = [2, 3, 4, 1, 2]              # Lista de pesos correspondentes às notas

# Chamada da função para cálculo da média ponderada
media_ponderada = calcular_media_ponderada(valores, pesos)

# Exibe os dados e o resultado formatado com duas casas decimais
print(f"Os valores são: {valores}")
print(f"Os pesos são: {pesos}")
print(f"A média ponderada é: {media_ponderada:.2f}")
