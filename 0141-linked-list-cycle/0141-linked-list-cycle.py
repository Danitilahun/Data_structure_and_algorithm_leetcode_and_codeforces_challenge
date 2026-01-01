# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Approach 1: Using set 
        - Iterating over the linkedlist, check if node already exist in the set or not, 
        if exist return that True, else put the node in the set.
        - Where N is the number of nodes till the first Cyclic node.
        Time Complexity : O(N)
        Space Complexity : O(N)

        Approach 2: Floyd's Cycle Detection Algorithm, also known as the "Tortoise and Hare" algorithm
        - Create two variables(pointers) named tortoise and hare. Assign head for both.
        - hare moves twice as fast as tortoise. Since there is a cycle after some time they will meet 
        if there is cycle. 


        Edge cases:
        0. When the head is None
        1. When there is only one element


        Time Complexity : O(N)
        Space Complexity : O(1)
        """

        if not head or not head.next:
            return False

        hare = head
        tortoise = head

        while hare and hare.next:
            hare = hare.next.next
            
            tortoise = tortoise.next
            
            if hare == tortoise:
                return True
        
        return False