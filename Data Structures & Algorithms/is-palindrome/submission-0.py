class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = []
        for char in s:
            if char.isalnum():
                item = char.lower()
                clean_str.append(item)
        low = 0
        high = len(clean_str) - 1
        while low <= high:
            if clean_str[low] != clean_str[high]:
                return False
            low += 1
            high -= 1
        return True
        