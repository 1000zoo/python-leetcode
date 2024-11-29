# https://leetcode.com/problems/path-sum-ii/

from ..util.tree import TreeNode

class Solution:

    """
    Runtime 0 ms Beats 100.00%
    """
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        
        def dfs(node, currSum, path, answer):
            if not node:
                return
            currSum += node.val
            path.append(node.val)
            if currSum == targetSum and not node.left and not node.right:
                answer.append(path[:])
                path.pop()
                return
            dfs(node.left, currSum, path, answer)
            dfs(node.right, currSum, path, answer)
            path.pop()
        
        answer = []
        dfs(root, 0, [], answer)
        return answer
