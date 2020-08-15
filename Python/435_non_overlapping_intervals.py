class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        length = len(intervals)
        if length < 2:
            return 0
        
        intervals.sort()
        
        n = comp_idx = 0
        
        for i in range(1, length):
            if intervals[i][0] < intervals[comp_idx][1]:
                n += 1
                if intervals[i][1] < intervals[comp_idx][1]:
                    comp_idx = i
            else:
                comp_idx = i
        return n
