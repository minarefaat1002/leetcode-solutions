class Solution:
    def factorial(self,num):
        MOD = 10**9 + 7
        if num <=1:
            return 1
        return num*factorial(num-1)
    def countAnagrams(self, s: str) -> int:
        MOD = 10**9 + 7
        words = s.split(" ")
        anagrams = 1
        for word in words:
            freq = [0]*26
            letters = 0
            for char in word:
                freq[ord(char)-ord('a')] += 1
                letters += 1
            anagramsOfCurrentWord = self.factorial(letters)
            denominator = 1
            for f in freq:
                denominator *= self.factorial(f)
            anagramsOfCurrentWord = anagramsOfCurrentWord//denominator
            anagrams = anagrams*anagramsOfCurrentWord
        return anagrams%MOD
            
            
            