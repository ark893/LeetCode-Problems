class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
    
        q = deque()
        fresh = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 2:
                    q.append((i,j))
                
                if grid[i][j] == 1:
                    fresh.add((i,j))
                    
        
        if len(fresh)==0:
            return 0
        
        time = 0
        
        while q and fresh:
            
            for _ in range(len(q)):
                
                x,y = q.popleft()
            
                for dirr in [(0,1),(1,0),(0,-1),(-1,0)]:
                    i,j = x+dirr[0], y+dirr[1]
                
                    if (i,j) in fresh:
                        fresh.remove((i,j))
                        q.append((i,j))
            time+=1
                    
        if len(fresh):
            return -1
        
        return time        
                    
                    