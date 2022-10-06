class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        result = ""
        for i in range(len(min(strs))):
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j+1][i]:
                    return result
            result += strs[0][i]
        return result

