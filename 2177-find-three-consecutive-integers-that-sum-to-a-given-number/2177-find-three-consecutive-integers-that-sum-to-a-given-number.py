class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        #x-1,x,x+1 ===> 3x
        if num%3 == 0:
            x = int(num/3)
            return [x-1,x,x+1]
        return []