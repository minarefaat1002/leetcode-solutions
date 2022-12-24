class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = {}
        def dfs(i,row):
            if row == len(triangle):
                return 0
            if (row,i) in dp:
                return dp[(row,i)]
            dp[(row,i)]= triangle[row][i] + min(dfs(i,row+1),dfs(i+1,row+1))
            return dp[(row,i)]
        return dfs(0,0)
        
        '''
        Sum=0
        Min = 999999
        self.backtrack(0,triangle[0][0],triangle,Sum,Min)
        return Min
    def backtrack(self, recurrences, element,triangle: List[List[int]],Sum,Min):
        if recurrences== len(triangle):
            Min = min(Min , Sum)
        Sum += element
        self.backtrack(recurrences+1,triangle[recurrences+1][recurrences] if recurrences+1<4 else 0,triangle,Sum,Min)
        self.backtrack(recurrences+1,triangle[recurrences+1][reccurences+1] if recurrences+1<4 else 0,triangle,Sum,Min)
        '''