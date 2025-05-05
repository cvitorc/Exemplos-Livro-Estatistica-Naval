# Função para calcular a mediana de uma lista de valores numéricos
def calcular_mediana(valores):
    # Ordena os valores em ordem crescente
    valores_ordenados = sorted(valores)
    n = len(valores_ordenados)
    
    # Verifica se a lista está vazia para evitar erro
    if n == 0:
        return 0  
    
    meio = n // 2  # Índice central da lista

    # Se o número de elementos for par, retorna a média dos dois valores centrais
    if n % 2 == 0:
        mediana = (valores_ordenados[meio - 1] + valores_ordenados[meio]) / 2
    else:
        # Se for ímpar, retorna o valor central
        mediana = valores_ordenados[meio]
    
    return mediana

# Exemplo de uso da função
valores = [8.5, 7.3, 9.0, 6.8, 7.5]  # Lista de notas dos alunos

# Cálculo da mediana
mediana = calcular_mediana(valores)

# Exibição dos resultados
print(f"Os valores são: {valores}")
print(f"A mediana é: {mediana:.2f}")
