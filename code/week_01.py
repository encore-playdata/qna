
from collections import deque 

def solution(board, moves):
    moves = deque(moves)
    buckets = []
    cnt = 0 

    while moves:
        move = moves.popleft()

        for i in range(len(board)):
            doll = board[i][move-1]

            if doll != 0:
                board[i][move-1] = 0

                if buckets and buckets[-1] == doll:
                    buckets.pop()
                    cnt += 2
                else:
                    buckets.append(doll)
                break

    return cnt
