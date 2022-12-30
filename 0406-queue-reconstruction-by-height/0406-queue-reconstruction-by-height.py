class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = [[1000000+1]]*len(people)
        people = sorted(people,key = lambda x: (x[0]))
        for i,person in enumerate(people):
            count = person[1]
            j = 0
            while count > 0 or res[j][0] != 1000001:
                if res[j][0] >= person[0]:
                    count-=1
                j+=1
            res[j] = person
        return res