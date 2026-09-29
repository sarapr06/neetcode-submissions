class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #cannot do dfs because we explore deep rather than level by level
        #LEVEL BY LEVEL SO BFS (multi-level)
        #bfs: at each second, rot oranges adjacent to rotten ones. store rotten oranges in queue and process them in one go. time at which fresh orange getes rotten is level at which it is visit4ed. 

        #traverse grid and store rotten oranges in a queue. run a bfs, processing current level of rotten oranges and visiting adjacent cells of each rotten orange. insert adj cenll into queue if it contains fresh orange. continue until queue is empty. level at which we stop bfs is hte answer

        #check if all oranges rotted by traversing grid. if any fresh is found, return 1. else return level. 

        #1. intiialize queue with positions of all rotten oranges
        q=collections.deque()
        fresh=0
        time=0
        #2. count total number of fresh oranges
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append((r,c)) #location of rotten
        directions=[[0,1],[0,-1],[1,0],[-1,0]]

        #3. while queue NOT empty AND fresh oranges:
        #process all nodes in queue (one bfs level)
        #for each rotten orange, check its 4 neighbours. if fresh, make it rotten, decrease fresh count, add to queue. increment time by 1
        #if fresh count becomes 0, return time. else return 1 (some oranges never rot)
        while fresh>0 and q:
            length=len(q)
            for i in range(length):
                r,c=q.popleft()
                for dr, dc in directions:
                    row,col=r+dr, c+dc #go in all directions
                    if(row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col]==1): #if valid direction and we chose something fresh
                        grid[row][col]=2 #make rotten!
                        q.append((row, col)) #new rotten
                        fresh-=1
            time+=1
        return time if fresh==0 else -1
