import numpy as np
import matplotlib.pyplot as plt
X = np.array([[0,0], [0,1], [1,0], [1,1]])
Y = np.array([[0], [1], [1], [0]])
np.random.seed(1)
w1 = np.random.uniform(-1,1,(2,3))
w2 = np.random.uniform(-1,1,(3,1))
b1 = np.zeros((1,3))
b2 = np.zeros((1,1))
lr = 1.5
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
errors = []
for epoch in range(10000):
    # Forward propagation
    h = sigmoid(X @ w1 + b1)
    o = sigmoid(h @ w2 + b2)
    # Error
    error = Y - o
    total_error = np.sum(error**2)
    errors.append(total_error)
    print("Epoch:", epoch+1)
    print("Error:", round(total_error, 4))
    print("Predictions:", np.round(o.flatten(), 2))
    print()
    if total_error < 0.01:
        print("Training completed at epoch:", epoch+1)
        break
    # Backpropagation
    d2 = error * o * (1-o)
    d1 = (d2 @ w2.T) * h * (1-h)
    # Update weights and biases
    w2 += lr * (h.T @ d2) / 4
    b2 += lr * d2.mean()
    w1 += lr * (X.T @ d1) / 4
    b1 += lr * d1.mean()
print("Final Predictions:")
print(np.round(o, 2))