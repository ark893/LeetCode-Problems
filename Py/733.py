class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        oldColor = image[sr][sc]

        if newColor == oldColor:
            return image

        queue = deque([(sr, sc)])

        while len(queue) > 0:
            i, j = queue.popleft()

            image[i][j] = newColor

            for i, j in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if 0 <= i < m and 0 <= j < n and image[i][j] == oldColor:
                    queue.append((i, j))

        return image
        
        