import matplotlib.pyplot as plt  # Importa a biblioteca para criação de gráficos
import pandas as pd  # Importa a biblioteca pandas para trabalhar com tabelas de dados

# Cria um conjunto de dados fictícios com velocidade (nós) e consumo (litros por hora)
dados = {
    "Velocidade (nos)": [10, 12, 15, 18, 20],
    "Consumo (litros/hora)": [50, 60, 80, 110, 150]
}

# Cria um DataFrame (tabela de dados) a partir do dicionário
df = pd.DataFrame(dados)

# Calcula a correlação entre as colunas (como elas se relacionam)
correlacao = df.corr()

# Exibe a matriz de correlação no console
print(correlacao)

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
