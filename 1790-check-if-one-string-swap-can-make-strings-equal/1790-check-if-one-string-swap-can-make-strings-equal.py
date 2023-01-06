class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        count1 = Counter(s1)
        count2 = Counter(s2)
        count = 0
        for char1,char2 in zip(s1,s2):
            if  char1 == char2:
                count += 1
        if count == len(s1):
            return True
        if count1 == count2 and count == len(s1) - 2:
            return True
        return False
                