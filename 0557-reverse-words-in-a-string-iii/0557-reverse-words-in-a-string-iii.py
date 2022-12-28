class Solution:
    def reverseWords(self, s: str) -> str:
        newS = ""
        def reverseWord(word):
            word = list(word)
            l = 0
            r = len(word)-1
            while l <= r:
                temp = word[r]
                word[r] = word[l]
                word[l] = temp
                l+=1
                r-=1
            return "".join(word)
        stack = s.split(" ")
        for word in stack:
            newS+=reverseWord(word)+" "
        return newS[:-1:]

