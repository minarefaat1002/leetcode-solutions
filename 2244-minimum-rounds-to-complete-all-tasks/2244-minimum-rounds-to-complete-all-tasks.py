class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        rounds = 0
        for item in counter:
            if counter[item] == 1:
                return -1 
            else:
                rounds += ceil(counter[item]/3)
        return rounds