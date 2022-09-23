import heapq

class Solution:
    """
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        points.sort(key=lambda x: (x[0]**2 + x[1]**2))
        return points[:k]
    """

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for (x, y) in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (dist, x, y))

        result = []
        for _ in range(k):
            (dist, x, y) = heapq.heappop(heap)
            result.append((x, y))
        return result


test = Solution()
print(test.kClosest([[3, 3], [5, -1], [-2, 4]], 2))
