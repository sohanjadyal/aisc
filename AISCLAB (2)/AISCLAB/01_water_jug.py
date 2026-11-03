from collections import deque
def water_jug():
    visited = set()
    q = deque()
    q.append((0, 0))
    while q:
        a, b = q.popleft()
        if (a, b) in visited:
            continue
        visited.add((a, b))
        print(a, b)
        if a == 2:
            print("Goal Reached!")
            return
        states = [
            (4, b),                 # Fill A
            (a, 3),                 # Fill B
            (0, b),                 # Empty A
            (a, 0),                 # Empty B
            (a-min(a, 3-b), b+min(a, 3-b)),  # A to B
            (a+min(b, 4-a), b-min(b, 4-a))   # B to A
        ]
        for state in states:
            if state not in visited:
                q.append(state)
water_jug()
