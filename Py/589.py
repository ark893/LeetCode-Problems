class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans=[]
        def solve(root, ans):
            if root:
                ans.append(root.val)
                for child in root.children:
                    solve(child, ans)
            return ans
        return solve(root, ans)