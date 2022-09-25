from sys import stdin
import math

## 출발점과 도착점이 몇개의 원안에 있는지, 같은 원안에 있다면 count 하지 않는다.
N = int(stdin.readline())
for _ in range(N):
    startX, startY, endX, endY = map(int, stdin.readline().split())
    planet = int(stdin.readline())
    planet_ls = [list(map(int, stdin.readline().strip().split())) for _ in range(planet)]
    judge = [False for _ in range(planet)]
    i = 0
    for x, y, r in planet_ls:
        if math.sqrt((x - startX) ** 2 + (y - startY) ** 2) < r:
            judge[i] = True
        if math.sqrt((x - endX) ** 2 + (y - endY) ** 2) < r:
            if judge[i] is True:
                judge[i] = False
            else:
                judge[i] = True
        i += 1
    print(judge.count(True))

