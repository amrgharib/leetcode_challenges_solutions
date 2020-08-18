class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        
        citations.sort(reverse=True)
        x = 0
        
        for ind, val in enumerate(citations):
            
            if val >= ind+1 and ind+1 > x:
                x = ind+1
                
        return x
