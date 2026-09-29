class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #valid tree: no cycles, all nodes cannoeced as one component and any two nodes have exactly one path
        #can use dfs to find cycle in graph

        #tree with n nodes must have n-1 edges
        if len(edges)>n-1:
            return False

        #make a graph of the given edges
        edgedict=[[] for _ in range(n)]
        for u,v in edges:
            edgedict[u].append(v)
            edgedict[v].append(u)
        
        visited = set() #track visited nodes
        def dfs(edge, parent):
            if edge in visited:
                return False #cycle detected
            visited.add(edge)
            for neighbor in edgedict[edge]:
                if neighbor==parent:
                    continue
                if not dfs(neighbor, edge):
                    return False
            return True
        #can start dfs from node 0, assuming -1 is a parent
        return dfs(0,-1) and len(visited)==n
        #return true if graph conneced, else false