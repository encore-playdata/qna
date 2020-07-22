def solution(currentLanes):
    cnt = 0
    # 제일 처음 빠져나가는 차는 마지막 인덱스 값
    car = currentLanes[-1][0]
    # 남아있는 차 
    currentLanes[-1] = currentLanes[-1][1:]
    # 마지막 원소의 첫 번째 문자가 D인 경우도 고려해주어야 함 
    if car == 'D': 
        return cnt
    cnt += 1
    
    # D가 나올 때까지 반복 
    idx = 0
    while True:
        # currentLanes 계속 순회하기 위함 
        if idx > len(currentLanes) - 1:
            idx = 0
        # 비어있는 레인이면 스킵하고 다음 레인 탐색 
        if len(currentLanes[idx]) == 0:
            idx += 1
            continue
        else:
            car = currentLanes[idx][0]
            # 먼저 해당 car가 D인지 확인한 이후, cnt 증가시키기
            if car == 'D':
                return cnt
            currentLanes[idx] = currentLanes[idx][1:]
            idx +=1 
            cnt += 1
