class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxConsecutive = 0
        
        j = 0
        n = len(nums)
        total = 0
        while j < n:
            if nums[j] == 1:
                total += 1
                maxConsecutive = max(total, maxConsecutive)
                j += 1
            else:
                total = 0
                j += 1
        return maxConsecutive


        