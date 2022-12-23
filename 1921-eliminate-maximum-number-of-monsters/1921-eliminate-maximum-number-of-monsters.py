class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        times=[0]*len(dist)
        counter = 0
        for i in range(len(dist)):
            times[i]=dist[i]/speed[i]
        times.sort()
        temp = 0
        for time in times:
            if time-temp > 0:
                counter+=1
                temp+=1
            else:
                break
        return counter 
    # linear solution --->  https://leetcode.com/problems/eliminate-maximum-number-of-monsters/discuss/1314897/C%2B%2B-O(n)-Solution-or-108ms