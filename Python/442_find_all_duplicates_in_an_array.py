# Without extra space
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dups = []
        for num in nums:
            num = abs(num)
            if nums[num-1] > 0:
                nums[num - 1] *= -1
            else:
                dups.append(num)
        return dups

# With extra space
class Solution2:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dups = []
        nums_set = set()
        for num in nums:
            if num in nums_set:
                dups.append(num)
            else:
                nums_set.add(num)
        return dups
