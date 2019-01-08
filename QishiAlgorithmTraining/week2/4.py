#https://leetcode.com/problems/palindrome-linked-list/description/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # O(n) space
        #         stack=[]
        #         cur=head

        #         lenlist=0
        #         while cur is not None:
        #             lenlist+=1
        #             stack.append(cur)
        #             cur=cur.next

        #         for _ in range(lenlist):
        #             stackpop=stack.pop()
        #             if not  stackpop.val==head.val:
        #                 return False

        #             head=head.next

        #         return True

        if head is None:
            return True

        if head.next is None:
            return True

        cur = head
        lenlist = 0
        while cur is not None:
            lenlist += 1
            cur = cur.next

        # corner case
        if lenlist == 2:
            if not head.val == head.next.val:
                return False
            else:
                return True

        if lenlist == 3:
            if not head.val == head.next.next.val:
                return False
            else:
                return True

        # 1  2  3  |5| 3  2  1
        halflenlist = lenlist // 2

        # reverse first half method
        if lenlist % 2 == 0:
            righthalfpos = halflenlist
        else:
            righthalfpos = halflenlist + 1

        righthalfhead = head
        for _ in range(righthalfpos):
            righthalfhead = righthalfhead.next

        lefthalfhead = head
        for _ in range(halflenlist - 1):
            lefthalfhead = lefthalfhead.next
        lefthalfhead.next=None
       #reverse lefthalf


        def reverse(head):
            if head==None or head.next==None:
                return head
            else:
                remainings= reverse(head.next)
                head.next.next=head
                head.next=None
            return remainings

        lefthalfhead=reverse(head)


        while lefthalfhead is not None:
            if not lefthalfhead.val == righthalfhead.val:
                return False

            righthalfhead = righthalfhead.next
            lefthalfhead = lefthalfhead.next

        return True
