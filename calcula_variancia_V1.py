# Lista de valores (exemplo: notas de alunos)
valores = [8.5, 7.3, 9.0, 6.8, 7.5]

# Verifica se a lista não está vazia
if len(valores) > 0:
    # Calcula a média dos valores
    soma = sum(valores)
    media = soma / len(valores)

    # Calcula a soma dos quadrados das diferenças entre cada valor e a média
    soma_dos_quadrados = 0
    for valor in valores:
        soma_dos_quadrados += (valor - media) ** 2

    # Calcula a variância dividindo a soma das diferenças pelo número de valores
    variancia = soma_dos_quadrados / len(valores)

    # Exibe os resultados
    print(f"Os valores são: {valores}")
    print(f"A média é: {media:.2f}")
    print(f"A variância é: {variancia:.2f}")
else:
    print("A lista está vazia. Não é possível calcular a variância.")
