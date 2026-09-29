class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #basically a bfs because we need to check our breadth and go level by level rather than deep first
        #so lets first make note of all the fresh stuff we have (will be important for checking at the end) and then the location sof all our rotten
        fresh=0
        time=0
        q=collections.deque()
        for row in range(0,len(grid)):
            for col in range(0,len(grid[0])):
                if grid[row][col]==1:
                    fresh+=1
                if grid[row][col]==2:
                    q.append((row, col)) #add to queue of rotten
        #now lets traverse
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        while fresh!=0 and q:
            length=len(q)
            for i in range(length):
                r,c=q.popleft()
                for dr, dc in directions:
                    row, col=r+dr, c+dc
                    if (row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col]==1):
                        grid[row][col]=2
                        fresh-=1
                        q.append((row,col))
            time+=1
        return time if fresh ==0 else -1
