class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        r1 = [1,1]
        for i in range(3, rowIndex+2):
            r2 = [1] * i
            for j in range(1,i-1):
                r2[j]= r1[j-1]+r1[j]
            r1 = r2
        
        return r1
