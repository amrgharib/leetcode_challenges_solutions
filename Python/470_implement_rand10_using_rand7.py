# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        r1, r2 = rand7(), rand7()
        while r1 >5:
            r1 = rand7()
        while r2 ==7:
            r2 = rand7()
        return r1 if (r2 <= 3) else (r1+5)
