
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_str = ""
        length = len(s)
        for i in range(length):
            sub_longest_str = s[i]
            for j in range(length - i):
                curr = s[i:length - j]
                if curr == curr[::-1] and len(sub_longest_str) < len(curr):
                    sub_longest_str = curr
                    break

            if len(longest_str) < len(sub_longest_str):
                longest_str = sub_longest_str

            if len(longest_str) >= length - i - 1:
                break

        return longest_str


test = Solution()
print(test.longestPalindrome("babad"))