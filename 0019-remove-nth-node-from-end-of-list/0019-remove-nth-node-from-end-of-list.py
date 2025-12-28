# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Approach 1: Find length First
        - First find the length of the linked list, then traverse until length - n -1 element,
          change the next of that node to node.next.next

        Time Complexity : O(N)
        Splace Complexity : O(1)

        Approch 2: using two pointer and dummy node
        - initialize dummy node
        - Initialize two pointer left and right, both assigned to dummy
        - right pointer first goes n from the head and left stay at dummy
        - then move each by one together until right.next becomes null
        - That means out left is on the element before the one need to be deleted
        - update left.next to be left.next.next
        - return dummy.next
        """

        dummy = ListNode()
        dummy.next = head

        left = dummy
        right = dummy

        for _ in range(n):
            right = right.next
        
        while right.next:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return dummy.next