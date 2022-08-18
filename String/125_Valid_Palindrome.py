import copy


class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = []
        for al in s:
            if al.isalnum():
                ls.append(al.lower())
        temp = copy.deepcopy(ls)
        ls.reverse()
        return ls == temp


a = Solution()
print(a.isPalindrome("Appa"))
