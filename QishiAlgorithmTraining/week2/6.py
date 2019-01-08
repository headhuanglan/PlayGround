#https://leetcode.com/problems/linked-list-cycle-ii/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pt1= head
        pt2 = head

        while pt2 is not None:
            # move cur slow
            pt1 = pt1.next

            # move cur fast
            pt2 = pt2.next
            if pt2 is None:
                return None
            pt2 = pt2.next

            # Meeting point
            if pt1 == pt2:
                pt2=head
                while pt2 != pt1:
                    pt2 = pt2.next
                    pt1 = pt1.next

                return pt1

        return None
        
