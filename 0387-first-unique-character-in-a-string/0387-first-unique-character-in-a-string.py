class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashset = {}
        pivot =-1
        Letter = None
        for letter in s:
            hashset[letter]= hashset.get(letter,0)+1
        for i in range(len(s)):
            if hashset[s[i]] == 1:
                return i 
        return -1