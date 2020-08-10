class Solution:
    def titleToNumber(self, s: str) -> int:
        ind = 0
        while len(s):
            ind, s = ind * 26 + ord(s[0]) - 64, s[1:]

        return ind