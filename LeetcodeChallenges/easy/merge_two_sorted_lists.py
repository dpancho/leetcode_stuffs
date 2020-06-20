# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        # Make sure l1 is the list with smaller head. We will return l1 at the end.
        if l1.val > l2.val:
            l1, l2 = l2, l1
        # Store the head to return later.
        head = l1
        while l2:
            if l1:
                # If l1 value is less than or equal to l2 value, keep advancing l1.
                if l1.val <= l2.val:
                    prev, l1 = l1, l1.next
                # If we find a value in l2 that is bigger than the current node in l1, we need to insert it before the currrent l1 node.
                else:
                    # Store l2.next for later use.
                    l2_next = l2.next
                    # Insert l2 node before the l1 node.
                    prev.next = l2
                    l2.next = l1
                    prev = l2
                    # Advance l2. Do not advance l1.
                    l2 = l2_next
            # We have exhausted all nodes in l1, so we can append the current node of l2 to the tail of l1 and be done.
            else:
                prev.next = l2
                return head
        return head