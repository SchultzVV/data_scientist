import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import random as rd

# Dados de exemplo
#X = np.array([1, 2, 3, 4, 5])
#Y = np.array([2, 4, 5, 4, 5])
X = np.linspace(1,20,20)
print(rd.random()*2*np.pi)
Y = [i*np.cos(rd.random()*2*np.pi)*np.sin(rd.random()*2*np.pi) for i in X]


# Criar um objeto de regressão linear
regression_model = LinearRegression()

# Ajustar o modelo aos dados
X = X.reshape(-1, 1)  # Redimensionar para uma matriz 2D
# print(X)
regression_model.fit(X, Y)

# Fazer previsões
X_new = np.array([[6]])
Y_pred = regression_model.predict(X_new)

y=[]
x = np.linspace(20,35,15).reshape(-1, 1)
print(x)
x_predictions = np.array(x)
for i in x_predictions:
    value = np.array([i])
    print(value)
    y.append(regression_model.predict(value))
#Y_pred2 = regression_model.predict(X_new)


# Coeficientes da regressão
slope = regression_model.coef_[0]
intercept = regression_model.intercept_

# Plotar os dados e a linha de regressão
plt.scatter(X, Y, label='Dados de exemplo')
plt.plot(X, regression_model.predict(X), color='red', label='Regressão Linear')
plt.scatter(X_new, Y_pred, color='green', marker='x', s=100, label='Previsão para X=6')
plt.scatter(x_predictions, y, color='red', marker='x', s=100, label='Previsão para X>20')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.savefig('sklearn_exemple.png')
# plt.show()

print(f"Coeficiente de inclinação (b): {slope}")
print(f"Interceptação (a): {intercept}")
print(f"Previsão para X=6: {Y_pred[0]}")
print(f"Previsão para X=22: {y[0]}")
print(type(y))
print(y)
