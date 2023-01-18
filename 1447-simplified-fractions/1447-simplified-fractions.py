class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        Set = set()
        res = []
        for i in range(2,n+1):
            for j in range(1,i):
                if j/i not in Set:
                    Set.add(j/i)
                    res.append(str(j)+"/"+str(i))
        return res