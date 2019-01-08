#https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        
        Input: 1->1->2->3->3
        Output: 1->2->3
        """
        if head is None:
            return []
        
        pre=head
        cur=head.next
        while cur is not None:
            if pre.val==cur.val:
                pre.next=cur.next
                pre=pre
                cur=cur.next
            
            else:
                pre=cur
                cur=cur.next
                
        return head
