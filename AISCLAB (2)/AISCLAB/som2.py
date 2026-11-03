import numpy as np

# Input data
X = np.array([[1,1], [1,0], [0,1], [0,0]])

# Initialize weights
np.random.seed(0)
W = np.random.rand(4,2)

# Training
for epoch in range(100):

    for x in X:

        # Calculate distance
        distance = np.linalg.norm(W-x, axis=1)

        # Find best matching unit
        bmu = np.argmin(distance)

        # Update weights
        W[bmu] += 0.5 * (x-W[bmu])

print("Final Weights:")
print(W)