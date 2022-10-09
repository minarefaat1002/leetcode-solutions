class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        longestTime = logs[0][1]
        idOfTheEmployee = logs[0][0]
        for i in range(1,len(logs)):
            timeTaken = logs[i][1]-logs[i-1][1]
            if timeTaken > longestTime:
                longestTime = timeTaken
                idOfTheEmployee = logs[i][0]
            elif timeTaken == longestTime:
                idOfTheEmployee = min(logs[i][0],idOfTheEmployee)
        return idOfTheEmployee