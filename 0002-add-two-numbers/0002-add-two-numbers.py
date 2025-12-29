# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach : Using two pointers on the head and One variable to hold carry
        - Since the number are reversed , this make the linkedlist to be found in natural order for addition.

        Algorithm:
        - Create new linkedlist dummy head and create second variable named current to hold value of 
        current nodes additon and carry
        - Create variable named carry and initilize it with 0
        - Traverse both linked lists starting from there head and do that until both are None
        - Inside create summation = carry
        - Check linked list one current node is none or not. If it is not add the value to sum, 
        update the next current pointer of linked list one
        - Check linked list two current node is none or not. If it is not add the value to sum , 
        update the next current pointer of linked list two
        - Create the node with value using sum%10 and update carry using sum//10 
        - make the current.next = new node and current should be updated to current.next
        - finally, Check if carry is 0 or not. If not create Node with that value and make current.next =
        the new node. to Handle edge case when the last sum is above 10 and when they have equal length
        - return dummy.next

        Time Complexity :  O(max(N,M))
        Space Complexity: O(max(N,M))
        """

        carry = 0
        dummy = ListNode()
    
        current = dummy

        while l1 or l2:
            summation = carry
            if l1:
                summation += l1.val
                l1 = l1.next
            if l2:
                summation += l2.val
                l2 = l2.next
            
            New_Node = ListNode(summation%10)
            current.next = New_Node
            current = current.next
            carry = summation // 10
        
        if carry:
            New_Node = ListNode(carry)
            current.next = New_Node
            current = current.next
        
        return dummy.next
