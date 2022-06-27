class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def func(root, low, high):            
            if not root:
                return True
            if not low < root.val < high:
                return False
            
            return func(root.left,low, root.val) and func(root.right, root.val, high)
        
        return func(root,low = float("-inf"), high = float('inf'))
            