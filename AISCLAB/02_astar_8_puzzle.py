import heapq

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal  = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def h(state):
    return sum(
        abs(i//3 - (n-1)//3) + abs(i%3 - (n-1)%3)
        for i, n in enumerate(state) if n != 0
    )

def astar(start):
    pq = [(h(start), 0, start, [start])]
    best = {start: 0}

    while pq:
        f, g, state, path = heapq.heappop(pq)
        if g != best[state]:
            continue

        if state == goal:
            for step in path:
                for i in range(0, 9, 3):
                    print(*step[i:i+3])
                print()
            print("Moves:", g)
            return

        z = state.index(0)
        row, col = divmod(z, 3)
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = row+dr, col+dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                nz = nr*3+nc
                new = list(state)
                new[z], new[nz] = new[nz], new[z]
                new = tuple(new)
                if g+1 < best.get(new, float('inf')):
                    best[new] = g+1
                    heapq.heappush(pq, (g+1+h(new), g+1, new, path+[new]))
    print("No solution")

astar(start)
