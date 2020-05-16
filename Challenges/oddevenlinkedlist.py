# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        '''
        The program should run in O(1) space complexity and O(nodes) time complexity.
        This problem can be solved by using two pointers. 
        We iterate over the link and move the two pointers.
        '''
        
        if head is None:
            return head
        result = head
        p1 = head
        p2 = head.next
        connectNode = head.next
        
        while p1 is not None and p2 is not None:
            t = p2.next
            if t is None:
                break
            p1.next = p2.next
            p1 = p1.next
            
            p2.next = p1.next
            p2 = p2.next
        
        p1.next = connectNode
        
        return result
