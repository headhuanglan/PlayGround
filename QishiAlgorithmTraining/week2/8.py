#https://leetcode.com/problems/reverse-linked-list-ii/description/# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        
        #good solution, if have time , study it next time. 
        https://leetcode.com/problems/reverse-linked-list-ii/discuss/30672/Python-one-pass-iterative-solution
        """
       
      
        def reverseList(head):
            if head is None:
                return None
            if head.next is None:
                return head
            remaining=reverseList(head.next)
            head.next.next=head
            head.next=None
            return remaining
        #
        #[3,5,7   4]
        #[7 5 3   4]
        #m=1
        #n=3
        if m==1:
            left=None
            middle=head
            right=head
            for i in range(n-1):
                right=right.next
            
            
            righthead=right.next
            right.next=None
            
            reversemiddle=reverseList(middle)
            head.next=righthead
            
            return reversemiddle
            
       
        #Input:  1->   2->3->4->   5->NULL, m = 2, n = 4
        #Output: 1->   4->3->2->   5->NULL


        #cut to pices  head ~ m-2
        #               m-1 ~ n-1
        #                n ~ end
        if m>=2:
            left=head
            right=head
            
            for i in range(m-2):
                left=left.next
            
            for i in range(n-1):
                print(right.val)
                right=right.next
                
                
            middle=left.next
            left.next=None
            
            
            middlehead_afterreverse=right
            righthead=right.next
            right.next=None
            
            reversemiddle=reverseList(middle)
            
            
            left.next=middlehead_afterreverse
            middle.next=righthead
            
            return head
            
            
            
        
