"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?


"""

def removeNthFromEnd(self, head, n): 
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
   
        """
        
        if not head:
            return head
        
        node = head
        cnt = 1
        
        while cnt < n:
            node = node.next
            cnt +=1
        
        if node.next:
            node = node.next
            prev = head
            while node.next:
                node = node.next
                prev = prev.next
            
            prev.next = prev.next.next
            return head
        
        else:
            return head.next
