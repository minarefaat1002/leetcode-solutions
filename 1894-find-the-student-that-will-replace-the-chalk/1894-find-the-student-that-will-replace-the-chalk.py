class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        iteration = k//sum(chalk)
        Sum = k - iteration*sum(chalk)
        for i in range(len(chalk)):
            Sum -= chalk[i]
            if Sum < 0:
                return i