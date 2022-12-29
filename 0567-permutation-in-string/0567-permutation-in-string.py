class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        freq1 =[0]*26
        freq2 = [0]*26
        for char in s1:
            freq1[ord(char)-ord('a')]+=1
        for i in range(len(s1)):
            freq2[ord(s2[i])-ord('a')]+=1
        for j in range(i+1,len(s2)):
            count = 0
            for ele1,ele2 in zip(freq1,freq2):
                if ele1 == ele2:
                    count+=1
            if count == 26:
                return True
            freq2[ord(s2[j-len(s1)])-ord('a')]-=1
            freq2[ord(s2[j])-ord('a')]+=1
        return False if freq1 != freq2 else True