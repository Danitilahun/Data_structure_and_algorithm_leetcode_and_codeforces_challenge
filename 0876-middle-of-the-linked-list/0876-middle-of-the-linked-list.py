# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach 1: Two Pass solution
        - First, find the length of the linkedlist.
        - Second iterate over linkedlist until length//2

        Time Complexity: O(N)
        Space Complexity: O(1)

        Approach 2: One pass solution
        - From physics knowlage , I know that distace = Speed * Time.
        - If I consider the length as distace and If I have two pointer that move that distance in different 
          speed pointer1_speed = 2 * pointer2_speed. In same time , when pointer1_speed finish the distance 
          pointer2_speed will be in half of the distance. That means in the middle.
        - Using this fact , I will use two pointer one slow and one fast. fast moves twice as fast as slow.

        Algorithm :
        1. Create two pointer, named slow and fast. Initialize them as head.
        2. Loop over the linkedlist until fast and fast.next is not None. This means until tail node.
        3. Update slow as slow.next, update fast as fast.next.next 
        4. return slow

        Edge cases:
        - When there is only one element-> Handled.
        - When the length is even -> Handled

        Time Complexity: O(N)
        Space Complexity: O(1)
        """

        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow
