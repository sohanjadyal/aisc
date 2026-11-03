import numpy as np

# Triangular membership function
def triangular(x, a, b, c):
    if a == b:
        return 1 if x <= b else max(0, (c-x)/(c-b))
    if b == c:
        return 1 if x >= b else max(0, (x-a)/(b-a))
    return max(0, min((x-a)/(b-a), (c-x)/(c-b)))

# Input
temp = 26

# Fuzzification
low = triangular(temp, 0, 10, 20)
medium = triangular(temp, 15, 25, 35)
high = triangular(temp, 30, 40, 50)

# Fan speed membership functions
speed = np.arange(0, 101)

slow = np.array([triangular(x, 0, 0, 50) for x in speed])
normal = np.array([triangular(x, 25, 50, 75) for x in speed])
fast = np.array([triangular(x, 50, 100, 100) for x in speed])

# Mamdani inference: MIN + MAX
output = np.maximum.reduce([
    np.minimum(low, slow),
    np.minimum(medium, normal),
    np.minimum(high, fast)
])

# Centroid defuzzification
if output.sum() > 0:
    fan = np.sum(speed * output) / np.sum(output)
    print("Temperature:", temp)
    print("Fan Speed:", round(fan, 2), "%")
else:
    print("No rule activated")
    
if fan < 35:
    print("Fan is Slow")
elif fan < 65:
    print("Fan is Medium")
else:
    print("Fan is Fast")