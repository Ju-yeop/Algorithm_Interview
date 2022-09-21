class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        length = len(intervals)
        result = [intervals[0]]
        for i in range(1, length):
            if intervals[i][0] <= result[-1][1] <= intervals[i][1]:
                temp = result[-1][0]
                result.pop()
                result.append([temp, intervals[i][1]])
            elif result[-1][1] >= intervals[i][0] and result[-1][1] >= intervals[i][1]:
                continue
            else:
                result.append(intervals[i])
        return result


test = Solution()
print(test.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))