class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s, p = ' ' + s, ' ' + p
        dp = [[False for _ in range(len(p))] for _ in range(len(s))]
        dp[0][0] = True
        for i in range(1, len(p)):
            if p[i] == '*':
                dp[0][i] = dp[0][i - 2]

        for i in range(1, len(s)):
            for j in range(1, len(p)):
                if s[i] == p[j] or p[j] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j] == '*':
                    if dp[i][j - 2] is True:
                        dp[i][j] = True
                    else:
                        if dp[i - 1][j] is True:
                            dp[i][j] = bool(p[j - 1] == s[i] or p[j - 1] == '.')
                        else:
                            dp[i][j] = False

        return bool(dp[-1][-1])


test = Solution()
test.isMatch("ab", ".*c")
