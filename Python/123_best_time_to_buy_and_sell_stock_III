class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1, p2, b1, b2 = 0, 0, -math.inf, -math.inf
        
        for x in prices:
            b1 = max(b1, -x)
            p1 = max(p1, b1+x)
            b2 = max(b2, p1-x)
            p2 = max(p2, b2+x)
        
        return p2
