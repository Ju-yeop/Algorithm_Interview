class Solution:
    def isMatch(self, s: str, p: str) -> bool:
            """
            ls = [False for _ in range(len(p))]
            result = []
            for i, item in enumerate(p):
                if item == '.' or s[i] == p[i] or (item == '*' and ls[i-1] is True):
                    ls[i] = True
                else:
                    ls[i] = False
            return True
            """
            def recursion(ss: str, pp: str) -> bool:
                if not pp and not ss:
                    return True
                if not pp:
                    return False
                pplen = len(pp)
                sslen = len(ss)
                if pplen > 1 and pp[1] == '*':
                    if recursion(ss, pp[2:]) is True:
                        return True
                    if sslen > 0 and (ss[0] == pp[0] or pp[0] == '.'):
                        return recursion(ss[1:], pp)
                else:
                    if sslen > 0 and (ss[0] == pp[0] or pp[0] == '.'):
                        return recursion(ss[1:], pp[1:])
                return False
            return recursion(s, p)


test = Solution()
test.isMatch("ab", ".*c")