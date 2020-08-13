# 포인트: 
#   무조건 제일 큰 값을 가져가는 것이 아니라 
#   그룹을 나누거나/ 나누지 않거나 두 가지 선택지 중 최선의 선택해야 함 
# 그룹 나눠질 때마다 재귀적으로 호출
# 각 시퀀스마다 답 저장해놓기
class Solution:
    def solution(self, goldValues):
        self.N = N = len(goldValues)
        self.golds = goldValues.copy()
        
        self.mem = dict()
        ans = prev = 0
        for idx, key in enumerate(self.golds):    
            _, my_gold = self.sub_solution(idx+1, idx)
            ans = max(ans, my_gold + key)
        return ans
        
    def sub_solution(self, bgn, end):
        bgn %= self.N
        end %= self.N
        
        if (bgn, end) in self.mem:
            return self.mem[(bgn, end)]
        
        _len = end - bgn
        if _len < 0: _len += self.N
        
        if _len == 0:   return (0, 0)
        elif _len == 1: return (self.golds[bgn], 0)
        
        ans = (0, 0)
        _end = end if end>bgn else end+self.N
        for _idx in range(bgn, _end):
            ans_l = self.sub_solution(bgn, _idx)
            ans_r = self.sub_solution(_idx+1, end)
            
            tmp = ans_l[1] + ans_r[1] + self.golds[(_idx%self.N)]
            if ans[1] < tmp:
                ans = (ans_l[0] + ans_r[0], tmp)
                
        ans = (ans[1], ans[0])
        self.mem[(bgn, end)] = ans
        return ans
