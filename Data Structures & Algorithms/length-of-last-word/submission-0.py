class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lis = list(map(str, s.split()))
        return len(lis[len(lis) - 1])
        