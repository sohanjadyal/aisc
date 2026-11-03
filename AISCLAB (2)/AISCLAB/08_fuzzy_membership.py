import numpy as np
import matplotlib.pyplot as plt

# Triangular membership; for a < b < c
def triangular(x, a, b, c):
    return np.maximum(0, np.minimum((x-a)/(b-a), (c-x)/(c-b)))

for v in [10,15,20,25,30]:
    print(v, triangular(v, 10,20,30))

x = np.linspace(0,40,201)
plt.figure()
plt.plot(x, triangular(x, 0,10,20), label="Cold")
plt.plot(x, triangular(x, 10,20,30), label="Warm")
plt.plot(x, triangular(x, 20,30,40), label="Hot")
plt.title("Temperature Membership Functions")
plt.xlabel("Temperature")
plt.ylabel("Membership")
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig("08_fuzzy_membership.png")
plt.show()

