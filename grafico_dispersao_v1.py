import matplotlib.pyplot as plt  # Importa a biblioteca para criação de gráficos

# Cria um gráfico de dispersão (scatter plot) para visualizar a relação entre velocidade e consumo
plt.scatter(df["Velocidade (nos)"], df["Consumo (litros/hora)"], color='blue')

# Adiciona título e rótulos aos eixos
plt.title("Relação entre Velocidade e Consumo de Combustível")
plt.xlabel("Velocidade (nós)")
plt.ylabel("Consumo (litros/hora)")

# Adiciona uma grade para facilitar a leitura do gráfico
plt.grid(True)

# Exibe o gráfico na tela
plt.show()
