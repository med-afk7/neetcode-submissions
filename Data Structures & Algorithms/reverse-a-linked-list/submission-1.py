# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp ,ans = None ,  head

        while  ans  is  not None :
            nextnode  = ans.next  
            ans.next  = temp 
            temp = ans
            ans = nextnode
        return temp