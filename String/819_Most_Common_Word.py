class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        dic = {}
        ls = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        words = ls.split()
        for j in words:
            if j not in banned:
                if j in dic.keys():
                    dic[j] += 1
                else:
                    dic[j] = 1
        print(max(dic, key=dic.get))


test = Solution()
test.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])