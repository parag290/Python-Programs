"""
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.

"""


def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None or head.next == None:
            return head
        
        temp = head
        head = head.next

        while temp != None and temp.next != None:
           
            next_node = temp.next
            temp.next = temp.next.next
            next_node.next = temp
            next_node = temp.next
            
            if temp.next != None:
                if temp.next.next != None:
                    temp.next = temp.next.next
                
            temp = next_node
                   
        return head
