# Top solution on leetcode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_ll(self, head: ListNode) -> ListNode:
        prev = nex = None
        curr = head
        while curr:
            nex = curr.next # store the next term
            curr.next = prev # then switch next pointer to the previous term
            prev = curr # increment previous term to the current term
            curr = nex # increment current term to the stored old_next_term
        return prev # prev is at the new head
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        prev = None
        slow = fast = l1 = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        l2 = self.reverse_ll(slow)
        while l2.next:
            tmp = l1.next
            l1.next = l2
            l1 = tmp
            
            tmp = l2.next
            l2. next = l1
            l2 = tmp
