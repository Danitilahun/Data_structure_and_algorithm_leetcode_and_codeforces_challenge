# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        
        1. Brute force Approch
        - Convert the linked list into an array ,reverse the array, and then re-populate the nodes based on the new array.
        Time complexity = O(N) , Space Complexity = O(N)
        
        2. Space is the costly part in the Brute force Approch.

        - I need to find O(1) space solution by manipulating the Linkedlist in-place. 
        1. Because Single linked list is unidirectional,I must reverse the link while traversing to the tail.

        I want to change A -> B to A <- B. To do that, A must know about Previous. For the very first node (the original Head), 
        what is the "Previous"?     
        There is no previous node. It points to the void (Nothingness).
        prev = None. 
        Also, if I change A, I lose B.
        Therefore, I must capture B first. Thus, I logically require three holding states.

        Obstacle (Forensics): I need to change Current to point to Past.
            Tool: I need a pointer for Past (I call this prev).
        Obstacle (Forensics): When I point Current to Past, I lose Future.
            Tool: I need a temporary pointer to hold Future before I cut the wire (I call this new_head).
        Obstacle (Forensics): I need to move forward, but I am standing on the node I just modified.
            Tool: I need to update my "Frame of Reference" to the Future node I saved.

        Algorithm:
        - Initialize a pointer, prev, to track the predecessor of the current node (initially null).

        - Use a temporary variable to preserve the reference to the next node (the successor).

        - Re-point the current node's next pointer to prev.

        - Advance the pointers: update prev to be the current node for the next iteration.

        - The final result is stored in prev, which becomes the new head of the reversed list.

        """

        prev = None
 
        while head:
            new_head = head.next
            head.next = prev
            prev = head
            head = new_head

        return prev

