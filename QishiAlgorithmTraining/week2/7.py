#https://leetcode.com/problems/reverse-linked-list/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        Input: 1->2->3->4->5->NULL
        Output: 5->4->3->2->1->NULL

        """
        if head is None:
            return None
        if head.next is None:
            return head
        
        
        remaining=self.reverseList(head.next)
        head.next.next=head
        head.next=None
    
        return remaining
        
