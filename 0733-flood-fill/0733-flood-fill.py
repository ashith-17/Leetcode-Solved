class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        original = image[sr][sc]

        if original == color:
            return image

        rows = len(image)
        cols = len(image[0])

        def dfs(r, c):
            image[r][c] = color

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original:
                    dfs(nr, nc)

        dfs(sr, sc)

        return image