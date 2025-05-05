import statistics  # Importa o módulo padrão para operações estatísticas

# Lista de dados numéricos
dados = [1, 2, 2, 3, 4, 4, 5, 5, 6, 5, 6, 6, 6, 6, 6, 6, 5, 5, 5]

# Calcula todas as modas (valores mais frequentes)
modas = statistics.multimode(dados)

# Exibe o(s) resultado(s)
if len(modas) == 1:
    print(f"A moda é: {modas[0]}")
else:
    print(f"As modas são: {modas}")
