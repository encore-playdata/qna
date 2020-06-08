def solution(s):
    answer = len(s)
    unit = 1
    while unit <= len(s)//2:
        word = ''
        count = 1
        comp = s[:unit]
        for i in range(unit, len(s), unit):
            if comp == s[i: i+unit]:
                count += 1
            else:
                if count == 1:
                    word += comp
                else:
                    word += (str(count) + comp)
                comp = s[i: i+unit]
                count = 1

        if count == 1:
            word += comp
        else:
            word += str(count) + comp

        unit += 1
        answer = min(len(word), answer)

    return answer
