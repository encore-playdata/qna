
def solution(currentLanes):
    # 차량이 양보했는지 여부 저장하기 위한 리스트 
    check = [False] * len(currentLanes)
    # 차량의 수 카운트 
    cnt = 0
    # D차량 빠져나갈 때까지 반복
    while True: 
        # 첫 번째 차선 이후의 차량이 빠져나갈 시 
        # 다시 첫 번째 차선부터 차량 빠져나감 
        for i in range(len(currentLanes)):
            # 차량 존재하지 않는 차선 스킵 
            if len(currentLanes[i]) == 0:
                continue
            # 마지막 차선에 항상 차가 존재하게하기 위해 
            # 끝부분에 차가 존재하지 않는 차선은 제거 
            # 모든 차선이 양보를 하지 않았을 때 차가 존재하는 마지막 차선의 차량을 
            # 먼저 빠져나가게 하기 위함 
            if len(currentLanes[-1]) == 0:
                currentLanes.pop()
                break
            
            if check[i] == False:
                # 마지막 차선까지 온 경우 해당 차선의 차량 빼기 
                if i == len(currentLanes)-1:
                    car = currentLanes[i][0]
                    if car == 'D':
                        return cnt
                    currentLanes[i] = currentLanes[i][1:]
                    cnt += 1
                    break
                # 양보했음을 체크 
                else:
                    check[i] = True
            # 양보한 적 있는 차량 빼내기 
            # 빼낸 후 양보여부 초기화 
            else:
                car = currentLanes[i][0]
                if car == 'D':
                    return cnt
                currentLanes[i] = currentLanes[i][1:]
                cnt += 1
                check[i] = False
                break


        
    
