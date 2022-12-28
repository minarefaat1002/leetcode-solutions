class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}
        for letter in s:
            hashmap[letter]=1+ hashmap.get(letter,0)
            counter = 0
        for key in hashmap:
            counter += hashmap[key]//2 *2
        if counter == len(s):
            return counter 
        elif counter <len(s):
            return counter+1