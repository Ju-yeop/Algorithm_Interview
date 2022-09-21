# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ls = []
        point = head
        while point:
            ls.append(point.val)
            point = point.next
        ls.sort()
        p = head
        for i in range(len(ls)):
            p.val = ls[i]
            p = p.next
        return head
