# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach 1: Using Dicrionary
        - Use dictionary to store Node: Index
        - Iterate over the linkedlist
        - Check if node found in the dictionary, If it exist return the index ,
         else put the node with it's index in the dictionary. 
        
        Time Complexity : O(N)
        Space Complexity : O(N)

        Approach 2: Floyd's Cycle Detection Algorithm
        Time Complexity : O(N)
        Space Complexity : O(1)
        """

        if not head or not head.next:
            return None

        tortoise = head
        hare = head

        found = False

        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next

            if hare == tortoise:
                found = True
                break
        
        if found:
            index = 0 
            tortoise = head
            while tortoise != hare:
                hare = hare.next
                tortoise = tortoise.next
                index+=1
            
            return tortoise
        
        return None