class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        i = 1
        n = len(s)
        while i < n:
            total = total + abs(ord(s[i]) - ord(s[i - 1]))
            i += 1
        return total
        