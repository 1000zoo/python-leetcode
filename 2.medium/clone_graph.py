from typing import Optional
from ..util.node import Node

class Solution:

    """
    Runtime 40 ms Beats 57.42%
    """
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None
            
        q = [node]
        clones = {node.val: Node(node.val, [])}

        while q:
            curr = q.pop(0)
            pointer = clones[curr.val]

            for n in curr.neighbors:
                if n.val not in clones:
                    clones[n.val] = Node(n.val, [])
                    q.append(n)
                pointer.neighbors.append(clones[n.val])

        return clones[node.val]