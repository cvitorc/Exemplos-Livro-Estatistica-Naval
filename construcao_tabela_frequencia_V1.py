import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Lista de dados (exemplo: velocidades das embarcações)
velocidades = [12, 13, 13, 14, 15, 15, 15, 16, 16, 17,
               17, 18, 18, 18, 19, 19, 20, 20, 21, 22,
               22, 22, 23, 23, 23, 24, 24, 24, 25, 26,
               26, 26, 27, 27, 27, 28, 28, 29, 29, 30,
               30, 31, 31, 31, 32, 32, 33, 34, 34, 35]

# Número de classes: usa a raiz quadrada da quantidade de dados
num_classes = int(np.sqrt(len(velocidades)))

# Cria os intervalos de classe igualmente espaçados
intervalos = np.linspace(min(velocidades), max(velocidades), num_classes + 1)

# Calcula a frequência absoluta (quantos dados caem em cada intervalo)
frequencia_abs, limites = np.histogram(velocidades, bins=intervalos)

# Frequência relativa: porcentagem dos dados em cada intervalo
frequencia_rel = frequencia_abs / len(velocidades)

# Frequência acumulada: soma progressiva das frequências
frequencia_acum = np.cumsum(frequencia_abs)

# Pontos médios dos intervalos (para gráficos)
pontos_medios = [(limites[i] + limites[i+1]) / 2 for i in range(len(limites) - 1)]

# Mostra a tabela de frequências
tabela = pd.DataFrame({
    "Intervalo": [f"{int(limites[i])}-{int(limites[i+1])}" for i in range(len(limites)-1)],
    "Ponto Médio": pontos_medios,
    "Freq. Abs.": frequencia_abs,
    "Freq. Rel.": np.round(frequencia_rel, 2),
    "Freq. Acum.": frequencia_acum
})

print(tabela)

# Plota o histograma com pontos médios marcados
plt.figure(figsize=(10, 6))
plt.hist(velocidades, bins=intervalos, edgecolor='black', rwidth=0.9)
plt.title("Histograma das Velocidades")
plt.xlabel("Velocidade (nós)")
plt.ylabel("Frequência")

# Marcar os pontos médios no gráfico
for i in range(len(pontos_medios)):
    plt.text(pontos_medios[i], frequencia_abs[i] + 0.5,
             str(round(pontos_medios[i], 1)), ha='center')
    plt.vlines(pontos_medios[i], 0, frequencia_abs[i], colors='red', linestyles='dashed')

plt.tight_layout()
plt.show()
