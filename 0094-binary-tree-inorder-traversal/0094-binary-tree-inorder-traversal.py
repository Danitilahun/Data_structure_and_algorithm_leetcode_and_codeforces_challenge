# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            []
    
        def traverse(root,answer):
            if not root:
                return 
            traverse(root.left,answer)
            answer.append(root.val)
            traverse(root.right,answer)

        answer = []
        traverse(root,answer)

        return answer
            

        
        