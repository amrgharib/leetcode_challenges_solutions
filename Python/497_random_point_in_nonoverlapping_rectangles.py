class Solution:

    def __init__(self, rects: List[List[int]]):
        areas = [(x2-x1+1)*(y2-y1+1) for x1,y1,x2,y2 in rects]
        
        s = sum(areas)
        
        self.weights = [x/s for x in accumulate(areas)]
        self.rects = rects
        

    def pick(self) -> List[int]:
        sel_rect = bisect.bisect(self.weights, random.random())
        x1,y1,x2,y2 = self.rects[sel_rect]
        return [random.randint(x1,x2), random.randint(y1,y2)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()


#Top solution
#import bisect
#import random

#class Solution:
#
#    def __init__(self, rects: List[List[int]]):
#        self.rects = rects
#        area = 0
#        self.ranges = [area]
#        for x1, y1, x2, y2 in rects:
#            area += (x2 - x1 + 1) * (y2 - y1 +1)
#            self.ranges.append(area)
#
#    def pick(self) -> List[int]:
#        n = random.randint(0, self.ranges[-1] - 1)
#        i = bisect.bisect(self.ranges, n)
#        x1, y1, x2, y2 = self.rects[i-1]
#        n -= self.ranges[i-1]
#        width = x2 - x1 + 1
#        return [x1 + n % width, y1 + n // width]
