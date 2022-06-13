class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        result = 0
    
        visited = [[0 for x in range(col)] for y in range(row)] #so that I don't visit the same nodes again
    
        area_store = [0] #for temporarily storing area
    
        def recurv(r,c): #when square is 1
            if row>r>=0 and col>c>=0 and grid[r][c] == 1 and visited[r][c] == 0:
                visited[r][c] = 1
                area_store[0] += 1
			    #recursion
                recurv(r-1,c)
                recurv(r+1,c)
                recurv(r,c-1)
                recurv(r,c+1)
        
            return area_store[0]
        
        for i in range(row):
            for j in range(col):
            
                if grid[i][j] == 0 or visited[i][j] == 1:
                    continue
            
                else:
                    temp = recurv(i,j)
                    area_store[0] = 0
                    result = max(result,temp)
    
        return result