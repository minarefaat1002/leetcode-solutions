class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.nextExists = True
        self.combinationLength = combinationLength
        self.characters = characters
        self.length = len(characters)
        self.arr = [0 for _ in range(self.length)]
        for i in range(combinationLength):
            self.arr[i] = 1

    def next(self) -> str:
        count = 0 
        i = self.length - 1
        while i>=0 and self.arr[i] == 1:
            i-=1
            count+=1
        if count == self.combinationLength:
            self.nextExists = False
        cur = ""
        rightMostOne = -1
        for i in range(self.length):
            if self.arr[i] == 1:
                cur+=self.characters[i]
                rightMostOne = i
        if rightMostOne != self.length-1:
            self.arr[rightMostOne+1] = 1
            self.arr[rightMostOne] = 0
        else:
            k = 0
            for i in range(self.length-1,0,-1):
                if self.arr[i] == 1:
                    k+=1
                if self.arr[i] == 0 and self.arr[i-1] == 1:
                    self.arr[i] = 1
                    self.arr[i-1] = 0
                    break
            if not self.nextExists:
                return cur
            for j in range(i+1,i+k+1):
                self.arr[j] = 1
            for z in range(j+1,self.length):
                self.arr[z] = 0
        return cur

    def hasNext(self) -> bool:
        return self.nextExists


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()