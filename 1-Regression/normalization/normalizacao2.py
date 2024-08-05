import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(loc=50, scale=15, size=500).reshape(-1, 1)

from sklearn.preprocessing import MaxAbsScaler

# Aplicar MaxAbsScaler
scaler = MaxAbsScaler()
max_abs_scaled_data = scaler.fit_transform(data)

# Plotar dados originais e normalizados
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(data, bins=30, color='blue', alpha=0.7)
plt.title('Dados Originais')

plt.subplot(1, 2, 2)
plt.hist(max_abs_scaled_data, bins=30, color='purple', alpha=0.7)
plt.title('Dados Normalizados (Max-Abs)')

plt.tight_layout()
plt.show()
