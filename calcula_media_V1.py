# Lista contendo os valores que serão utilizados no cálculo da média
valores = [42, 40, 48, 53]

# Verifica se a lista não está vazia antes de calcular a média
if len(valores) > 0:
    # Calcula a soma de todos os valores
    soma = sum(valores)
    
    # Calcula a média dividindo a soma pelo número de elementos
    media = soma / len(valores)
    
    # Exibe a média formatada com duas casas decimais
    print(f"Média: {media:.2f}")
else:
    # Caso a lista esteja vazia, exibe uma mensagem informando
    print("Não é possível calcular a média de uma lista vazia.")
