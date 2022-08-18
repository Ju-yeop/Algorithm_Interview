"""
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""


def dfs(depth, temp):
    if len(temp) == len(digits):
        ls.append(temp)
        return

    for i in range(depth, len(digits)):
        for j in phone[digits[i]]:
            dfs(i + 1, temp + j)


digits = input()
ls = []
phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
dfs(0, "")
print(ls)


