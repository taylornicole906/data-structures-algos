"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node: return
        
        seen = {}  # node value: node itself  
        
        def dfs(node):
            
            newNode = Node(node.val)            
            seen[node.val] = newNode
            newNeighbors = []
            
            for n in node.neighbors:
                if n.val not in seen:
                    newNeighbors.append(dfs(n))
                else: 
                    newNeighbors.append(seen[n.val])
            newNode.neighbors = newNeighbors
            
            
            return newNode
            
        return dfs(node)
        
        
        
        
                    
            
            