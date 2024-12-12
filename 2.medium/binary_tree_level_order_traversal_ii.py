# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/

from ..util.tree import TreeNode

class Solution:

    """
    Runtime 0 ms Beats 100.00%
    """
    def bfs(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
        answer = []
        queue = [root]

        while queue:
            answer.append([])

            n = len(queue)

            for _ in range(n):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                answer[-1].append(node.val)

        return list(reversed(answer))

    """
    Runtime 1 ms Beats 16.34%
    """
    def dfs(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
        answer = []

        def dfs(node, depth):
            if not node:
                return
            if len(answer) <= depth:
                answer.append([])
            answer[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return list(reversed(answer))