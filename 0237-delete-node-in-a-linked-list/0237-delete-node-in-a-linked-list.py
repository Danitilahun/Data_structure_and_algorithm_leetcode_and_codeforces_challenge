# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        """
        Approach : Shift the node values
        - Since we are guaranteed that the give node is not last node, we can traverse the linkedlist 
          starting from the node and update the value of the current node with the value of 
          current.next.val until current.next.next is not null.

        Algorithm:
        - Else traverse the linked list using the condition node.next.next is not null. 
        - Update the value of each node with the value of its adjecent node
        - finally make node.next null.
        """
        
        while node.next.next:
            node.val = node.next.val
            node = node.next

        node.val = node.next.val
        node.next = None