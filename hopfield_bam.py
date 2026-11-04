import numpy as np

def sign(x):
    return np.where(x>=0,1,-1)

original=np.array([1,1,1,-1,1,1,1,-1]) # max of 2 bits flipped only
noisy=np.array([1,1,1,1,1,1,1,1]
)

W=np.zeros((8,8))

W=np.outer(original,original)

np.fill_diagonal(W,0)

s=noisy.copy()

for i in range(8):
    s=sign(W @ s)

print("Hopfield")
print("Original ",original)
print("Noisy ",noisy)
print("Recalled ",s)


X=np.array([[1,1,-1,-1],[-1,1,-1,1]])
Y=np.array([[1,-1,1],[1,1,1]])

W=X.T @ Y

output=X[0] @ W
print("\nBAM : X to Y : ",sign(output))

output=Y[0] @ W.T
print("BAM : Y to X : ",sign(output))