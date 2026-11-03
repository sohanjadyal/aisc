import numpy as np

# Input data
X = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])

# Target classes
Y = np.array([0, 0, 1, 1])

# Initialize weights (MUST be float)
W = np.array([[1.0, 1.0], [0.0, 0.0]])

# Classes of weights
C = np.array([0, 1])

lr = 0.1

# Training
for epoch in range(10):
    for i in range(4):
        # Calculate Euclidean distance
        distance = np.linalg.norm(W - X[i], axis=1)

        # Find closest weight (BMU)
        bmu = np.argmin(distance)

        # Update weights (LVQ-1 Rule)
        if C[bmu] == Y[i]:
            W[bmu] += lr * (X[i] - W[bmu])
        else:
            W[bmu] -= lr * (X[i] - W[bmu])

# Final predictions
print("Final Prototype Weights:")
print(np.round(W, 3))

print("\nPredictions:")
for x in X:
    distance = np.linalg.norm(W - x, axis=1)
    bmu = np.argmin(distance)
    print(f"{x} -> Class {C[bmu]}")