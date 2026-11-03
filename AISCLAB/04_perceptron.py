import numpy as np

X = np.array([[0,0], [0,1], [1,0], [1,1]])
Y = np.array([0, 0, 0, 1])

w = np.zeros(2)
b = 0
lr = 1

for epoch in range(10):
    print("\nEpoch:", epoch + 1)
    total_error = 0

    for i in range(4):
        z = np.dot(X[i], w) + b
        y_pred = 1 if z >= 0 else 0

        error = Y[i] - y_pred
        total_error += abs(error)

        w = w + lr * error * X[i]
        b = b + lr * error

        print("Input:", X[i], "Target:", Y[i], "Predicted:", y_pred, "Error:", error)

    print("Weights:", w, "Bias:", b)
    if total_error == 0:
        print("Training completed! (Zero errors across all samples)")
        break

print("\nFinal Predictions:")
for i in range(4):
    z = np.dot(X[i], w) + b
    y_pred = 1 if z >= 0 else 0
    print(X[i], ":", y_pred)