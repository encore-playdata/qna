
def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        final_line = str(bin(a1 | a2))[2:]
        final_line = '0'*(n - len(final_line)) + final_line
        final_line = final_line.replace('1', '#')
        final_line = final_line.replace('0', ' ')
        answer.append(final_line)

    return answer
    


