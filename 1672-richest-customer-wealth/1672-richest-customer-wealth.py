class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        Max = float('-inf')
        for i in range(len(accounts)):
            customerWealth = 0 
            for j in range(len(accounts[0])):
                customerWealth += accounts[i][j]
            Max = max(Max,customerWealth)
        return Max