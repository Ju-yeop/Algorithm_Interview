"""
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
import copy
from sys import stdin

n, m = map(int, stdin.readline().strip().split())
Grid = [list(map(int, stdin.readline().strip().split())) for _ in range(n)]
move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
cnt = 0
visited = copy.deepcopy(Grid)

for i in range(n):
    for j in range(m):
        if Grid[i][j] == 0 or visited[i][j] == 0:
            continue
        ls = [[i, j]]
        while ls:
            x, y = ls.pop()
            for v in range(4):
                m_x = x + move[v][0]
                m_y = y + move[v][1]
                if -1 < m_x < n and -1 < m_y < m:
                    if visited[m_x][m_y] == 1:
                        visited[m_x][m_y] = 0
                        ls.append([m_x, m_y])
        cnt += 1

print(cnt)