def solution(currencies, wantMoney):
    n = len(currencies) # 동전의 가짓수

    dp = [0 for i in range(wantMoney + 1)]
    dp[0] = 1 # 첫번째 동전의 금액과 wantMoney가 같아지는 경우. 예) 2원으로 2원을 만드는 경우. 반드시 한번은 만들 수 있기 때문에 1로 지정 
    
    # 이전번째 동전을 사용하는 경우를 포함해주어야 함 
    for i in currencies: #4 25
        for j in range(i, wantMoney+1): # 현재 금액보다 작은 금액은 만드는 것이 불가능하므로 비교시작점을 동전의 현재 금액부터 시작 
            if j - i >= 0: # 금액 - 돈이 0보다 크거나 같다면 
                dp[j] += dp[j-i] # 해당 금액에서 현재 금액을 뺀 금액을 만드는 경우의 수 + 현재 금액을 만드는 경우의 수 //금액의 경우의 수 저장 
                
    return dp[wantMoney]