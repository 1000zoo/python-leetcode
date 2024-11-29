# https://leetcode.com/problems/validate-binary-search-tree/

from ..util.tree import TreeNode

class Solution:

    """
    Runtime 0 ms Beats 100.00%
    """
    def solution1(self, root: TreeNode) -> bool:
        pre = [None]

        def dfs(node):
            if node == None:
                return True
            if not dfs(node.left):
                return False
            if pre[0] != None and node.val <= pre[0]:
                return False
            pre[0] = node.val
            return dfs(node.right)
        
        return dfs(root)

    """
    Runtime 3 ms Beats 35.01%
    """
    def solution2(self, root: TreeNode) -> bool:
        stack = []
        pre = None

        while root != None or stack:
            while root != None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre != None and root.val <= pre.val:
                return False
            pre = root
            root = root.right
        return True
