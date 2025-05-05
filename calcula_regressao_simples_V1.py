from scipy import stats  # Importa funções estatísticas da biblioteca SciPy
import pandas as pd      # (opcional, se for usar com DataFrame)

# Dados de exemplo: velocidade da embarcação (X) e consumo de combustível (Y)
velocidade = [10, 12, 15, 18, 20]
consumo = [60, 72, 90, 108, 120]

# Calcula a regressão linear simples: Y = a + bX
slope, intercept, r_value, p_value, std_err = stats.linregress(velocidade, consumo)

# Exibe a equação da reta ajustada
print(f"Equação da reta: Y = {intercept:.2f} + {slope:.2f}X")

# Exibe o coeficiente de correlação (indica a força da relação linear)
print(f"Coeficiente de correlação: {r_value:.2f}")
