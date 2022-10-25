class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(sr,sc,newColor):
            if sr<len(image) and sr>-1 and sc<len(image[0]) and sc>-1 and image[sr][sc] == originalColor:
                image[sr][sc] = newColor
                dfs(sr,sc+1,newColor)
                dfs(sr+1,sc,newColor)
                dfs(sr-1,sc,newColor)
                dfs(sr,sc-1,newColor)
        originalColor = image[sr][sc]
        if image[sr][sc]!=newColor:
            dfs(sr,sc,newColor)
        return image
