class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        # A one-liner using bit maniputaion        
        return n > 0 and n & (n-1) == 0 and n % 3 ==1
        
        # Using a while loop 
        # if n > 0:
        #    while n % 4 ==0:
        #        n /= 4
        #    if n == 1:
        #        return True
        # return False
        

