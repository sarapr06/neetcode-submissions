class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #valid tree if acylic and for vertices n has edges n-1
        if len(edges)>n-1:
            return False
        #make a graph of the edges
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited=set()
        #dfs on this to find cycles and see if valid
        def dfs(edge, parent):
            if edge in visited:
                return False
            visited.add(edge)
            for neighbour in adj[edge]:
                if neighbour==parent:
                    continue
                if not dfs(neighbour, edge):
                    return False
            return True
        return dfs(0,-1) and len(visited)==n