class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s, p = ' ' + s, ' ' + p
        dp = [[False for _ in range(len(p))] for _ in range(len(s))]
        dp[0][0] = True

        # 첫 행 초기화
        for i in range(1, len(p)):
            if p[i] == '*':
                dp[0][i] = dp[0][i - 2]

        for i in range(1, len(s)):
            for j in range(1, len(p)):
                # i, j 가 매칭 되었을 때 dp[i-1][j-1] 까지 매칭 되어 있다면 True
                if s[i] == p[j] or p[j] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j] == '*':
                    # 2칸 전의 문자가 매칭 되어 있다면 Skip
                    if dp[i][j - 2] is True:
                        dp[i][j] = True
                    else:
                        # aa a*의 경우를 생각
                        if dp[i - 1][j] is True:
                            dp[i][j] = bool(p[j - 1] == s[i] or p[j - 1] == '.')
                        else:
                            dp[i][j] = False

        return bool(dp[-1][-1])


test = Solution()
test.isMatch("ab", ".*c")
