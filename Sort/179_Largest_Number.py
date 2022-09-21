class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        for i in range(len(nums)):
            for j in range(i, 0, -1):
                if int(str(nums[j]) + str(nums[j-1])) > int(str(nums[j-1]) + str(nums[j])):
                    nums[j], nums[j-1] = nums[j-1], nums[j]

        return str(int(''.join(map(str, nums))))


test = Solution()
print(test.largestNumber([3, 30, 34, 5, 9]))
