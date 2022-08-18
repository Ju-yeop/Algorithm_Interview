class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        for one in logs:
            if one.split()[1].isdigit():
                digits.append(one)
            else:
                letters.append(one)
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits


test = Solution()
print(test.reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))