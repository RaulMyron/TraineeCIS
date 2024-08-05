import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Gerar dados de exemplo
np.random.seed(0)
x = np.random.rand(100) * 10  # 100 pontos entre 0 e 10
y = 2.5 * x + np.random.randn(100) * 5  # Linha base com ruído

# Calcular a regressão linear
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# Função da linha de regressão
def linear_regression(x):
    return slope * x + intercept

# Geração dos valores previstos para a linha de regressão
regression_line = linear_regression(x)

# Plotar os dados e a linha de regressão
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Dados')
plt.plot(x, regression_line, color='red', label=f'Regressão Linear: y={slope:.2f}x+{intercept:.2f}')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regressão Linear')
plt.legend()
plt.show()
