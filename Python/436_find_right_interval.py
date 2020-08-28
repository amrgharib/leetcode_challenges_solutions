class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        r_int = []
        start, mp = zip(*sorted((x, i) for i, (x, _) in enumerate(intervals)))
        for x, y in intervals: 
            i = bisect_left(start, y)
            r_int.append(mp[i] if 0 <= i < len(intervals) else -1) # mapping to original index 
        return r_int 

# 
# # Top solution
# from bisect import bisect_right
# 
# 
# class Solution:
#     def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
#     d = {}
# 
# for i, (start, end) in enumerate(intervals):
#     if start not in d: d[start] = i
# 
# starts = list(sorted(d))
# 
# result = []
# 
# for start, end in intervals:
#     if end in d:
#     result.append(d[end])
# elif end > starts[-1]:
#     result.append(-1)
# else:
#     idx = bisect_right(starts, end)
# result.append(d[starts[idx]])
# 
# return result
