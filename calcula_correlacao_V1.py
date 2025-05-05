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
