import numpy as np

# Lista de dados (exemplo)
dados = [480, 500, 495, 510, 505, 490, 500]

# Cálculo da média
media = np.mean(dados)

# Cálculo do desvio padrão amostral (ddof=1)
#ddof=1 garante que o desvio padrão seja amostral, não populacional.
desvio_padrao = np.std(dados, ddof=1)

# Cálculo do Coeficiente de Variação (em %)
%A saída é em porcentagem, como normalmente se apresenta o CV.
cv = (desvio_padrao / media) * 100

# Resultado
print(f"Coeficiente de Variação: {cv:.2f}%")
