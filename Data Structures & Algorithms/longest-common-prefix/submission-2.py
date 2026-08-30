class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallestStr = ""
        longest = 999999999
        for str in strs:
            if len(str) <= longest:
                smallestStr = str
                longest = len(str)
        i = 0
        resultPrefix = ""
        for ch in str:
            for string in strs:
                if i >= longest or ch != string[i]:
                    return resultPrefix
            resultPrefix += ch
            i += 1

        return resultPrefix
            
        