import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Gerar dados de exemplo
data = np.random.normal(loc=50, scale=15, size=500).reshape(-1, 1)

# Aplicar StandardScaler
scaler = StandardScaler()
standardized_data = scaler.fit_transform(data)

# Plotar dados originais e padronizados
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(data, bins=30, color='blue', alpha=0.7)
plt.title('Dados Originais')

plt.subplot(1, 2, 2)
plt.hist(standardized_data, bins=30, color='green', alpha=0.7)
plt.title('Dados Padronizados (média=0, desvio padrão=1)')

plt.tight_layout()
plt.show()
