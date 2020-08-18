class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = collections.Counter(s)
        is_odd = longest = 0
        for i in d.values():
            if i % 2 ==1:
                is_odd = 1
            longest += i//2 * 2
        return longest + is_odd
        
