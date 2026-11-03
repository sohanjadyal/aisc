import numpy as np

def triangular(x, a, b, c):
    return max(0, min((x-a)/(b-a), (c-x)/(c-b)))

print("Temp  Cold  Warm  Hot")

for x in range(0, 41, 5):
    cold = triangular(x, 0, 10, 20)
    warm = triangular(x, 10, 20, 30)
    hot = triangular(x, 20, 30, 40)

    print(x, round(cold, 2), round(warm, 2), round(hot, 2))