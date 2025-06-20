import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Dados de exemplo
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])  # Duas variáveis independentes
Y = np.array([3, 6, 7, 8, 10])  # Variável dependente

# Criar um objeto de regressão linear
regression_model = LinearRegression()

# Ajustar o modelo aos dados
regression_model.fit(X, Y)

# Coeficientes da regressão
coefficients = regression_model.coef_
intercept = regression_model.intercept_

# Prever os valores para os pontos de dados originais
Y_pred = regression_model.predict(X)

# Prever os valores para novos pontos de dados
X_new = np.array([[6, 7], [7, 8], [8, 9], [9, 10], [10, 11]])
Y_new = regression_model.predict(X_new)

# Plotar o gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X[:, 0], X[:, 1], Y, c='b', label='Dados de exemplo')
ax.scatter(X_new[:, 0], X_new[:, 1], Y_new, c='r', marker='x', s=100, label='Previsão para novos pontos')

ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('Y')
ax.legend()
plt.savefig('sklearn_exemple_multiplo.png')

#plt.show()

