# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach 1: Serialize the linkedlist to an array and use two pointers.
        - I can use placeholder and seeker pointers place holder
        Time Complexity : O(N)
        Space Complexity : O(N)

        Approach 2: Using two pointers in the linkedlist
        Time Complexity : O(N)
        Space Complexity : O(1)

        Algorithm :
        1. create placeholder and seeker pointers pointing to head
        2. seeker will go until seeker.val is different from placeholder.val
        3. when it is different I will make placeholder.next = seeker and update placeholder to be 
           equal to seeker,
        4. Repeat step 2 and 3 until seeker becomes null.
        5. finally make placeholder.next null
        6. return head

        Approach 3: Using one pointer
        - If I check the value of node's next and if the value is similar , I delete the next node.

        Algorithm:
        - Initialize pointer named current
        - always check current.next.val if current.next 
            - If similar delete the next, make current.next = current.next.next
            - Else change current = current.next
        - return head
        """

        current = head

        while current and current.next:

            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
            
        return head

