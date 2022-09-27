class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        con = nums1
        for i in nums2:
            con.append(i)
        con.sort()
        length = len(con)
        if length % 2 == 0:
            return (con[length // 2] + con[length // 2 - 1]) / 2
        else:
            return con[length // 2]

