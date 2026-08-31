class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultList = {}
        result = []
        for str in strs:
            newStr = "".join(sorted(str))
            if resultList.get(newStr, 0) == 0:
                resultList[newStr] = [str]
            else:
                resultList[newStr].append(str)

        for key, value in resultList.items():
             result.append(value)
        return result
        