class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        for char1 in list(counter1.keys()):
            for char2 in list(counter2.keys()):
                counter1[char1]-=1
                counter2[char2] -=1
                if counter1[char1] == 0:
                    del counter1[char1]
                if counter2[char2] == 0:
                    del counter2[char2]
                counter2[char1] = counter2.get(char1,0) + 1
                counter1[char2] = counter1.get(char2,0) + 1
                if len(counter1) == len(counter2):
                    return True
                counter2[char1]-=1
                counter1[char2]-=1
                if counter2[char1] == 0:
                    del counter2[char1]
                if counter1[char2] == 0:
                    del counter1[char2]
                counter2[char2] = counter2.get(char2,0) + 1
                counter1[char1] = counter1.get(char1,0) + 1
        return False