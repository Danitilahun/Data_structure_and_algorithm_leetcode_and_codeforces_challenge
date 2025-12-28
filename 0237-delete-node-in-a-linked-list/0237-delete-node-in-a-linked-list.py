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
        Approach 1: Shift the node values
        - Since we are guaranteed that the give node is not last node, we can traverse the linkedlist 
          starting from the node and update the value of the current node with the value of 
          current.next.val until current.next.next is not null.

        Algorithm:
        - Else traverse the linked list using the condition node.next.next is not null. 
        - Update the value of each node with the value of its adjecent node
        - finally make node.next null.

         Time Complexity : O(K) , K is number of element after the given node.
         Space Complexity : O(1)

        Approach 2: Constant time solution
        - Build on top of solution one, After I change the value of the node with the value of its next,
        what if I remove the next element ? 
        Algorith:
        - Make the value of the node to be the value of node.next.val
        - Update the node.next to be node.next.next

        Time Complexity : O(1) 
        Space Complexity : O(1)

        """
        # Approach 1:
        # while node.next.next:
        #     node.val = node.next.val
        #     node = node.next

        # node.val = node.next.val
        # node.next = None

        # Approach 2:
        node.val = node.next.val
        node.next = node.next.next
        