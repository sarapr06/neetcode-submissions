"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        #can explore nodes and do dfs to get all the nodes of the graph and clone them

        #have a visited set. if we've seen this node before we can stop. 

        visited = {}
        #DON'T USE A SET! not just knowing if we've visited a node, also need to retrieve clone we've made for it so we can wire up the neighbours correctly. instead of a set use a dictionary (hash map) to map og node to brand new clone
        def dfs(node):
            if node in visited:
                #return clone if we've visited
                return visited[node]
            clone=Node(node.val)
            visited[node]=clone
            for neighbour in node.neighbors:
                clone.neighbors.append(dfs(neighbour)) #recursively clone neighbours and apped to clone list
            return clone
        return dfs(node)
        