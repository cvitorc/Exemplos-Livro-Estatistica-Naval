import numpy as np
import matplotlib.pyplot as plt

# Lista de dados (exemplo: velocidades das embarcações)
velocidades = [12, 13, 13, 14, 15, 15, 15, 16, 16, 17,
               17, 18, 18, 18, 19, 19, 20, 20, 21, 22,
               22, 22, 23, 23, 23, 24, 24, 24, 25, 26,
               26, 26, 27, 27, 27, 28, 28, 29, 29, 30,
               30, 31, 31, 31, 32, 32, 33, 34, 34, 35]

# Número de classes: raiz quadrada do total de dados (aproximado)
num_classes = int(np.sqrt(len(velocidades)))

# Cria os intervalos de classe igualmente espaçados
intervalos = np.linspace(min(velocidades), max(velocidades), num_classes + 1)

# Calcula a frequência absoluta (quantos dados caem em cada faixa)
frequencia, _ = np.histogram(velocidades, bins=intervalos)

# Mostra o resultado no console
print("Frequência absoluta por faixa:")
print(frequencia)

# Desenha o histograma
plt.hist(velocidades, bins=intervalos, edgecolor='black', rwidth=0.9)
plt.title("Histograma das Velocidades")
plt.xlabel("Velocidade (nós)")
plt.ylabel("Frequência")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
