# https://leetcode.com/problems/recover-binary-search-tree/

from ..util.tree import TreeNode

class Solution:

    """
    Runtime 0 ms Beats 100.00%
    """
    def solution1(self, root: TreeNode) -> None:
        def dfs(node, li):
            if not node:
                return li
            li = dfs(node.left, li)
            li.append(node)
            return dfs(node.right, li)
        
        inorder = dfs(root, [])
        length = len(inorder)
        first, second = None, None

        for i in range(length - 1):
            if inorder[i].val >= inorder[i + 1].val:
                first = inorder[i]
                break
        for i in range(length - 1):
            if inorder[length-i-2].val >= inorder[length-i-1].val:
                second = inorder[length-i-1]
                break
                
        first.val, second.val = second.val, first.val
        

    """
    Runtime 4 ms Beats 46.12%
    """
    def solution2(self, root: TreeNode) -> None:
        pre, first, second = [None], [None], [None]

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if pre[0] and node.val < pre[0].val:
                if not first[0]:
                    first[0] = pre[0]
                second[0] = node
            pre[0] = node
            dfs(node.right)

        dfs(root)
        first[0].val, second[0].val = second[0].val, first[0].val
