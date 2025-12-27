# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        """
        # Approach 1: Brute Force
        - Convert the linked list to an array, reverse the array section, and then rebuild the linked list based on the 
        new order of elements from the array.
        - Time Complexity: O(N)
        - Space Complexity: O(N)

        # Approach 2: In-Place Linked List Update
        - Let me identify what makes this problem a problem (Forensics):

        Obstacle 1: I need to preserve the link to the part of the list before the 'left' index.
            Tool: I should keep the head intact and maintain a pointer immediately before 'left'.
            Let's name that variable 'prev_left'.
            I should also use a dummy node to handle edge cases, such as when left = 1.

        Obstacle 2: I need a way to reverse the elements in the range from 'left' to 'right'.
            Tool: Use three pointers: 'prev', 'current', and 'future' (Lesson from Reverse Linked List I).

        Obstacle 3: I need a way to connect the reversed section to the remaining list after the 'right' index.
            Tool: After I finish iterating, the 'current' pointer (or 'future', depending on implementation) 
            will hold the node after 'right'. Let's refer to this conceptually as 'after_right'.

        Algorithm:
        0. Create a dummy node and point its 'next' to 'head'.
        1. Initialize a variable called 'prev_left' and iterate through the list until it reaches the node at index 'left - 1'.
        2. Initialize 'current = prev_left.next'. 
        Iterate 'right - left' times. Inside the loop, use 'prev' (to hold the reversed history), 
        'current', and 'future' (to avoid losing the rest of the list during pointer updates) 
        to reverse the links.
        3. Reconnection Step 1: The 'current' pointer (which started at 'left') is now the tail of the reversed section.
        Connect it to the rest of the list ('current.next = future' or 'current.next = current' depending on loop exit).
        *Correction*: In your logic, 'prev_left.next' is the node that needs to connect to the remainder.
        4. Reconnection Step 2: Connect 'prev_left.next' to 'prev' (which is now the head of the reversed section).
        5. Return 'dummy.next'.

        - Time Complexity: O(N)
        - Space Complexity: O(1)
        """

        dummy = ListNode()
        dummy.next = head

        prev_left = None
        current = dummy
        for _ in range(left):
            prev_left = current
            current = current.next
        
        current = prev_left.next
        prev = None
        future = None
        
        for _ in range(right - left + 1):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            future = current

        
        # rewiring
        current = prev_left.next
        current.next = future

        prev_left.next = prev

        return dummy.next


        


        