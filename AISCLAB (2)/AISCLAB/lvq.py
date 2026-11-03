
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
iris = load_iris()
X = StandardScaler().fit_transform(iris.data)
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
p = np.array([X_train[y_train == i].mean(axis=0) for i in range(3)])
rate = 0.1
for epoch in range(100):
    for x, label in zip(X_train, y_train):
        winner = np.argmin(np.linalg.norm(p - x, axis=1))
        if winner == label:
            p[winner] += rate * (x - p[winner])
        else:
            p[winner] -= rate * (x - p[winner])
    rate *= 0.99
pred = np.array([np.argmin(np.linalg.norm(p-x, axis=1)) for x in X_test])
print("LVQ Accuracy:", round(np.mean(pred == y_test)*100, 2), "%")
plt.scatter(X_test[:, 0], X_test[:, 1], c=pred, cmap="viridis")
plt.title("LVQ - Predictions")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
