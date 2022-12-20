class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            Set = set()
            for j in range(len(matrix[0])):
                Set.add(matrix[i][j])
            if len(Set) != len(matrix):
                return False
        for j in range(len(matrix[0])):
            Set = set()
            for i in range(len(matrix)):
                Set.add(matrix[i][j])
            if len(Set) != len(matrix):
                return False
        return True