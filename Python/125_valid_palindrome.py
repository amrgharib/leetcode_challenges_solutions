class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        
        i, j = 0, len(s)-1
        
        for char in set(s):
            if not char.isalnum():
                s = s.replace(char, '')
                
        if s.casefold() == s[::-1].casefold():
            return True
        return False
