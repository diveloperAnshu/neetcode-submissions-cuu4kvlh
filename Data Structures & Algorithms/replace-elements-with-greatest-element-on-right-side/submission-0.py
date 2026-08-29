class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        newArr = [None] * n
        newArr[n - 1] = -1
        highest = arr[n - 1]
        i = n - 2
        while i >= 0:
            newArr[i] = highest
            if arr[i] > highest:
                highest = arr[i]
            i -= 1
        return newArr

        