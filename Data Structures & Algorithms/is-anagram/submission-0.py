class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        newStr1 = "".join(sorted(s))
        newStr2 = "".join(sorted(t))
        if len(s) != len(t):
            return False
        else:
            for i in range(len(newStr1)):
                if newStr1[i] != newStr2[i]:
                    return False
            return True