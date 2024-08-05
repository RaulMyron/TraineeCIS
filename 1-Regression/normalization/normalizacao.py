import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

data = np.random.normal(loc=50, scale=15, size=500).reshape(-1, 1)

# Aplicar MinMaxScaler
scaler = MinMaxScaler()
min_max_scaled_data = scaler.fit_transform(data)

# Plotar dados originais e normalizados
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(data, bins=30, color='blue', alpha=0.7)
plt.title('Dados Originais')

plt.subplot(1, 2, 2)
plt.hist(min_max_scaled_data, bins=30, color='orange', alpha=0.7)
plt.title('Dados Normalizados (Min-Max)')

plt.tight_layout()
plt.show()
