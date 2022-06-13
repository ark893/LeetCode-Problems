from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        visited = set()
        q = deque()
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    visited.add((i,j))
                    q.append((i,j))
                    
        
        while q:
            x,y = q.popleft()
            
            for direction in [(0,1),(1,0),(0,-1),(-1,0)]:
                
                i,j = x+direction[0], y+direction[1]
                
                if 0<=i<len(mat) and 0<=j<len(mat[0]) and (i,j) not in visited:
                    visited.add((i,j))
                    mat[i][j] = mat[x][y] +1
                    q.append((i,j))
                    
        
        return mat