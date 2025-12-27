# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Approach 1: Bruteforce
        - Convert the linkedlist to array and check if it is palindrome or not using
         two pointers(colliding pointers.)

        - Time Complexity: O(N)
        - Space Complexity: O(N)

        Approch 2: Inplace

        - Since space is the costly part here, I should use implace way of checking
        - Fact(Rule of the problem): Palindrome are symetric from center. So if I get the center , 
         then reverse the next half and interate over both of them , and then check if the value
         in that position is same or not. 

        - Forensic(Obstacle 1): Length can be odd or even. This means finding center need caution.
        - Forensic(Obstacle 2): How to find the center of linked list ? Using Fast and Slow poiter. 
        - Forensic(Obstacle 3): How to reverse the other half? Using Linked list reversal technique 
        learnt when solving problem. Using 3 pointer to track past(prev), present(current), 
        future nodes to avoid lossing referece.

        Algorithm:
        1. Initialize two variables named fast and slow, and initialize both from head 
        3. Traverse the linked list. So the slow will point to center
        4. reverse slow.next to tail using three pointers prev, current and future
        5. use prev and head and iterate until one of them becomes null and check the value in each
            - if there is a missmatch return false
            - else return true

        - Time Complexity: O(N)
        - Space Complexity: O(1)
        """

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse slow.next to tail
        prev = None
        current = slow.next
        while current:
            next_current = current.next
            current.next = prev
            prev = current
            current = next_current
        # check palindrome
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next

        return True
    
