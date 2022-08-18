import collections
import copy

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ls = []
        dct = collections.defaultdict(list)
        for item in strs:
            ls.append(''.join(sorted(item)).strip())
        for i in range(len(ls)):
            if ls[i] in dct.keys():
                dct[ls[i]].append(strs[i])
            else:
                dct[ls[i]] = [strs[i]]
        print(list(dct.values()))


test = Solution()
test.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])