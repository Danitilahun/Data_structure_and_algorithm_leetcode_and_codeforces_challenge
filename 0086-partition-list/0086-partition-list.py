# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        Approch 1: Brute force
        - Convert the linked list to an array and solve the problem(Using two new array to hold 
        less than or equal to x ,  greater element and merge them.) , then change the result array to 
        linked list.

        Time Complexity : O(N)
        Space Complexity : O(N)

        Approch 2: Using two linked list(creating new node for each value)
        - Initialize two linked list one hold less than or equal to x and other greather 
        and letter make the next of less than or equal to x tail to greater head

        Time Complexity : O(N)
        Space Complexity : O(N)

        Approch 3: Using two linked list(but working on given node not on new one created)
        - Initialize two linked list one hold less than or equal to x and other greather 
        and letter make the next of less than or equal to x tail to greater head

        Time Complexity : O(N)
        Space Complexity : O(1)
        Algirithm :
        1. initialize 4 pointer 
            - less_than_X_head to hold the head of elements lessthan X
            - less_than_X_pointer to traverse on less than X linked list
            - greater_than_X_head to hold the head of elements greater than X
            - greater_than_X_pointer to traverse on greater than X  linked list
        2. traverse through the orginal linked list 
        3. if element is less than X add it in less_than_X_pointer and update the pointer to point to that new 
        element
        4. if element is greater than X add it in greater_than_X_pointer and update the pointer to point to 
        that new element
        5. When the orginal linked list raversal completed , 
            - first I will make greater_than_X_pointer.next null to avoid loop
            - less_than_X_pointer.next = greater_than_X_head.next
        6. return less_than_X_head.next(To avoid dummy node part)
        """

        less_than_X_head = ListNode()
        less_than_X_pointer = less_than_X_head
        greater_than_X_head = ListNode()
        greater_than_X_pointer = greater_than_X_head

        while head:
            if head.val >= x:
                greater_than_X_pointer.next = head
                greater_than_X_pointer = head
            if head.val < x:
                less_than_X_pointer.next = head
                less_than_X_pointer = head
            head= head.next
        
        greater_than_X_pointer.next = None
        less_than_X_pointer.next = greater_than_X_head.next

        return less_than_X_head.next
            