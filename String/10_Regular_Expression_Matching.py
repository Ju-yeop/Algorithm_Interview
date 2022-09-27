class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) > len(p):
            return False
        elif len(s) < len(p):
            ls = [False for _ in range(len(p))]
            result = []
            for i, item in enumerate(p):
                if item == '.' or s[i] == p[i] or (item == '*' and ls[i-1] is True):
                    ls[i] = True
                else:
                    ls[i] = False
            return True
