# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = list1, list2
        merge = ListNode()

        cur3 = merge

        while cur1 and cur2:

            if cur1.val >= cur2.val:
                cur3.next = cur2
                cur3 = cur3.next
                cur2 = cur2.next
                
            
            else:
                cur3.next = cur1
                cur3 = cur3.next
                cur1 = cur1.next
        
        if cur1:
            cur3.next = cur1
        
        if cur2:
            cur3.next = cur2
        
        return merge.next

        