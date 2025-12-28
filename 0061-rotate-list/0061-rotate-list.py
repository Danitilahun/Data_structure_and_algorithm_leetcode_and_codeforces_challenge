# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Approach 1: Brute force
        - Tool : Rotate(k)≡Reverse(All)+Reverse(0…k)+Reverse(k…N)
        - First, Serialize the linked list to an array. Next, reverse the entire array, followed by 
        localized reversal of the prefix (0...k), and the suffix(k...end). 
        Finally reconstact the linked list based on the new array and return the new head.

        - Costly in terms of space. 
        
        Time Complexity : O(N) , Space Complexity : O(N)

        Approach 2: Inplace
        - The fast or tool, I can use is that, since rotating k times means the order of the last 
          k element and and element range from first to length - k will mentains their order,
          using this fast, I can do it inplace.

        Algorithm :
        - Find the length of the linkedlist, let me name it length and connect tail to head of 
          the linkedlist as short cut.
        - Check it length == 0 to return head
        - Know the reminder r = K % length
        - traverse the linked list up to length - r -1, to have pointer on that last part of 
        length - r , let me call it prev_of_ks
        - create new_head variable and assign prev_of_ks.next to it
        - make prev_of_ks.next = None
        - return new_head
        Time Complexity : O(N) , Space Complexity : O(1)
        """

        length = 1
        current = head

        if not current:
            return head
        
        while current and current.next:
            length +=1
            current = current.next
        current.next = head
        
        reminder = k%length
        prev_of_ks = head
        for _ in range(length - reminder -1):
            prev_of_ks = prev_of_ks.next
        
        new_head = prev_of_ks.next
        prev_of_ks.next = None

        return new_head
        

        
