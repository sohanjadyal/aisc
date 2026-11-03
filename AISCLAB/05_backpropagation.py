import numpy as np

# Inputs and non-linear XOR targets
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
Y = np.array([[0], [1], [1], [0]])

# Sigmoid activation and its derivative
def sigmoid(x): return 1 / (1 + np.exp(-x))
def d_sigmoid(x): return x * (1 - x)

np.random.seed(42)
w_h = np.random.uniform(size=(2, 2))  # Hidden weights
b_h = np.random.uniform(size=(1, 2))  # Hidden bias
w_o = np.random.uniform(size=(2, 1))  # Output weights
b_o = np.random.uniform(size=(1, 1))  # Output bias

lr = 0.5

for epoch in range(10000):
    # Forward Pass
    h = sigmoid(np.dot(X, w_h) + b_h)
    out = sigmoid(np.dot(h, w_o) + b_o)

    # Backward Pass (Error calculation & propagation)
    d_out = (Y - out) * d_sigmoid(out)
    d_h = d_out.dot(w_o.T) * d_sigmoid(h)

    # Weight and bias updates
    w_o += h.T.dot(d_out) * lr
    b_o += np.sum(d_out, axis=0, keepdims=True) * lr
    w_h += X.T.dot(d_h) * lr
    b_h += np.sum(d_h, axis=0, keepdims=True) * lr

print("Final Predictions for XOR:")
for i in range(4):
    print(X[i], "->", round(out[i, 0], 3), "-> Predicted Class:", int(out[i, 0] >= 0.5))