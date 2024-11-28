# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from ..util.tree import TreeNode

class Solution:

    """
    Runtime 0 ms Beats 100.00%
    """
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        leftResult = []
        rightResult = []

        def dfs(level, node, left, result=[]):
            if node == None:
                return

            if len(result) <= level:
                result.append([])
            result[level].append(node.val)

            if left:
                dfs(level + 1, node.left, left, result)
                dfs(level + 1, node.right, left, result)
            else:
                dfs(level + 1, node.right, left, result)
                dfs(level + 1, node.left, left, result)
        
        dfs(0, root, True, leftResult)
        dfs(0, root, False, rightResult)

        answer = [None] * len(leftResult)

        for i in range(len(answer)):
            answer[i] = leftResult[i] if i % 2 == 0 else rightResult[i]
        
        return answer
