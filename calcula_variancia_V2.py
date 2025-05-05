# Função para calcular a média de uma lista
def calcular_media(valores):
    if len(valores) == 0:
        return 0  # Evita divisão por zero
    return sum(valores) / len(valores)

# Função para calcular a variância de uma lista
def calcular_variancia(valores):
    if len(valores) == 0:
        return 0  # Evita cálculo em lista vazia

    media = calcular_media(valores)  # Calcula a média dos valores
    soma_dos_quadrados = 0

    # Soma os quadrados das diferenças entre os valores e a média
    for valor in valores:
        soma_dos_quadrados += (valor - media) ** 2

    # Divide pela quantidade de valores para obter a variância
    variancia = soma_dos_quadrados / len(valores)
    return variancia

# Lista de valores (exemplo: notas de alunos)
valores = [8.5, 7.3, 9.0, 6.8, 7.5]

# Chama a função e exibe o resultado
variancia = calcular_variancia(valores)

print(f"Os valores são: {valores}")
print(f"A variância é: {variancia:.2f}")
