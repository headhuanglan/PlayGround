#https://leetcode.com/problems/linked-list-cycle/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
                
        if head is None or head.next is None:
            return False

        pt1=head
        pt2=head.next
        while (pt1 is not pt2):
            if pt2==None or pt2.next==None:
                return False

            pt1=pt1.next
            pt2=pt2.next.next

        return True
#O(n) space
#         nodeset=set()
        
#         while head is not None:
#             if head in nodeset:
#                 return True
#             nodeset.add(head)
#             head=head.next
#         return False
        
"""
         public boolean hasCycle(ListNode head) {
    if (head == null || head.next == null) {
        return false;
    }
    ListNode slow = head;
    ListNode fast = head.next;
    while (slow != fast) {
        if (fast == null || fast.next == null) {
            return false;
        }
        slow = slow.next;
        fast = fast.next.next;
    }
    return true;
}
"""

