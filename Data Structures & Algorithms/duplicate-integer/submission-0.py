class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dicti = {}
        for num in nums:
            dicti[num] = dicti.get(num, 0) + 1
            if dicti[num] > 1:
                return True
        return False
        