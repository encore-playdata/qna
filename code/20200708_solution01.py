def solution(candles):
    day = 0
    for i in range(len(candles)):
        # 길이가 제일 긴 초부터 불을 붙여야 하므로 역순 정렬 
        candles = sorted(candles, reverse=True)
        # 일자별로 초의 개수를 늘림 
        for j in range(i+1):
            # 만약 해당 초의 길이가 0이면, 불을 붙일 초가 모자라다는 의미이므로 그때의 day 리턴
            if candles[j]==0:
                return day
            # 초의 길이 1씩 감소 
            candles[j] -= 1
        # 해당 일자에 초를 모두 태웠으면 day 1 증가 
        day += 1
    return day
