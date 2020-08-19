class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        
        
        if N == 1:
            return list(range(10))
        
        num_list = []
        
        def dfs(N, num):
            
            if N == 0:
                return num_list.append(num)
            
            tail_digit = num % 10
            
            digits = set([tail_digit + K, tail_digit - K])
            
            for d in digits:
                if 0 <= d < 10:
                    dfs(N-1, num*10 + d)
        
        for num in range(1, 10):
            dfs(N-1, num)
            
        return num_list
        
        
#from collections import deque

#class Solution:
#    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
#        deltas = [-K, K] if K > 0 else [K]                    
#
#       results = deque(range(10))
#       while results[0] < threshold:
#            n = results.popleft()
#            if n == 0:
#                continue
#
#            digit = n % 10
#            for delta in deltas:
#                if 0 <= digit + delta <= 9:
#                    results.append(n*10 + digit + delta)
#
#        return results 
