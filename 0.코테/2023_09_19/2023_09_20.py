# 인프런 트리 #2

# 1. 레벨 오더 기본 구조
from collections import deque

""" def bfs(root):
    
    visited = []
    if root is None:
        return None
    
    queue = deque()
    queue.append(root)
    
    while queue:
        cur_node = queue.popleft()
        visited.append(cur_node)
        
        if cur_node.left:
            queue.append(cur_node.left)
        if cur_node.right:
            queue.append(cur_node.right)
    return visited

bfs(root) """


# 2. 레벨오더 잇코테
def maxDepth(root):
    max_depth = 0
    if root is None:
        return max_depth

    queue = deque()
    queue.append((root, 1))

    while queue:
        cur_node, cur_depth = queue.popleft()
        max_depth = cur_depth
        if cur_node.left:
            queue.append((cur_node.left, cur_depth + 1))
        if cur_node.right:
            queue.append((cur_node.right, cur_depth + 1))
    return max_depth


class TreeNode:
    def __init__(self, l=None, r=None, v=0):
        self.left = l
        self.right = r
        self.value = v


root = TreeNode(v=3)
root.left = TreeNode(v=9)
root.right = TreeNode(v=20)
root.right.left = TreeNode(v=15)
root.right.right = TreeNode(v=7)

print(maxDepth(root))
