def solution(n, actions):
    # 가방이 어디에 놓여있는지 나타내기 위한 리스트 선언
    # 각 인덱스는 가방의 번호를, 원소는 해당 가방이 놓여있는 가방의 번호를 나타냄 
    # ex) ground[1] = 2 : 1번 가방이 2번 가방 안에 놓여있음 
    # 0: 땅에 놓여있음을 의미 
    # 인덱스와 가방번호를 맞춰주기 위해 n+1 길이의 리스트로 생성 
    ground = [0] * (n+1)

    for action in actions:
        action = action.split(' ') # 공백을 기준으로 action 문자열 분리 
        if action[0] == 'PUT':
            i, j = int(action[1]), int(action[3])
            if (ground[i] | ground[j]) == 0: # 두 가방은 반드시 땅에 놓여있어야 함
                ground[i] = j # i가 j안에 놓여있음을 마킹 
            else:
                return -1
        elif action[0] == 'SET' :
            i = int(action[1])
            if ground[i] == 0: # 가방 i는 반드시 바닥에 놓여있어야 함 
                # ground 리스트를 순회하며 가방이 i안에 있다면
                # 바닥에 놓음(0으로 마킹)
                for j in range(1, n+1):
                    if ground[j] == i: 
                        ground[j] = 0 
            else:
                return -1
        elif action[0] == 'SWAP':
            i, j = int(action[1]), int(action[3])
            if (ground[i] | ground[j]) == 0: # 두 가방은 반드시 땅에 놓여있어야 함
                # ground 리스트를 순회하며 
                # i안에 있는 가방과 j안에 있는 가방을 바꿔줌 
                for c in range(1, n+1):
                    if ground[c] == i:
                        ground[c] = j
                    elif ground[c] == j:
                        ground[c] = i
            else:
                return -1


    # 완성된 ground 리스트에 대해
    # 바닥에 놓여진 가방의 개수를 카운트해준다
    # 만약, 가방이 자신의 가방 번호보다 더 작은 번호의 가방에 들어가있다면, 적절하지 않으므로 -1을 리턴한다 
    ans = 0
    for i in range(1, n+1):
        if ground[i] == 0:
            ans += 1
        elif ground[i] < i:
            return -1
    return ans
