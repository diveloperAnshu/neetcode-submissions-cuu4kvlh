class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        n = len(s)
        i = 0
        j = 0
        maxLen = 0
        while j < n:
            mp[s[j]] = mp.get(s[j], 0) + 1
            mpLen = len(mp)
            if mpLen == (j - i + 1):
                maxLen = max(maxLen, (j - i + 1))
                j += 1
            else:
                while mpLen != (j - i + 1):
                    mp[s[i]] = mp.get(s[i], 0) - 1
                    if mp[s[i]] <= 0:
                        del(mp[s[i]])
                    i += 1
                    
                maxLen = max(maxLen, (j - i + 1))
                j += 1
        return maxLen

            