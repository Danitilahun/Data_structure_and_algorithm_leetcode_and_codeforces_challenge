# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Using Two Pointers (The Zipper Method)
        - Since both lists are already sorted, I can iterate through them simultaneously, 
          picking the smaller node at each step to attach to our new list.

        Algorithm:
        - Create a dummy node and a 'current' pointer pointing to the dummy.
        - Iterate while BOTH list1 AND list2 are not None:
            - Compare list1.val and list2.val:
                - If list1.val is smaller (or equal):
                    - Point current.next to list1
                    - Move list1 forward (list1 = list1.next)
                - Else (list2.val is smaller):
                    - Point current.next to list2
                    - Move list2 forward (list2 = list2.next)
            - Move 'current' forward (current = current.next) to prepare for the next node.
        
        - After the loop, one list might still have nodes left.
        - If list1 is not None, attach the rest of list1 to current.next.
        - If list2 is not None, attach the rest of list2 to current.next.
        
        - Return dummy.next

        Time Complexity : O(N + M)
        Space Complexity : O(1)
        """

        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next
        
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        return dummy.next
