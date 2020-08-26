from functools import lru_cache

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dur_list = [1, 7, 30]
        
        @lru_cache(None)
        def dp(i):
            if i >= n:
                return 0
            
            min_cost = float('inf')
            j = i
            for c, d in zip(costs, dur_list):
                while j  < n and days[j] < days[i] + d:
                    j += 1
                min_cost = min(min_cost, dp(j)+ c)
            
            return min_cost
        
        return dp(0)



# class Solution:
#     def mincostTickets(self, days, costs):
#     first,last=days[0],days[-1]
#     dp=[0]*(last+1)
#     days=set(days)
#     for i in range(first,last+1):
#         if not i in days:
#         dp[i]=dp[i-1]
#     else:
#         dp[i]=min(
#             dp[i-1]+costs[0],
#             dp[i-7]+costs[1] if i>7 else costs[1],
#             dp[i-30]+costs[2] if i>30 else costs[2],
#         )
#     
#     return dp[last]
