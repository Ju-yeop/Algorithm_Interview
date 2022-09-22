class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl = list(s)
        tl = list(t)
        sl.sort()
        tl.sort()
        return sl == tl
