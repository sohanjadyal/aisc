import numpy as np

# Input data (4 patterns)
X = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])

# Initialize weights (4 cluster neurons)
np.random.seed(0)
W = np.random.rand(4, 2)

lr = 0.5
epochs = 100

# Training
for epoch in range(epochs):
    # Decay learning rate over epochs
    alpha = lr * (1 - epoch / epochs)
    
    for x in X:
        # Euclidean distance
        distance = np.linalg.norm(W - x, axis=1)
        
        # Best Matching Unit (BMU)
        bmu = np.argmin(distance)
        
        # Update winning weight
        W[bmu] += alpha * (x - W[bmu])

print("Final Cluster Centroids (Weights):")
print(np.round(W, 2))

print("\nCluster Mapping:")
for x in X:
    distance = np.linalg.norm(W - x, axis=1)
    bmu = np.argmin(distance)
    print(f"Input {x} -> Assigned to Neuron {bmu}")