class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      dicti = {}
      i = 0
      for num in nums:
        if (target - num) not in dicti:
            dicti[num] = i
            i += 1
        else:
            return [dicti[target - num], i]
        