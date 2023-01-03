class Solution:
    def average(self, salary: List[int]) -> float:
        Max = max(salary)
        Min = min(salary)
        Sum = 0
        for i in range(len(salary)):
            if salary[i]<Max and salary[i] > Min:
                Sum+= salary[i]
        return Sum/(len(salary)-2)