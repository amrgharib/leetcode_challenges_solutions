class Solution:
    def customSortString(self, order: str, str: str) -> str:
        
        counter = collections.Counter(str)
        result = []
        for char in order:
            result.append(char * counter[char])
            counter[char] = 0
            
        for char in counter:
            result.append(char * counter[char])
            
        return ''.join(result)
