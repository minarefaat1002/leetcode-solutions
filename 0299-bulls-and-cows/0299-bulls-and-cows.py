class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        hashMap1 = {}
        hashMap2 = {}
        for char1,char2 in zip(secret,guess):
            if char1 == char2:
                bulls += 1
            else:
                hashMap1[char1] = hashMap1.get(char1,0) + 1
                hashMap2[char2] = hashMap2.get(char2,0) + 1
        for item in hashMap2:
            cows += min(hashMap2[item],hashMap1.get(item,0))
        return str(bulls) + "A" +  str(cows) + "B"