import math  # Importa o módulo math para usar a função de raiz quadrada

# Lista de valores (exemplo: notas de alunos)
valores = [8.5, 7.3, 9.0, 6.8, 7.5]

# Verifica se a lista não está vazia
if len(valores) > 0:
    # Calcula a média
    media = sum(valores) / len(valores)

    # Calcula a soma dos quadrados das diferenças entre cada valor e a média
    soma_dos_quadrados = 0
    for valor in valores:
        soma_dos_quadrados += (valor - media) ** 2

    # Calcula a variância
    variancia = soma_dos_quadrados / len(valores)

    # Calcula o desvio padrão (raiz quadrada da variância)
    desvio_padrao = math.sqrt(variancia)

    # Exibe os resultados
    print(f"Os valores são: {valores}")
    print(f"O desvio padrão é: {desvio_padrao:.2f}")
else:
    print("A lista está vazia. Não é possível calcular o desvio padrão.")
