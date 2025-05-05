import math  # Importa o módulo math para usar a função de raiz quadrada

# Função para calcular a média de uma lista de valores
def calcular_media(valores):
    if len(valores) == 0:
        return 0
    return sum(valores) / len(valores)

# Função para calcular a variância de uma lista de valores
def calcular_variancia(valores):
    if len(valores) == 0:
        return 0

    media = calcular_media(valores)
    soma_dos_quadrados = 0
    for valor in valores:
        soma_dos_quadrados += (valor - media) ** 2
    return soma_dos_quadrados / len(valores)

# Função para calcular o desvio padrão
def calcular_desvio_padrao(valores):
    variancia = calcular_variancia(valores)
    return math.sqrt(variancia)

# Lista de valores (exemplo: notas dos alunos)
valores = [8.5, 7.3, 9.0, 6.8, 7.5]

# Cálculo do desvio padrão
desvio_padrao = calcular_desvio_padrao(valores)

# Exibição do resultado
print(f"Os valores são: {valores}")
print(f"O desvio padrão é: {desvio_padrao:.2f}")
