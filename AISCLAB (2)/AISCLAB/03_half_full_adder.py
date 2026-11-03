def half_adder(a, b):
    s = a ^ b
    c = a & b
    return s, c

print("HALF ADDER")
print("A B | Sum Carry")
for a in [0,1]:
    for b in [0,1]:
        s, c = half_adder(a,b)
        print(a,b,"|",s,c)

def full_adder(a,b,cin):
    s = a ^ b ^ cin
    c = (a & b) | (b & cin) | (a & cin)
    return s,c

print("\nFULL ADDER")
print("A B C | Sum Carry")
for a in [0,1]:
    for b in [0,1]:
        for cin in [0,1]:
            s,c = full_adder(a,b,cin)
            print(a,b,cin,"|",s,c)
