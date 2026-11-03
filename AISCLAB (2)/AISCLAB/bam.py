
import numpy as np

# Paired patterns
A = np.array([
    [1, -1, 1],
    [-1, 1, -1]
])

B = np.array([
    [1, -1],
    [-1, 1]
])

# Training
w = np.zeros((3, 2))

for a, b in zip(A, B):
    w += np.outer(a, b)

print("Weight Matrix:")
print(w)

# Recall A to B
a = np.array([1, -1, 1])
b = np.sign(a @ w)
print("A -> B:", b)

# Recall B to A
b = np.array([-1, 1])
a = np.sign(b @ w.T)
print("B -> A:", a)
