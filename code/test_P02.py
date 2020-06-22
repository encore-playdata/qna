def solution(code):
    dashes = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

    answer = 0
    for c in code:
        answer += dashes[int(c)]
    
    return answer