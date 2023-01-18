class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = [0,0]
        res = []
        i = 0
        j = 0
        d = [-1,1]
        while i < len(mat) and j < len(mat[0]):
            while i>=0 and j>=0 and i < len(mat) and j < len(mat[0]):
                res.append(mat[i][j])
                i+=d[0]
                j+=d[1]
            i-=d[0]
            j-=d[1]
            if i == len(mat)-1:
                j+=1
                d=[-1,1]
            elif j == len(mat[0])-1:
                i+=1
                d=[1,-1]
            elif i == 0:
                j+=1
                d=[1,-1]
            elif j == 0:
                i+=1
                d=[-1,1]
            # if i == 0 and j!=len(mat[0])-1:
            #     j+=1
            #     d = [1,-1]
            # elif j == 0 and i != len(mat)-1:
            #     i+=1
            #     d = [-1,1]
            # elif j == len(mat[0]) - 1:
            #     i+=1
            #     d = [1,-1]
            # elif i == len(mat) - 1:
            #     j+=1
            #     d = [-1,1]
        return res