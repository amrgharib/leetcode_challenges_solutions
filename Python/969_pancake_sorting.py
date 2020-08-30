# leetcode solution
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        """ sort like bubble-sort
            sink the largest number to the bottom at each round
        """
        def flip(sublist, k):
            i = 0
            while i < k / 2:
                sublist[i], sublist[k-i-1] = sublist[k-i-1], sublist[i]
                i += 1

        ans = []
        value_to_sort = len(A)
        while value_to_sort > 0:
            # locate the position for the value to sort in this round
            index = A.index(value_to_sort)

            # sink the value_to_sort to the bottom,
            #   with at most two steps of pancake flipping.
            if index != value_to_sort - 1:
                # flip the value to the head if necessary
                if index != 0:
                    ans.append(index+1)
                    flip(A, index+1)
                # now that the value is at the head, flip it to the bottom
                ans.append(value_to_sort)
                flip(A, value_to_sort)

            # move on to the next round
            value_to_sort -= 1

        return ans
# Top solution
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        if len(A) == 1:
            return []
        
        m = len(A)
        out = []
        
        while m > 0:
            if A[m-1] != m:
                idx = A.index(m)
                if idx != 0:
                    out.append(idx+1)
                    A = A[:idx+1][::-1] + A[idx+1:]
                out.append(m)
                A = A[:m][::-1]+A[m+1:]
            m -= 1
        return out
