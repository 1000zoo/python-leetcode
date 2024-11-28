# https://leetcode.com/problems/binary-tree-level-order-traversal/

from ..util.tree import TreeNode

class Solution:

    """
    Runtime 0 ms Beats 100.00%
    """
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        answer = []

        def dfs(level, node):
            if node == None:
                return
            if len(answer) <= level:
                answer.append([])
            answer[level].append(node.val)

            dfs(level + 1, node.left)
            dfs(level + 1, node.right)
        
        dfs(0, root)
        return answer
