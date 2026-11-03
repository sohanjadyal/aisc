import numpy as np
import matplotlib.pyplot as plt
from minisom import MiniSom
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans

np.random.seed(42)
iris = load_iris()
X = StandardScaler().fit_transform(iris.data)
y = iris.target

# SOM: 10x10 grid, 1000 iterations, 4 clusters
som = MiniSom(10, 10, 4, sigma=1.5, learning_rate=0.5, random_seed=42)
som.pca_weights_init(X)
som.train_random(X, 1000)
weights = som.get_weights().reshape(-1, 4)
clusters = KMeans(n_clusters=4, random_state=42, n_init=10).fit_predict(weights)

# LVQ: three prototypes, 100 epochs
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
print("SOM: 1000 iterations, 4 clusters")
print("LVQ accuracy:", round(np.mean(pred == y_test)*100, 2), "%")

plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.imshow(clusters.reshape(10,10), cmap="viridis")
plt.title("SOM - 4 Clusters")
plt.colorbar()
plt.subplot(1,2,2)
plt.scatter(X_test[:,0], X_test[:,1], c=pred, cmap="viridis")
plt.title("LVQ - Predictions")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.tight_layout()
plt.savefig("06_som_lvq.png")
plt.show()
