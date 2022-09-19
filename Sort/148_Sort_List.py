# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def quicksort(h, low, high):
            def partition(lo, hi):
                left = lo
                pivot = hi
                for right in range(lo, hi):
                    if h[right] < h[pivot]:
                        h[left], h[right] = h[right], h[left]
                        left += 1
                h[left], h[pivot] = h[pivot], h[left]
                return left
            if low < high:
                pvt = partition(low, high)
                quicksort(h, low, pvt-1)
                quicksort(h, pvt+1, hi)

        quicksort(head, 0, len(head)-1)
        return head


a = Solution()
print(a.sortList([-1, 5, 3, 4, 0]))




