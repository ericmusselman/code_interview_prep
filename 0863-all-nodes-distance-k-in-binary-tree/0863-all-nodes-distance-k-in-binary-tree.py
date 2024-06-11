# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        # convert tree to undirected graph, then use BFS and step k times
        def dfs(node, parent):
            if not node:
                return
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root, None)
        queue = deque([target])
        seen = {target}
        distance = 0
        
        while queue and distance < k:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                for neighbor in [node.parent, node.left, node.right]:
                    if neighbor and neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
            distance += 1
        return [node.val for node in queue]