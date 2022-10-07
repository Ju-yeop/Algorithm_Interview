import sys

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        result = sys.maxsize
        comp = sys.maxsize
        nums.sort()
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                if temp == target:
                    return temp
                elif abs(temp - target) < comp:
                    comp = abs(temp - target)
                    result = temp
                if temp - target > 0:
                    right -= 1
                elif temp - target < 0:
                    left += 1

        return result