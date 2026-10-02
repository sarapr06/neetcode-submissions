class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        #equal height or lower
        #can do dfs starting from border cells of grid, want the cells to have a height greater than or equal to current cell. 
        #do hash set from pacfiic and one from atlantic. required coordinates are cells that exist in both pacific and atlantic
        pacific=set()
        atlantic=set()
        def dfs_rec(noded, nodec, seen):
            seen.add((noded, nodec))
            for dr, dc in directions:
                newd, newc=noded+dr, nodec+dc
                if (0<=newd<len(heights) and 0<=newc<len(heights[0]) and (newd, newc) not in seen and heights[newd][newc]>=heights[noded][nodec]):
                        dfs_rec(newd, newc, seen)
        for c in range(len(heights[0])):
            dfs_rec(0,c,pacific)
            dfs_rec(len(heights)-1, c, atlantic)
        for r in range(len(heights)):
            dfs_rec(r,0,pacific)
            dfs_rec(r, len(heights[0])-1, atlantic)
        res=[]
        for r, c in pacific.intersection(atlantic):
            res.append([r,c])
        #doing bfs for each cell will be costly!
        return res
        