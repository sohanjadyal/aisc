def mcp(x, w, t):
    return int(sum(a*b for a, b in zip(x, w)) >= t)

def half_adder(a, b):
    OR = mcp([a, b], [1, 1], 1)
    AND = mcp([a, b], [1, 1], 2)
    SUM = mcp([OR, AND], [1, -2], 1)
    return SUM, AND

def full_adder(a, b, cin):
    s1, c1 = half_adder(a, b)
    s2, c2 = half_adder(s1, cin)
    carry = mcp([c1, c2], [1, 1], 1)
    return s2, carry

print("HALF ADDER")
print("A B | Sum Carry")
for a in range(2):
    for b in range(2):
        print(a, b, "|", *half_adder(a, b))

print("\nFULL ADDER")
print("A B Cin | Sum Carry")
for a in range(2):
    for b in range(2):
        for cin in range(2):
            print(a, b, cin, "|", *full_adder(a, b, cin))