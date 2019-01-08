#https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
# o(N) o(N) bad!         
#         nodehistory=[]
        
#         while head.next is not None:
#             nodehistory.append(head)
#             head=head.next
        
#         nodehistory.append(head)
        
#         delnode=nodehistory[-n]
        
#         if n+1<=len(nodehistory): 
#             delnode_previous=nodehistory[-(n+1)]
#             delnode_previous.next=delnode.next
#             return nodehistory[0]
#         else:
#             return delnode.next
            
        
        """
        Approach 2: One pass algorithm
        Algorithm
        The above algorithm could be optimized to one pass. Instead of one pointer, we could use two pointers. The first pointer advances the list by    n+1n+1n+1 steps from the beginning, while the second pointer starts from the beginning of the list. Now, both pointers are exactly separated by nnn nodes apart. We maintain this constant gap by advancing both pointers together until the first pointer arrives past the last node. The second pointer will be pointing at the nnnth node counting from the last. We relink the next pointer of the node referenced by the second pointer to point to the node's next next node.
        
        
        
        public ListNode removeNthFromEnd(ListNode head, int n) {
    ListNode dummy = new ListNode(0);
    dummy.next = head;
    ListNode first = dummy;
    ListNode second = dummy;
    // Advances first pointer so that the gap between first and second is n nodes apart
    for (int i = 1; i <= n + 1; i++) {
        first = first.next;
    }
    // Move first to the end, maintaining the gap
    while (first != null) {
        first = first.next;
        second = second.next;
    }
    second.next = second.next.next;
    return dummy.next;
}

       d-1-2-3-4-5      2
            ||   |

        
        """
        
        dummy=ListNode(-1)
        dummy.next=head
        
        first=dummy
        second=dummy
        
        for _ in range(n):
            first=first.next
            
        while first.next is not None:
            first=first.next
            second=second.next

        second.next=second.next.next
        return dummy.next
        
        
 
        
        
        
        
        
        
        
