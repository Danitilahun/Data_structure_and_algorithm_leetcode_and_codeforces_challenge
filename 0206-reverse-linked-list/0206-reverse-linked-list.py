# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1. Brute force Approch
        - change it to array and reverse it and then change the value of the nodes to the new array value.
        Time complexity = O(N) , Space Complexity = O(N)
        
        2. Space is costly part
        To solve I need to find O(1) space complexity method by manipulating the Linkedlist. 
        1. Single linked list is one way (directed path), So I will try to reverse it while travling to tail
        Algorithm:
        1. I will have one variable prev that hold the previou element before any node
        2. I will have variable to store old next of the current node 
        3. I will asign current node next to prev 
        4. For next iteration the next node prev will be the current node


        """

        prev = None
 
        while head:
            new_head = head.next
            head.next = prev
            prev = head
            head = new_head

        return prev

