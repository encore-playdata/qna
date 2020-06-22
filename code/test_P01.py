def solution(n):
    answer = n-1 

    for i in range(1, n):
        if len(set(str(i))) != len(str(i)): 
            answer -= 1
    
    return answer
           
