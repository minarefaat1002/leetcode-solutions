class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstRow = set(['q','w','e','r','t','y','u','i','o','p'])
        secondRow = set(['a','s','d','f','g','h','j','k','l'])
        thirdRow = set(['z','x','c','v','b','n','m'])
        res = []
        for word in words:
            existsInFirst = True
            existsInSecond = True
            existsInThird = True
            for char in word:
                if char.lower() not in firstRow:
                    existsInFirst = False
            for char in word:
                if char.lower() not in secondRow:
                    existsInSecond = False 
            for char in word:
                 if char.lower() not in thirdRow:
                    existsInThird = False
            if existsInFirst or existsInSecond or existsInThird:
                res.append(word)
        return res
                