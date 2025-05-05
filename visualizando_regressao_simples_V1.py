from scipy import stats  # Importa ferramentas estatísticas
import pandas as pd      # (opcional, caso deseje trabalhar com tabelas no futuro)
import matplotlib.pyplot as plt  # Biblioteca para gráficos

# Dados de entrada: velocidade da embarcação (X) e consumo de combustível (Y)
velocidade = [10, 12, 15, 18, 20]
consumo = [60, 72, 90, 108, 120]

# Regressão linear simples: ajusta uma reta do tipo Y = a + bX
slope, intercept, r_value, p_value, std_err = stats.linregress(velocidade, consumo)

# Exibe a equação da reta ajustada
print(f"Equação da reta: Y = {intercept:.2f} + {slope:.2f}X")

# Exibe o coeficiente de correlação (indica a força da relação linear)
print(f"Coeficiente de correlação: {r_value:.2f}")

# Calcula os valores previstos (Y) com base no modelo ajustado
y_pred = [intercept + slope * x for x in velocidade]

# Cria o gráfico: pontos reais e linha de regressão
plt.scatter(velocidade, consumo, label="Dados observados")
plt.plot(velocidade, y_pred, color='red', label="Reta de regressão")

# Ajustes visuais do gráfico
plt.xlabel("Velocidade (nós)")
plt.ylabel("Consumo (litros/hora)")
plt.title("Regressão Linear Simples")
plt.legend()
plt.grid(True)
plt.show()
