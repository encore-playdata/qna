import sys 
from collections import deque 

N, M = map(int, input().split())
maze = [input() for i in range(N)]

def solution(N, M, maze):
    maze = list(map(lambda x: list(x), maze))
    dist = [[-1]*M for i in range(N)] 
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    q = deque()
    q.append((0,0))
    dist[0][0] = 0
    cnt = 0
    while q:
        cur = q.popleft() 
        for i in range(4):
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if dist[nx][ny] < 0 and maze[nx][ny] == '1':
                    dist[nx][ny] = dist[cur[0]][cur[1]] + 1
                    q.append((nx, ny))

    cnt = dist[N-1][M-1] + 1
    return cnt 
