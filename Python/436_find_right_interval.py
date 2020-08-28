# Top solution
from bisect import bisect_right


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        d = {}

        for i, (start, end) in enumerate(intervals):
            if start not in d: d[start] = i

        starts = list(sorted(d))

        result = []

        for start, end in intervals:
            if end in d:
                result.append(d[end])
            elif end > starts[-1]:
                result.append(-1)
            else:
                idx = bisect_right(starts, end)
                result.append(d[starts[idx]])

        return result
