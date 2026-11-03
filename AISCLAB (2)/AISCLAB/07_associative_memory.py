import numpy as np
# Stored patterns
patterns = np.array([
    [1, -1, 1, -1],
    [-1, 1, -1, 1]
])
# Train network
w = np.zeros((4, 4))
for p in patterns:
    w += np.outer(p, p)
w /= len(patterns)
np.fill_diagonal(w, 0)
# Recall pattern
x = np.array([1, -1, 0, -1])
for i in range(10):
    x = np.sign(w @ x)
    print(x)
print("Recalled:", x)