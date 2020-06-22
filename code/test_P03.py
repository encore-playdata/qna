def solution(arr, num):
    day, remain = 0, 0 
    for a in arr:
        tmp = a + remain
        if tmp > num:
            remain = tmp - num
            day += 1
        elif tmp > 0:
            remain = 0
            day += 1
    
    day += remain//num + (0 if remain%num == 0 else 1)
    return day
